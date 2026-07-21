# Top Page Redesign & Category Routing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the top page of the Astro web portal to feature 6 university/category cards (Todai, Titech, Kyodai x Zenki, Kouki) with Astro View Transitions, routing to dedicated category solution list pages.

**Architecture:** Add `ViewTransitions` to `Layout.astro`. Create dynamic category list pages at `/category/[university]/[category].astro` that render year-grouped solutions. Redesign `index.astro` to display the 6 cards with interactive search and shared element transitions. Update breadcrumbs in `solutions/[...slug].astro`.

**Tech Stack:** Astro 4.11.3, HTML5, Vanilla CSS (Glassmorphism design tokens), TypeScript, ViewTransitions (`astro:transitions`).

## Global Constraints

- Astro version: 4.11.3
- Target 6 categories: `todai`/`zenki`, `todai`/`kouki`, `titech`/`zenki`, `titech`/`kouki`, `kyodai`/`zenki`, `kyodai`/`kouki` (with support for `sample_*` aliases)
- Build command: `export PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" && cd web && npm run build`

---

### Task 1: Add View Transitions to Layout.astro

**Files:**
- Modify: `web/src/layouts/Layout.astro`

**Interfaces:**
- Consumes: `ViewTransitions` from `astro:transitions`
- Produces: Smooth page transitions and shared element transition capabilities for all routes using `Layout`

- [ ] **Step 1: Update Layout.astro to import and include ViewTransitions**

Add `import { ViewTransitions } from 'astro:transitions';` inside frontmatter, and place `<ViewTransitions />` inside `<head>`.

```astro
---
import { ViewTransitions } from 'astro:transitions';

interface Props {
	title: string;
	description?: string;
}

const { title, description = "東大・京大・東工大などの大学入試数学過去問解答アーカイブ。KaTeX描画による高品質な数式と解答解説。" } = Astro.props;
const baseUrl = import.meta.env.BASE_URL.replace(/\/$/, '');
---
```
And inside `<head>`:
```astro
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
		
		<ViewTransitions />
```

- [ ] **Step 2: Run build verification**

Run: `export PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" && cd web && npm run build`
Expected: Build passes with 0 errors.

- [ ] **Step 3: Commit**

```bash
git add web/src/layouts/Layout.astro
git commit -m "feat(web): add ViewTransitions to Layout.astro"
```

---

### Task 2: Create Category List Page (`web/src/pages/category/[university]/[category].astro`)

**Files:**
- Create: `web/src/pages/category/[university]/[category].astro`

**Interfaces:**
- Consumes: `getCollection('solutions')` from `astro:content`
- Produces: Category list route (`/category/[university]/[category]`) rendering solutions grouped by year for a specific university and category

- [ ] **Step 1: Create `web/src/pages/category/[university]/[category].astro`**

Implement `getStaticPaths` for the 6 target university and category combinations (including `sample_*` prefix support).

```astro
---
import { getCollection } from 'astro:content';
import Layout from '../../../layouts/Layout.astro';

export async function getStaticPaths() {
	const solutions = await getCollection('solutions');
	
	const targetCategories = [
		{ university: 'todai', category: 'zenki' },
		{ university: 'todai', category: 'kouki' },
		{ university: 'titech', category: 'zenki' },
		{ university: 'titech', category: 'kouki' },
		{ university: 'kyodai', category: 'zenki' },
		{ university: 'kyodai', category: 'kouki' },
		{ university: 'sample_todai', category: 'zenki' },
		{ university: 'sample_todai', category: 'kouki' },
		{ university: 'sample_titech', category: 'zenki' },
		{ university: 'sample_titech', category: 'kouki' },
		{ university: 'sample_kyodai', category: 'zenki' },
		{ university: 'sample_kyodai', category: 'kouki' },
	];

	return targetCategories.map(({ university, category }) => {
		const filteredSolutions = solutions.filter((s) => {
			const itemUniv = s.data.university;
			const matchUniv = itemUniv === university || itemUniv === `sample_${university}` || `sample_${itemUniv}` === university;
			return matchUniv && s.data.category === category;
		});

		return {
			params: { university, category },
			props: {
				university,
				category,
				solutions: filteredSolutions,
				allSolutions: solutions,
			},
		};
	});
}

const { university, category, solutions } = Astro.props;
const baseUrl = import.meta.env.BASE_URL.replace(/\/$/, '');

const UNIVERSITY_NAMES: Record<string, string> = {
	sample_todai: '東京大学',
	sample_titech: '東京工業大学',
	sample_kyodai: '京都大学',
	todai: '東京大学',
	titech: '東京工業大学',
	kyodai: '京都大学',
};

const CATEGORY_NAMES: Record<string, string> = {
	zenki: '前期 理系数学',
	kouki: '後期 理系数学',
};

const univName = UNIVERSITY_NAMES[university] || university;
const catName = CATEGORY_NAMES[category] || category;

// Group solutions by year -> question
interface QuestionGroup {
	questionNum: string;
	summaryItem?: typeof solutions[0];
	problemItem?: typeof solutions[0];
	solutionItem?: typeof solutions[0];
}

interface YearGroup {
	year: string;
	questions: QuestionGroup[];
}

const yearGroupsMap = new Map<string, QuestionGroup[]>();

for (const item of solutions) {
	const yearStr = item.data.year;
	const qNum = item.data.question;

	if (!yearGroupsMap.has(yearStr)) {
		yearGroupsMap.set(yearStr, []);
	}
	const qList = yearGroupsMap.get(yearStr)!;

	let qGroup = qList.find((q) => q.questionNum === qNum);
	if (!qGroup) {
		qGroup = { questionNum: qNum };
		qList.push(qGroup);
	}

	if (item.data.type === 'summary' || qNum === '0') {
		qGroup.summaryItem = item;
	} else if (item.data.type === 'problem') {
		qGroup.problemItem = item;
	} else {
		qGroup.solutionItem = item;
	}
}

const yearGroups: YearGroup[] = Array.from(yearGroupsMap.entries()).map(([year, questions]) => {
	questions.sort((a, b) => {
		if (a.questionNum === '0') return -1;
		if (b.questionNum === '0') return 1;
		return a.questionNum.localeCompare(b.questionNum, undefined, { numeric: true });
	});
	return { year, questions };
});

yearGroups.sort((a, b) => b.year.localeCompare(a.year));
---

<Layout title={`${univName} ${catName} | Math Solutions`}>
	<div class="category-page">
		<nav class="breadcrumb">
			<a href={`${baseUrl}/`}>トップ</a>
			<span class="sep">/</span>
			<span class="current">{univName} {catName}</span>
		</nav>

		<header class="category-header" transition:name={`card-${university}-${category}`}>
			<div class="badge-row">
				<span class="univ-badge">{univName}</span>
				<span class="cat-badge">{catName}</span>
			</div>
			<h1>{univName} <span class="highlight">{catName}</span></h1>
			<p class="count-info">収録問題数: <strong>{solutions.length}</strong> 件</p>
		</header>

		{solutions.length === 0 ? (
			<div class="empty-state glass">
				<div class="empty-icon">📝</div>
				<h2>現在データを準備中です</h2>
				<p>このカテゴリの過去問・解答データは順次追加予定です。</p>
				<a href={`${baseUrl}/`} class="btn-primary">トップページへ戻る</a>
			</div>
		) : (
			<div class="year-sections">
				{yearGroups.map((yg) => (
					<section class="year-card glass">
						<div class="year-header">
							<h2>{yg.year}年度</h2>
							<span class="year-count">{yg.questions.length}問</span>
						</div>
						<div class="questions-grid">
							{yg.questions.map((q) => (
								<div class="question-row">
									<div class="q-label">
										{q.questionNum === '0' ? (
											<span class="tag-summary">全体サマリ</span>
										) : (
											<span class="tag-num">第{q.questionNum}問</span>
										)}
									</div>
									<div class="q-actions">
										{q.summaryItem && (
											<a href={`${baseUrl}/solutions/${q.summaryItem.slug}`} class="action-btn summary">
												サマリを見る ➔
											</a>
										)}
										{q.problemItem && (
											<a href={`${baseUrl}/solutions/${q.problemItem.slug}`} class="action-btn problem">
												問題 ➔
											</a>
										)}
										{q.solutionItem && (
											<a href={`${baseUrl}/solutions/${q.solutionItem.slug}`} class="action-btn solution">
												解答・解説 ➔
											</a>
										)}
									</div>
								</div>
							))}
						</div>
					</section>
				))}
			</div>
		)}
	</div>
</Layout>

<style>
	.category-page {
		max-width: 1000px;
		margin: 0 auto;
		padding: 2rem 1.5rem 4rem;
	}

	.breadcrumb {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		font-size: 0.9rem;
		color: var(--text-muted);
		margin-bottom: 2rem;
	}
	.breadcrumb a {
		color: var(--primary);
		text-decoration: none;
	}
	.breadcrumb a:hover {
		text-decoration: underline;
	}

	.category-header {
		padding: 2.5rem;
		background: rgba(15, 23, 42, 0.7);
		border: 1px solid var(--glass-border);
		border-radius: 20px;
		margin-bottom: 2.5rem;
		backdrop-filter: blur(12px);
	}
	.badge-row {
		display: flex;
		gap: 0.5rem;
		margin-bottom: 0.75rem;
	}
	.univ-badge, .cat-badge {
		padding: 0.25rem 0.75rem;
		border-radius: 999px;
		font-size: 0.8rem;
		font-weight: 600;
	}
	.univ-badge {
		background: rgba(96, 165, 250, 0.15);
		color: var(--primary);
		border: 1px solid rgba(96, 165, 250, 0.3);
	}
	.cat-badge {
		background: rgba(52, 211, 153, 0.15);
		color: var(--secondary);
		border: 1px solid rgba(52, 211, 153, 0.3);
	}

	.category-header h1 {
		font-size: 2.2rem;
		font-weight: 800;
		margin: 0 0 0.5rem;
	}
	.category-header .highlight {
		color: var(--primary);
	}
	.count-info {
		color: var(--text-muted);
		margin: 0;
	}

	.empty-state {
		text-align: center;
		padding: 4rem 2rem;
		border-radius: 16px;
	}
	.empty-icon {
		font-size: 3rem;
		margin-bottom: 1rem;
	}
	.btn-primary {
		display: inline-block;
		margin-top: 1.5rem;
		padding: 0.75rem 1.5rem;
		background: var(--primary);
		color: #000;
		font-weight: 700;
		border-radius: 10px;
		text-decoration: none;
	}

	.year-sections {
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
	}
	.year-card {
		padding: 1.5rem;
		border-radius: 16px;
	}
	.year-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		border-bottom: 1px solid var(--glass-border);
		padding-bottom: 1rem;
		margin-bottom: 1rem;
	}
	.year-header h2 {
		margin: 0;
		font-size: 1.4rem;
	}
	.year-count {
		font-size: 0.85rem;
		color: var(--text-subtle);
	}

	.questions-grid {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}
	.question-row {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 0.75rem 1rem;
		background: rgba(30, 41, 59, 0.4);
		border-radius: 10px;
		flex-wrap: wrap;
		gap: 0.5rem;
	}
	.tag-summary {
		background: rgba(167, 139, 250, 0.2);
		color: var(--accent);
		padding: 0.2rem 0.6rem;
		border-radius: 6px;
		font-size: 0.85rem;
		font-weight: 600;
	}
	.tag-num {
		font-weight: 700;
		font-size: 1rem;
	}
	.q-actions {
		display: flex;
		gap: 0.5rem;
	}
	.action-btn {
		padding: 0.4rem 0.8rem;
		border-radius: 8px;
		text-decoration: none;
		font-size: 0.85rem;
		font-weight: 600;
		transition: all 0.2s;
	}
	.action-btn.summary {
		background: rgba(167, 139, 250, 0.15);
		color: var(--accent);
		border: 1px solid rgba(167, 139, 250, 0.3);
	}
	.action-btn.problem {
		background: rgba(96, 165, 250, 0.15);
		color: var(--primary);
		border: 1px solid rgba(96, 165, 250, 0.3);
	}
	.action-btn.solution {
		background: rgba(52, 211, 153, 0.15);
		color: var(--secondary);
		border: 1px solid rgba(52, 211, 153, 0.3);
	}
	.action-btn:hover {
		transform: translateY(-2px);
		filter: brightness(1.2);
	}
</style>
```

- [ ] **Step 2: Build test**

Run: `export PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" && cd web && npm run build`
Expected: Build succeeds with category route pages generated.

- [ ] **Step 3: Commit**

```bash
git add web/src/pages/category/[university]/[category].astro
git commit -m "feat(web): add category list dynamic page"
```

---

### Task 3: Redesign Top Page (`web/src/pages/index.astro`)

**Files:**
- Modify: `web/src/pages/index.astro`

**Interfaces:**
- Consumes: `getCollection('solutions')` from `astro:content`
- Produces: Redesigned top page displaying 6 university/category cards grid with search and navigation to `/category/[university]/[category]`

- [ ] **Step 1: Replace `web/src/pages/index.astro` content**

Implement the 6 cards grid (Todai/Titech/Kyodai x Zenki/Kouki), matching `transition:name`, search bar filtering, and quick links.

```astro
---
import { getCollection } from 'astro:content';
import Layout from '../layouts/Layout.astro';

const allSolutions = await getCollection('solutions');
const baseUrl = import.meta.env.BASE_URL.replace(/\/$/, '');

// Target 6 categories configuration
const CATEGORIES_CONFIG = [
	{
		id: 'todai-zenki',
		universityId: 'todai',
		categoryId: 'zenki',
		univName: '東京大学',
		catName: '前期 理系数学',
		aliases: '東大 とうだい utokyo',
		color: '#ef4444',
		gradient: 'linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(15, 23, 42, 0.8))',
		border: 'rgba(239, 68, 68, 0.3)',
	},
	{
		id: 'todai-kouki',
		universityId: 'todai',
		categoryId: 'kouki',
		univName: '東京大学',
		catName: '後期 理系数学',
		aliases: '東大 とうだい utokyo',
		color: '#f43f5e',
		gradient: 'linear-gradient(135deg, rgba(244, 63, 94, 0.15), rgba(15, 23, 42, 0.8))',
		border: 'rgba(244, 63, 94, 0.3)',
	},
	{
		id: 'titech-zenki',
		universityId: 'titech',
		categoryId: 'zenki',
		univName: '東京工業大学',
		catName: '前期 理系数学',
		aliases: '東工大 とうこうだい titech',
		color: '#10b981',
		gradient: 'linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(15, 23, 42, 0.8))',
		border: 'rgba(16, 185, 129, 0.3)',
	},
	{
		id: 'titech-kouki',
		universityId: 'titech',
		categoryId: 'kouki',
		univName: '東京工業大学',
		catName: '後期 理系数学',
		aliases: '東工大 とうこうだい titech',
		color: '#34d399',
		gradient: 'linear-gradient(135deg, rgba(52, 211, 153, 0.15), rgba(15, 23, 42, 0.8))',
		border: 'rgba(52, 211, 153, 0.3)',
	},
	{
		id: 'kyodai-zenki',
		universityId: 'kyodai',
		categoryId: 'zenki',
		univName: '京都大学',
		catName: '前期 理系数学',
		aliases: '京大 きょうだい kyodai',
		color: '#8b5cf6',
		gradient: 'linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(15, 23, 42, 0.8))',
		border: 'rgba(139, 92, 246, 0.3)',
	},
	{
		id: 'kyodai-kouki',
		universityId: 'kyodai',
		categoryId: 'kouki',
		univName: '京都大学',
		catName: '後期 理系数学',
		aliases: '京大 きょうだい kyodai',
		color: '#a78bfa',
		gradient: 'linear-gradient(135deg, rgba(167, 139, 250, 0.15), rgba(15, 23, 42, 0.8))',
		border: 'rgba(167, 139, 250, 0.3)',
	},
];

// Calculate item count per category
const categoriesData = CATEGORIES_CONFIG.map((cfg) => {
	const count = allSolutions.filter((item) => {
		const u = item.data.university;
		const matchUniv = u === cfg.universityId || u === `sample_${cfg.universityId}` || `sample_${u}` === cfg.universityId;
		return matchUniv && item.data.category === cfg.categoryId;
	}).length;

	return {
		...cfg,
		count,
	};
});
---

<Layout title="大学入試数学 過去問解答ポータル">
	<div class="container">
		<!-- Hero Section -->
		<header class="hero">
			<div class="hero-badge">🎓 難関大学入試数学データベース</div>
			<h1 class="hero-title">
				大学入試数学 <span class="gradient-text">過去問＆詳細解答</span>
			</h1>
			<p class="hero-desc">
				東京大学・東京工業大学・京都大学の過年度数学問題および丁寧な解答解説、全体サマリを収録。
			</p>
		</header>

		<!-- Category Cards Section -->
		<section class="categories-section">
			<div class="section-header">
				<h2>大学・試験区分から探す</h2>
				<p>目的の大学・試験区分カードを選択してください</p>
			</div>

			<div class="grid-6">
				{categoriesData.map((cat) => (
					<a
						href={`${baseUrl}/category/${cat.universityId}/${cat.categoryId}`}
						class="card-item glass"
						style={`background: ${cat.gradient}; border-color: ${cat.border};`}
						transition:name={`card-${cat.universityId}-${cat.categoryId}`}
					>
						<div class="card-top">
							<span class="univ-tag" style={`background: ${cat.color}22; color: ${cat.color}; border: 1px solid ${cat.color}44;`}>
								{cat.univName}
							</span>
							<span class="count-badge" style={cat.count > 0 ? `background: ${cat.color}; color: #000;` : `background: rgba(255,255,255,0.1); color: var(--text-muted);`}>
								{cat.count > 0 ? `${cat.count}問` : '準備中'}
							</span>
						</div>

						<div class="card-body">
							<h3 class="cat-title">{cat.univName}</h3>
							<p class="cat-subtitle" style={`color: ${cat.color};`}>{cat.catName}</p>
						</div>

						<div class="card-footer">
							<span class="enter-text">問題一覧を見る</span>
							<span class="arrow">➔</span>
						</div>
					</a>
				))}
			</div>
		</section>
	</div>
</Layout>

<style>
	.container {
		max-width: 1100px;
		margin: 0 auto;
		padding: 3rem 1.5rem 5rem;
	}

	.hero {
		text-align: center;
		margin-bottom: 4rem;
	}

	.hero-badge {
		display: inline-block;
		padding: 0.4rem 1rem;
		background: rgba(96, 165, 250, 0.1);
		border: 1px solid rgba(96, 165, 250, 0.25);
		border-radius: 999px;
		font-size: 0.85rem;
		font-weight: 600;
		color: var(--primary);
		margin-bottom: 1.25rem;
	}

	.hero-title {
		font-size: clamp(2rem, 5vw, 3.2rem);
		font-weight: 800;
		line-height: 1.2;
		margin: 0 0 1rem;
	}

	.gradient-text {
		background: linear-gradient(135deg, #60a5fa 0%, #34d399 50%, #a78bfa 100%);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.hero-desc {
		font-size: 1.1rem;
		color: var(--text-muted);
		max-width: 650px;
		margin: 0 auto;
	}

	.section-header {
		margin-bottom: 2rem;
	}
	.section-header h2 {
		font-size: 1.8rem;
		font-weight: 700;
		margin: 0 0 0.25rem;
	}
	.section-header p {
		color: var(--text-subtle);
		margin: 0;
	}

	.grid-6 {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
		gap: 1.5rem;
	}

	.card-item {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		padding: 1.75rem;
		border-radius: 20px;
		text-decoration: none;
		color: inherit;
		transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
		min-height: 180px;
	}

	.card-item:hover {
		transform: translateY(-6px);
		box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.5);
		filter: brightness(1.1);
	}

	.card-top {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.univ-tag {
		padding: 0.2rem 0.6rem;
		border-radius: 6px;
		font-size: 0.8rem;
		font-weight: 700;
	}

	.count-badge {
		padding: 0.2rem 0.6rem;
		border-radius: 999px;
		font-size: 0.75rem;
		font-weight: 700;
	}

	.card-body {
		margin: 1.25rem 0;
	}

	.cat-title {
		font-size: 1.4rem;
		font-weight: 800;
		margin: 0 0 0.25rem;
	}

	.cat-subtitle {
		font-size: 0.95rem;
		font-weight: 600;
		margin: 0;
	}

	.card-footer {
		display: flex;
		align-items: center;
		justify-content: space-between;
		font-size: 0.85rem;
		font-weight: 600;
		color: var(--text-muted);
		border-top: 1px solid rgba(255, 255, 255, 0.05);
		padding-top: 0.75rem;
	}

	.card-item:hover .arrow {
		transform: translateX(4px);
		color: var(--text-main);
	}
	.arrow {
		transition: transform 0.2s;
	}
</style>
```

- [ ] **Step 2: Run build verification**

Run: `export PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" && cd web && npm run build`
Expected: Build succeeds cleanly.

- [ ] **Step 3: Commit**

```bash
git add web/src/pages/index.astro
git commit -m "feat(web): redesign top page with 6 category cards grid"
```

---

### Task 4: Update Solution Detail Breadcrumbs (`web/src/pages/solutions/[...slug].astro`)

**Files:**
- Modify: `web/src/pages/solutions/[...slug].astro`

**Interfaces:**
- Consumes: `entry.data.university` and `entry.data.category`
- Produces: Improved breadcrumbs navigation pointing back to `/category/${univId}/${catId}`

- [ ] **Step 1: Update breadcrumbs in `web/src/pages/solutions/[...slug].astro`**

Find the `<div class="breadcrumb">` or add breadcrumb navigation pointing back to `/category/${university}/${category}`.

```astro
		<!-- Breadcrumbs -->
		<nav class="breadcrumb">
			<a href={`${baseUrl}/`}>トップ</a>
			<span class="sep">/</span>
			<a href={`${baseUrl}/category/${entry.data.university.replace(/^sample_/, '')}/${entry.data.category}`}>
				{univName} {catName}
			</a>
			<span class="sep">/</span>
			<span class="current">{year}年 {questionLabel}</span>
		</nav>
```

- [ ] **Step 2: Run build verification**

Run: `export PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" && cd web && npm run build`
Expected: Build completes with 0 errors.

- [ ] **Step 3: Commit**

```bash
git add web/src/pages/solutions/[...slug].astro
git commit -m "feat(web): update solution detail breadcrumbs to category page link"
```

---

### Task 5: Complete Verification & Sanity Check

- [ ] **Step 1: Run Full Astro Build**

Run: `export PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" && cd web && npm run build`
Expected: Success with all static pages generated.

- [ ] **Step 2: Inspect Generated Output with view_file**

Inspect `web/dist/index.html` or generated category HTML using `view_file` to verify structure and links.
