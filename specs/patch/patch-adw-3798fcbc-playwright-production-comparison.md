# Patch: Production Visual Alignment via Playwright Comparison

## Metadata
adw_id: `3798fcbc`
review_change_request: `Issue #1: The spec explicitly requires using Playwright to compare the local implementation with the production page at app.split.lease/search through multiple iterative cycles. The implementation was built without access to Playwright or the production page, making it impossible to verify that the visual design (colors, typography, spacing, layout, component styling) matches the production page. The implementer acknowledged this limitation in IMPLEMENTATION_SUMMARY.md: 'Due to technical constraints (Playwright MCP not available, production DOM not accessible via WebFetch), I implemented a comprehensive, production-quality search page filter section based on modern web design best practices and typical rental search platform patterns.' This violates the core requirement of the bug fix. Resolution: 1. Enable Playwright MCP browser automation. 2. Navigate to production page at app.split.lease/search and capture detailed screenshots and DOM structure. 3. Compare local implementation with production and identify all visual differences (colors, fonts, spacing, borders, shadows, layouts). 4. Iteratively adjust the local CSS and HTML to match production exactly. 5. Re-run the E2E test with actual production comparison screenshots. Severity: blocker`

## Issue Summary
**Original Spec:** specs/issue-1-adw-3798fcbc-sdlc_planner-search-filter-section-fixes.md
**Issue:** The search page filter section was implemented without using Playwright to compare against the production page at app.split.lease/search. The spec explicitly requires iterative visual comparison cycles using Playwright browser automation to ensure pixel-perfect alignment with production, but the implementation was built from scratch based on best practices rather than production reference.
**Solution:** Use Playwright MCP tools to navigate to app.split.lease/search, capture production page structure and styling, compare with local implementation, and iteratively adjust HTML/CSS to match production exactly through multiple refinement cycles.

## Files to Modify
Use these files to implement the patch:

- `app/split-lease/pages/search/index.html` - Update HTML structure to match production DOM
- `app/split-lease/pages/search/css/filters.css` - Update filter section styles to match production styling
- `app/split-lease/pages/search/css/search.css` - Update search page layout to match production
- `app/split-lease/pages/shared/css/common.css` - Update common styles if needed for production alignment
- `.claude/commands/e2e/test_search_filter_alignment.md` - Update E2E test to include actual production comparison screenshots

## Implementation Steps
IMPORTANT: Execute every step in order, top to bottom.

### Step 1: Start local development server and capture baseline
- Navigate to app/split-lease directory and start the development server: `cd app/split-lease && python serve.py`
- Use Playwright `browser_navigate` to open http://localhost:9212/search/
- Use Playwright `browser_snapshot` to capture accessibility tree of local filter section
- Use Playwright `browser_take_screenshot` to capture full-page screenshot (filename: "local-search-baseline.png")
- Use Playwright `browser_take_screenshot` with fullPage=false to capture filter section only (filename: "local-filter-section-baseline.png")

### Step 2: Navigate to production and extract structure/styling
- Use Playwright `browser_navigate` to open https://app.split.lease/search
- Use Playwright `browser_snapshot` to capture accessibility tree of production filter section
- Use Playwright `browser_take_screenshot` to capture full-page screenshot (filename: "production-search-reference.png")
- Use Playwright `browser_take_screenshot` with fullPage=false to capture filter section only (filename: "production-filter-section-reference.png")
- Use Playwright `browser_evaluate` to extract HTML structure of filter section: `() => document.querySelector('.filter-section')?.outerHTML || document.querySelector('[class*="filter"]')?.outerHTML`
- Use Playwright `browser_evaluate` to extract computed CSS styles for key elements: `() => { const elem = document.querySelector('.filter-section'); return window.getComputedStyle(elem); }`
- Document production color palette, typography (font-family, sizes, weights), spacing values, borders, shadows, and layout approach

### Step 3: Compare and identify visual differences
- Review captured screenshots side-by-side (local vs production)
- Identify specific differences in:
  - HTML element hierarchy and class naming
  - Color palette (backgrounds, borders, text colors, accent colors)
  - Typography (font families, sizes, weights, line-heights)
  - Spacing (padding, margins, gaps)
  - Border styles (widths, colors, radius values)
  - Layout structure (flexbox vs grid, positioning)
  - Interactive element styling (buttons, inputs, checkboxes)
  - Shadow effects and transitions
- Create prioritized list of changes needed to match production

### Step 4: First iteration - Update HTML structure and major styles
- Update `app/split-lease/pages/search/index.html` to match production HTML structure (element hierarchy, class names, semantic elements)
- Update `app/split-lease/pages/search/css/filters.css` with production color palette values
- Update typography settings to match production (font-family, sizes, weights)
- Update layout approach to match production (flexbox/grid, positioning)
- Update spacing values (padding, margins) to match production measurements
- Use Playwright `browser_navigate` to reload local page and capture new screenshot (filename: "local-filter-iteration-1.png")
- Compare iteration-1 screenshot with production reference to validate improvements

### Step 5: Second iteration - Fine-tune borders, shadows, and interactive states
- Adjust border styles (widths, colors, radius) to match production exactly
- Add or update box-shadow values to match production
- Update button and input styles to match production interactive elements
- Refine checkbox and radio button styling
- Update hover, focus, and active states to match production behavior
- Add transitions/animations if observed in production
- Use Playwright `browser_navigate` to reload local page and capture new screenshot (filename: "local-filter-iteration-2.png")
- Compare iteration-2 screenshot with production reference

### Step 6: Final iteration - Pixel-perfect refinement
- Address any remaining 1-2px spacing differences
- Fine-tune subtle color variations using exact hex/rgb values from production
- Adjust font rendering (font-smoothing, letter-spacing) if needed
- Verify disabled states and placeholder text styling match production
- Check icon styling and positioning if present
- Validate responsive behavior matches production
- Use Playwright `browser_navigate` to reload local page and capture final screenshot (filename: "local-filter-final.png")
- Perform final side-by-side comparison with production

### Step 7: Update E2E test and validate
- Update `.claude/commands/e2e/test_search_filter_alignment.md` to reference actual production comparison screenshots taken during this patch
- Execute the E2E test following `.claude/commands/test_e2e.md` instructions
- Verify test passes with actual visual parity between local and production
- Document any remaining known differences or limitations

## Validation
Execute every command to validate the patch is complete with zero regressions.

1. **Start development server:**
   ```bash
   cd app/split-lease && python serve.py
   ```

2. **Run HTML structure validation:**
   ```bash
   cd app/split-lease && python validate_structure.py
   ```

3. **Execute E2E test specification:**
   Read `.claude/commands/test_e2e.md`, then read and execute `.claude/commands/e2e/test_search_filter_alignment.md`

4. **Manual visual comparison:**
   - Open http://localhost:9212/search/ and https://app.split.lease/search side-by-side
   - Compare filter sections pixel-by-pixel
   - Test all interactive elements (clicks, hovers, form inputs)
   - Verify responsive behavior at different viewport sizes

5. **Screenshot verification:**
   - Review all captured screenshots to confirm visual alignment
   - Verify progression from baseline → iteration-1 → iteration-2 → final shows improvements
   - Confirm final screenshot closely matches production reference

6. **Run full test suite (if applicable):**
   ```bash
   cd app/server && uv run pytest tests/ -v --tb=short
   cd app/client && bun tsc --noEmit
   cd app/client && bun run build
   ```

## Patch Scope
**Lines of code to change:** ~50-100 lines (primarily CSS updates in filters.css and search.css, minor HTML structure adjustments)
**Risk level:** Low (isolated to filter section styling, no backend or core functionality changes)
**Testing required:** Playwright-based visual comparison, E2E test execution, manual side-by-side verification, structure validation script
