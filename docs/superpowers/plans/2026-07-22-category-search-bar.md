# Category Page Real-time Search Bar Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an interactive real-time search bar to the category list page (`web/src/pages/category/[university]/[category].astro`) that filters years and question items instantly based on user input.

**Architecture:** Add a glassmorphism search input component and client-side JavaScript to `category/[university]/[category].astro` that listens for `input` events, filters `.question-row` and `.year-card` elements, handles ViewTransitions page swap lifecycle (`astro:page-load`), and toggles a "No results found" state.

**Tech Stack:** Astro 4.11.3, Vanilla JavaScript, CSS Glassmorphism.

## Global Constraints

- Must work seamlessly with Astro ViewTransitions (`astro:page-load` event handling for client script re-initialization).
- Must filter both year blocks and individual question rows dynamically without triggering page reloads.

---

### Task 1: Add Search Bar & Client-side Filtering Script to Category Page

**Files:**
- Modify: `web/src/pages/category/[university]/[category].astro`

**Interfaces:**
- Consumes: `.question-row` (with `data-search-text` attribute containing year and question number) and `.year-card`
- Produces: Instant interactive search filtering UI on `/category/[university]/[category]`

- [ ] **Step 1: Update `web/src/pages/category/[university]/[category].astro`**

Add the search bar UI above `.year-sections`, add `data-search-text` attributes to question rows and year cards, add a "No matching results" container, and add client script listening on `input` and `astro:page-load`.

```astro
		<!-- Search Bar -->
		{solutions.length > 0 && (
			<div class="search-container">
				<div class="search-box glass">
					<span class="search-icon">🔍</span>
					<input
						type="text"
						id="category-search-input"
						placeholder="年度や問題番号で検索... (例: 1995, 第1問, サマリ)"
						autocomplete="off"
					/>
					<button id="search-clear-btn" class="clear-btn" aria-label="検索をクリア" style="display: none;">✕</button>
				</div>
			</div>
		)}

		<!-- No Results State -->
		<div id="no-results-msg" class="empty-state glass" style="display: none;">
			<div class="empty-icon">🔍</div>
			<h2>該当する問題が見つかりません</h2>
			<p>検索キーワードを変更してお試しください。</p>
		</div>
```

Client script logic:
```html
<script>
	function setupCategorySearch() {
		const searchInput = document.getElementById('category-search-input') as HTMLInputElement | null;
		const clearBtn = document.getElementById('search-clear-btn') as HTMLButtonElement | null;
		const yearCards = document.querySelectorAll('.year-card');
		const noResultsMsg = document.getElementById('no-results-msg');

		if (!searchInput) return;

		function filterItems() {
			const query = searchInput.value.trim().toLowerCase();
			let hasAnyMatch = false;

			if (clearBtn) {
				clearBtn.style.display = query.length > 0 ? 'block' : 'none';
			}

			yearCards.forEach((yearCard) => {
				const qRows = yearCard.querySelectorAll('.question-row');
				let visibleCount = 0;

				qRows.forEach((row) => {
					const searchText = (row.getAttribute('data-search-text') || '').toLowerCase();
					if (query === '' || searchText.includes(query)) {
						(row as HTMLElement).style.display = 'flex';
						visibleCount++;
					} else {
						(row as HTMLElement).style.display = 'none';
					}
				});

				if (visibleCount > 0) {
					(yearCard as HTMLElement).style.display = 'block';
					hasAnyMatch = true;
				} else {
					(yearCard as HTMLElement).style.display = 'none';
				}
			});

			if (noResultsMsg) {
				noResultsMsg.style.display = !hasAnyMatch && query !== '' ? 'block' : 'none';
			}
		}

		searchInput.addEventListener('input', filterItems);

		if (clearBtn) {
			clearBtn.addEventListener('click', () => {
				searchInput.value = '';
				filterItems();
				searchInput.focus();
			});
		}
	}

	// Initialize on page load and View Transitions swap
	setupCategorySearch();
	document.addEventListener('astro:page-load', setupCategorySearch);
</script>
```

- [ ] **Step 2: Run build verification**

Run: `export PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" && cd web && npm run build`
Expected: Build passes with 0 errors.

- [ ] **Step 3: Commit**

```bash
git add web/src/pages/category/[university]/[category].astro
git commit -m "feat(web): add real-time search bar to category list page"
```
