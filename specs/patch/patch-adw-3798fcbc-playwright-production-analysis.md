# Patch: Playwright Production Analysis for Filter Section Visual Parity

## Metadata
adw_id: `3798fcbc`
review_change_request: `Issue #2: The spec's step-by-step tasks (steps 3-10) require extensive Playwright usage to analyze production page structure, extract CSS styles, and perform multiple comparison cycles. None of these steps were executed because Playwright was unavailable. Without this analysis, the implementation may have incorrect color values, font sizes, spacing, border styles, or layout structure compared to production. Resolution: Follow the spec's step-by-step tasks 3-10: Analyze production filter section structure using browser_snapshot, extract computed CSS styles using browser_evaluate, document color palette/typography/spacing, and perform at least 2 refinement iteration cycles with side-by-side screenshot comparisons to achieve visual parity. Severity: blocker`

## Issue Summary
**Original Spec:** `specs/issue-1-adw-3798fcbc-sdlc_planner-search-filter-section-fixes.md`
**Issue:** The search filter section was implemented without executing the critical Playwright analysis steps (3-10) from the specification. The implementation was based on assumptions and best practices rather than actual production page analysis, resulting in potential visual discrepancies in colors, typography, spacing, borders, and layout compared to the production page at app.split.lease/search.
**Solution:** Execute the spec's steps 3-10 using Playwright browser automation to analyze the production filter section structure, extract computed CSS styles, document the exact design system (color palette, typography, spacing), and perform at least 2 refinement iteration cycles with side-by-side screenshot comparisons to achieve visual parity with production.

## Files to Modify
Use these files to implement the patch:

- `app/split-lease/pages/search/css/filters.css` - Update filter section styles to match production
- `app/split-lease/pages/search/css/search.css` - Update search page layout styles to match production
- `app/split-lease/pages/search/index.html` - Update HTML structure to match production
- `app/split-lease/pages/shared/css/common.css` - Update shared styles if needed for production alignment
- `.claude/commands/e2e/test_search_filter_alignment.md` - Update E2E test with specific production values

## Implementation Steps
IMPORTANT: Execute every step in order, top to bottom.

### Step 1: Setup and Initial Production Analysis
- Ensure local development server is running (`cd app/split-lease && python serve.py`)
- Use Playwright to navigate to production page: `app.split.lease/search`
- Capture `browser_snapshot` of production page to analyze accessibility tree and structure
- Take full-page screenshot of production page for reference
- Take focused screenshot of production filter section specifically
- Document current state and save screenshots to analysis directory

### Step 2: Extract Production Filter Section HTML Structure
- Use `browser_evaluate` to extract the exact HTML structure of the production filter section
- Document the filter section's:
  - HTML element hierarchy and nesting (div, section, aside, form structure)
  - CSS class names and IDs used in production
  - Data attributes or special attributes
  - Interactive element types (input types, button types, select dropdowns)
  - Form structure and field organization
  - Any JavaScript-injected elements or React component markers
- Save this structural analysis to a temporary reference document

### Step 3: Extract Production CSS Computed Styles
- Use `browser_evaluate` with `window.getComputedStyle()` to extract computed CSS for key filter elements:
  - Filter container (background, borders, padding, margins, box-shadow)
  - Section headings (font-family, font-size, font-weight, color, line-height)
  - Input fields (border, border-radius, padding, font-size, background, focus states)
  - Buttons (background, color, padding, border-radius, font-size, hover/active states)
  - Checkboxes and radio buttons (size, border, checked state colors)
  - Spacing between filter groups (margin-bottom, gap values)
- Document the exact color palette:
  - Primary colors (button backgrounds, accents, links)
  - Text colors (headings, body, labels, placeholders)
  - Border colors (inputs, dividers, containers)
  - Background colors (filter section, page, selected states)
- Save all extracted values to a styling reference document

### Step 4: First Refinement Iteration - Major Structural Updates
- Update `app/split-lease/pages/search/index.html` to match production HTML structure if significant differences found
- Update `app/split-lease/pages/search/css/filters.css` with extracted production values:
  - Color palette (replace assumed colors with production hex values)
  - Typography (font-family, sizes, weights, line-heights)
  - Spacing (padding, margins, gaps - match production exactly)
  - Border styles (widths, colors, border-radius values)
  - Layout approach (flexbox/grid properties to match production)
- Update `app/split-lease/pages/search/css/search.css` for overall page layout alignment
- Test changes locally and verify no JavaScript errors

### Step 5: First Visual Comparison Cycle
- Use Playwright to navigate to both local (`http://localhost:9212/search/`) and production (`app.split.lease/search`)
- Take side-by-side screenshots at the same viewport size (1280x720 or production default)
- Use `browser_snapshot` on both pages to compare accessibility trees
- Identify specific visual discrepancies:
  - Pixel-level spacing differences (use browser DevTools overlay comparison)
  - Font rendering differences (size, weight, letter-spacing)
  - Color value mismatches (extract actual hex values from both)
  - Border or shadow differences (thickness, blur, color, offset)
  - Element size/proportion differences (width, height, aspect ratios)
- Document all findings with annotated screenshots showing specific issues
- Prioritize issues by visual impact (high, medium, low)

### Step 6: Second Refinement Iteration - Fine-Tuning
- Address high and medium priority visual discrepancies from Step 5
- Fine-tune CSS values for exact pixel alignment:
  - Adjust spacing (1-2px precision for padding/margins)
  - Correct color values (use exact hex codes from production)
  - Refine typography (letter-spacing, line-height, font-smoothing)
  - Update interactive states (hover, focus, active, disabled)
  - Adjust box-shadows (match blur, spread, offset, color)
- Update `filters.css` with refined values
- Test all interactive elements (buttons, checkboxes, inputs) for state styling
- Verify no regressions in functionality

### Step 7: Second Visual Comparison Cycle
- Perform second Playwright comparison cycle with updated styles
- Take new side-by-side screenshots at same viewport size
- Identify remaining low-priority discrepancies or edge cases
- Verify that high-priority issues from Step 5 are resolved
- Document any remaining minor differences (< 2px variations)
- Capture final comparison screenshots showing visual parity achievement

### Step 8: Final Polish and Edge Cases
- Address any remaining minor visual differences
- Test and match edge cases:
  - Disabled states for buttons and inputs
  - Placeholder text styling in form inputs
  - Empty states or zero-value displays
  - Loading states if applicable
  - Error states for form validation
- Verify responsive behavior if production page has mobile/tablet breakpoints
- Ensure no unintended changes affected other page sections (header, footer, results area)

### Step 9: Update E2E Test with Production Values
- Update `.claude/commands/e2e/test_search_filter_alignment.md` with specific production values discovered
- Add assertions for exact color values, spacing, and typography
- Include screenshot comparison steps with specific element selectors
- Document expected computed style values for key elements
- Add validation steps for visual parity verification

### Step 10: Final Validation
- Execute the updated E2E test: Read `.claude/commands/test_e2e.md` then execute `.claude/commands/e2e/test_search_filter_alignment.md`
- Verify all test steps pass with visual parity achieved
- Review all captured screenshots for final confirmation
- Run structure validation: `cd app/split-lease && python validate_structure.py`
- Perform manual side-by-side browser comparison
- Document final results and any known minor limitations

## Validation
Execute every command to validate the patch is complete with zero regressions.

- Read `.claude/commands/test_e2e.md` then execute `.claude/commands/e2e/test_search_filter_alignment.md` - Validates visual alignment with production using Playwright screenshots and comparisons
- `cd app/split-lease && python validate_structure.py` - Validates HTML structure integrity maintained
- Manual validation: Open `http://localhost:9212/search/` and `app.split.lease/search` side-by-side in browser, compare filter sections pixel-by-pixel at 1280x720 viewport
- Screenshot review: Verify all captured comparison screenshots show visual parity (< 2px variance acceptable)
- Interactive testing: Test all filter interactions (clicks, hovers, form inputs) match production behavior

## Patch Scope
**Lines of code to change:** 150-250 (primarily CSS value updates, minor HTML structure adjustments)
**Risk level:** medium (CSS changes only, no breaking functionality changes, thorough testing required)
**Testing required:** Playwright E2E visual comparison test with side-by-side screenshots, manual visual inspection, structure validation, interactive element testing across all filter components
