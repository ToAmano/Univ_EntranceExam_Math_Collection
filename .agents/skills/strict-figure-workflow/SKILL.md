---
name: strict-figure-workflow
description: Use when creating, replacing, or modifying figures (TikZ, includegraphics, zahyou, TODOs) in LaTeX solutions, especially when instructed to update ONLY figures without altering surrounding prose, formulas, preamble, or headings.
---

# Strict Figure Workflow (LaTeX / TikZ)

## Overview

When tasked with adding, replacing, or modifying figures in this repository, **you must only touch figure blocks**. Modifying surrounding text, converting `\[ ... \]` to `align`, changing headings, fixing cross-references, or modernizing preambles (`jarticle` to `subfiles`) is strictly prohibited unless explicitly requested by the user.

This workflow guarantees compliance by enforcing both TikZ styling guidelines and mechanical diff verification.

---

## 4-Step Execution Workflow

```
[1. Target Inspection] ──> [2. Draw TikZ] ──> [3. Diff Verification] ──> [4. Visual Proof]
                                                     │
                                            FAIL? Revert non-fig edits
```

### Step 1: Target Inspection
Before touching any code:
1. Identify the exact figure block to replace:
   - Old `figure` environment
   - Old `emath` environment (`\begin{zahyou} ... \end{zahyou}`)
   - Old graphic snippet (`\begin{center}\includegraphics...\end{center}`)
   - TODO comment (e.g. `% TODO: 概要図`)
2. Note the surrounding context so you do NOT accidentally delete or reformat surrounding formulas, headings, or paragraph text.

### Step 2: Draw TikZ (Following AGENTS.md Rules)
Write the new `figure` block strictly adhering to the repository conventions:
- **Dots/Points**: Use `\node[circle, fill, inner sep=...pt] at (...) {};` (NEVER `circle` path, which distorts when `xscale != yscale`).
- **Shading/Regions**: Always use hatching patterns (`pattern=north east lines`, `pattern color=...`), not just faint flat fills.
- **Projections/Perpendiculars**: Drop dotted lines (`densely dotted, thick, gray!70!black`) from key points/intersections to coordinate axes, labeling the values.
- **Contrast**: NEVER use faint grays like `gray!30` or `gray!40`. Use `gray!80!black` for axes and `gray!70!black` for projection lines.
- **Subfigures**: If multi-panel, use `subcaptionblock` (or `minipage`), NOT `subfigure`.
- **Do not compress layout**: 1-page fit optimization is strictly forbidden.

### Step 3: Mechanical Diff Verification (MANDATORY)
Immediately after saving the file, run the figure diff checker:

```bash
python3 scratch/check_figure_only_diff.py <path_to_tex_file>
```

- **If PASS**: Proceed to Step 4.
- **If FAIL**: You accidentally touched non-figure text!
  - Inspect the diff output reported by the tool.
  - Revert the accidental edits (e.g., reverted `subfiles` migration, restored `\[...\]`, restored original headings).
  - Re-run the checker until it outputs `PASS`.

### Step 4: Compile & Visual Verification
Verify rendering quality:
1. Compile the file (or a standalone test runner) with LuaLaTeX:
   ```bash
   lualatex --interaction=nonstopmode <test_file>.tex
   ```
2. Render pages to PNG and visually inspect:
   ```bash
   pdftoppm -png -r 150 <file>.pdf scratch/preview_page
   ```
3. Check for:
   - Label overlaps
   - Line clipping / bbox bounding issues
   - Visual clarity of hatched regions and contrast of axes

---

## What Counts as "Figure Block" vs "Non-Figure"

| Allowed to Edit (Figure Blocks) | FORBIDDEN to Edit (Non-Figure) |
|---|---|
| `\begin{figure} ... \end{figure}` | Documentclass / Preambles (`jarticle` $\to$ `subfiles`) |
| `\begin{zahyou} ... \end{zahyou}` | Framed problem statements (`\begin{oframed}`) |
| `\begin{center}\includegraphics...\end{center}` | Display math environments (`\[ ... \]` $\to$ `align`) |
| `% TODO: 概要図` (figure TODOs) | Headings (`{\bf [解]}` $\to$ `{\bf [解答]}`) |
| Directly adjacent `\vspace{...}` for the old figure | Cross-references (`\ref` $\to$ `\cref`) |
| | Surrounding text, words, punctuation, spaces |
