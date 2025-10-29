# Bug: Search Page Filter Section Visual Alignment

## Metadata
issue_number: `1`
adw_id: `3798fcbc`
issue_json: `{"number":1,"title":"Search page filter section fixes","body":"adw_plan\n\n/bug\n\nI need the filter section(and only work on the filter section) to look more in line with my actual original page at app.split.lease/search. Use playwright to run multiple cycles switching between the preview of the current search page and the original, and build out the functionality of the current page, to be visually more in line with the original."}`

## Bug Description
The search page filter section does not visually align with the original production page at app.split.lease/search. The current implementation's filter section styling, layout, spacing, colors, typography, and interactive elements differ from the production version, creating an inconsistent user experience. The filter section needs to be updated to match the visual design and functionality of the original page.

## Problem Statement
The filter section on the search page (currently being developed) has visual and functional inconsistencies compared to the live production page at app.split.lease/search. This creates a poor user experience as the styling, layout, component arrangement, and interactive behavior do not match user expectations set by the original page.

## Solution Statement
Use Playwright browser automation to systematically compare the current search page filter section with the production version at app.split.lease/search. Through iterative cycles of visual comparison and code updates, modify the HTML, CSS, and React components to achieve visual parity with the original filter section. The solution will focus exclusively on the filter section without modifying other page areas.

## Steps to Reproduce
1. Navigate to the local development version of the search page (http://localhost:9212/search or equivalent)
2. Navigate to the production version at app.split.lease/search in a separate tab
3. Compare the filter section visually between both pages
4. Observe differences in:
   - Layout and spacing
   - Typography (font sizes, weights, colors)
   - Component arrangement
   - Border styles and colors
   - Background colors
   - Interactive element styling (buttons, dropdowns, checkboxes)
   - Responsive behavior
   - Padding and margins
5. Note that the filter section in the current implementation does not match the original

## Root Cause Analysis
The root cause of this bug is that the filter section was developed without direct visual reference to the production page, or the design specifications have diverged from the original implementation. The HTML structure, CSS styling, and component props may have been built from scratch or with incomplete design references, leading to visual inconsistencies in:

- CSS class names and styling rules not matching the original
- Different spacing/padding/margin values
- Mismatched color schemes or typography
- Different component structure or HTML hierarchy
- Missing or incorrectly implemented interactive states (hover, focus, active)

## Relevant Files
Use these files to fix the bug:

### Core Application Files
- `README.md` - Project overview, architecture pattern (Islands Architecture), and structure documentation
- `.ports.env` - Port configuration for local development (FRONTEND_PORT=9212)
- `playwright-mcp-config.json` - Playwright configuration for browser automation

### Search Page Implementation
- `app/split-lease/pages/search/index.html` - Main search page HTML structure with filter section markup
- `app/split-lease/pages/search/css/search.css` - Search page specific CSS including filter section styles
- `app/split-lease/pages/search/css/filters.css` - Dedicated filter section CSS (if exists)
- `app/split-lease/pages/shared/css/common.css` - Shared CSS that may affect filter styling

### React Components (if filter uses React islands)
- `app/split-lease/components/src/SearchFilters/` - React component for search filters (if exists)
- `app/split-lease/components/src/SearchFilters/SearchFilters.tsx` - Main filter component
- `app/split-lease/components/src/SearchFilters/SearchFilters.styles.ts` - Styled-components for filters
- `app/split-lease/components/dist/split-lease-components.umd.cjs` - UMD bundle (rebuilt after changes)

### Testing Files
- `.claude/commands/test_e2e.md` - E2E test runner documentation
- `.claude/commands/e2e/test_basic_query.md` - Example E2E test structure

### Documentation
- `.claude/commands/conditional_docs.md` - Conditional documentation guide

### New Files
- `.claude/commands/e2e/test_search_filter_alignment.md` - New E2E test to validate filter section visual alignment with production

## Step by Step Tasks
IMPORTANT: Execute every step in order, top to bottom.

### 1. Setup and Reconnaissance
- Ensure the development environment is running with correct ports (FRONTEND_PORT=9212 per .ports.env)
- Verify local search page is accessible at http://localhost:9212/search (or appropriate path)
- Use Playwright to navigate to both local and production (app.split.lease/search) pages
- Take full-page screenshots of both pages for initial comparison
- Take focused screenshots of the filter sections on both pages
- Document the current state and major visual differences observed

### 2. Create Development Search Page Structure (if not exists)
- If `app/split-lease/pages/search/index.html` does not exist, create the basic page structure following the Islands Architecture pattern
- Include proper HTML5 document structure with meta tags
- Add React CDN scripts (React 18 production UMD)
- Include placeholder filter section HTML structure
- Create basic CSS file structure in `app/split-lease/pages/search/css/`
- Ensure the page is accessible via the development server

### 3. Analyze Production Filter Section Structure
- Use Playwright's `browser_snapshot` to capture the accessibility tree of the production filter section
- Use Playwright's `browser_evaluate` to extract HTML structure of the filter section
- Document the filter section's:
  - HTML element hierarchy and structure
  - CSS class names and IDs used
  - Data attributes or special attributes
  - Interactive element types (buttons, select dropdowns, checkboxes, radio buttons, range sliders)
  - Form structure and input field types
- Save this analysis to a temporary reference document for implementation

### 4. Analyze Production Filter Section Styling
- Use Playwright to inspect computed CSS styles for key filter elements on production
- Extract and document:
  - Color palette (backgrounds, borders, text colors, accent colors)
  - Typography (font families, sizes, weights, line heights)
  - Spacing (padding, margins, gaps between elements)
  - Border styles (widths, colors, radius values)
  - Layout approach (flexbox, grid, positioning)
  - Shadow effects (box-shadow values)
  - Transition/animation properties
- Take annotated screenshots highlighting key styling attributes
- Create a styling reference guide from the extracted values

### 5. Implement Filter Section HTML Structure
- Update `app/split-lease/pages/search/index.html` to match the production HTML structure
- Replicate the exact element hierarchy and nesting observed in production
- Use the same or equivalent HTML5 semantic elements
- Apply matching class names and IDs
- Include all necessary form elements (inputs, selects, buttons)
- Add placeholder content that matches the production page
- Ensure accessibility attributes are preserved (aria-labels, roles, etc.)

### 6. Implement Filter Section CSS Styling
- Create or update `app/split-lease/pages/search/css/filters.css` with styles matching production
- Apply the extracted color palette, typography, and spacing values
- Implement layout rules (flexbox/grid) to match element positioning
- Add border styles, shadows, and visual effects as observed in production
- Include responsive design rules if observed in production
- Implement interactive states (hover, focus, active) for buttons and inputs
- Add transitions for smooth interactions matching production behavior

### 7. First Visual Comparison Cycle
- Use Playwright to take side-by-side screenshots of local and production filter sections
- Identify remaining visual discrepancies:
  - Pixel-level spacing differences
  - Font rendering differences
  - Color value mismatches
  - Border or shadow differences
  - Element size or proportion differences
- Document specific issues found with screenshot annotations
- Prioritize issues by visual impact

### 8. Refinement Iteration 1
- Address the highest priority visual discrepancies identified in step 7
- Fine-tune CSS values for spacing, sizing, and positioning
- Adjust color values to exact matches (use color picker tools)
- Refine typography settings (font-smoothing, letter-spacing, etc.)
- Update any HTML structure issues identified
- Test interactive element states and adjust styling
- Take new comparison screenshots to validate changes

### 9. Refinement Iteration 2
- Perform second visual comparison cycle using Playwright
- Identify any remaining medium-priority discrepancies
- Address layout alignment issues
- Fine-tune responsive behavior if applicable
- Adjust z-index or stacking context issues if present
- Validate form element styling (inputs, dropdowns, checkboxes)
- Take comparison screenshots to validate improvements

### 10. Final Polish and Edge Cases
- Perform final detailed visual comparison
- Address any minor remaining differences (1-2px variations, subtle color differences)
- Test and match disabled states for interactive elements
- Verify placeholder text styling in form inputs
- Check icon styling and positioning if present
- Ensure loading states match (if applicable)
- Validate that no unintended changes affected other page sections

### 11. Create E2E Test for Filter Section Alignment
- Read `.claude/commands/e2e/test_basic_query.md` and `.claude/commands/e2e/test_complex_query.md` to understand E2E test structure
- Create new E2E test file: `.claude/commands/e2e/test_search_filter_alignment.md`
- Include test steps that:
  - Navigate to local search page
  - Take screenshot of filter section
  - Navigate to production page (app.split.lease/search)
  - Take screenshot of production filter section
  - Verify key visual elements are present in local version
  - Verify filter section is visible and properly styled
  - Test basic filter interactions (clicks, selections)
  - Capture final state screenshots
- Define success criteria including visual parity validation
- Specify minimum 4 screenshots: initial local state, initial production state, local filter detail, production filter detail

### 12. Run Validation Commands
- Execute all validation commands listed below to ensure the bug is fixed with zero regressions
- Verify all tests pass without errors
- Review all screenshots for visual confirmation
- Document any remaining known issues or limitations

## Validation Commands
Execute every command to validate the bug is fixed with zero regressions.

- Read `.claude/commands/test_e2e.md`, then read and execute the new `.claude/commands/e2e/test_search_filter_alignment.md` E2E test file to validate the filter section visually matches the production page
- `cd app/server && uv run pytest` - Run server tests to validate the bug is fixed with zero regressions (if server tests exist)
- `cd app/split-lease/components && npm run typecheck` - Verify TypeScript types if React components were modified
- `cd app/split-lease/components && npm run build` - Rebuild component UMD bundle if React components were modified
- Manual validation: Open local search page and production page side-by-side in browser, compare filter sections pixel-by-pixel
- Manual validation: Test all interactive elements in the filter section (clicks, hovers, form inputs) to ensure they function correctly
- Screenshot comparison: Review all captured screenshots to confirm visual alignment is achieved

## Notes
- **Focus exclusively on the filter section** - Do not modify other parts of the search page (header, footer, results section, map preview, etc.)
- **Use Playwright extensively** - Leverage browser automation for systematic visual comparison and testing
- **Iterative approach** - Multiple comparison cycles are expected to achieve pixel-perfect alignment
- **Production reference** - The production page at app.split.lease/search is the source of truth for all visual decisions
- **Islands Architecture** - If the filter section uses React components, follow the Islands Architecture pattern (static HTML enhanced with React islands)
- **Screenshot documentation** - All comparison screenshots should be saved in the E2E test screenshot directory structure
- **Responsive considerations** - If the production page has responsive behavior in the filter section, replicate it in the local version
- **Browser consistency** - Use the same browser (Chromium via Playwright per config) for all comparisons to ensure consistent rendering
- **CSS methodology** - Prefer vanilla CSS or styled-components based on existing project patterns
- **No new libraries** - Use existing dependencies; if a new library is absolutely required for visual parity, document it clearly in the plan resolution notes
- **Accessibility** - Maintain or improve accessibility attributes and ARIA labels during implementation
- **Performance** - Ensure CSS changes do not negatively impact page load performance
