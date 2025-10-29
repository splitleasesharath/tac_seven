# Bug: Search Page Filter Section Fixes

## Metadata
issue_number: `1`
adw_id: `71833aa9`
issue_json: `{"number":1,"title":"Search page filter section fixes","body":"adw_plan\n\n/bug\n\nI need the filter section(and only work on the filter section) to look more in line with my actual original page at app.split.lease/search. Use playwright to run multiple cycles switching between the preview of the current search page and the original, and build out the functionality of the current page, to be visually more in line with the original."}`

## Bug Description
The search page filter section in the local development version does not match the visual design and functionality of the production version at app.split.lease/search. The filter section needs to be updated to align with the original design in terms of layout, styling, filter options, and interactive behavior.

Currently, the local codebase appears to be in early stages with no client-side implementation present (only `app/server/` exists). The Islands Architecture described in the README.md needs to be implemented for the search page, specifically focusing on the filter section component.

## Problem Statement
The filter section on the local search page preview does not visually match the production site at app.split.lease/search. Users expect a consistent experience between development and production versions. The filter section is a critical component for property search functionality and must match the original design precisely.

## Solution Statement
Implement and/or update the search page filter section using the Islands Architecture pattern described in the README. Use Playwright browser automation to iteratively compare the local preview with the production site at app.split.lease/search, making incremental changes until the filter section achieves visual parity. Focus exclusively on the filter section without modifying other parts of the search page.

## Steps to Reproduce
1. Navigate to the production site: https://app.split.lease/search
2. Observe the filter section layout, styling, and available filters
3. Navigate to the local development preview (when implemented): http://localhost:9206/search
4. Compare the filter sections between production and local
5. Note the visual and functional differences

## Root Cause Analysis
The root cause is likely one or more of the following:
1. **Missing Implementation**: The search page filter section has not been implemented yet in the local codebase (app/client or app/split-lease structure doesn't exist)
2. **Incomplete Migration**: If partially implemented, the filter section may be missing key components, styles, or functionality present in production
3. **Styling Discrepancies**: CSS styles may not match the production version in terms of colors, spacing, typography, or layout
4. **Component Structure**: The React component structure may differ from what's needed to match the production design

## Relevant Files
Use these files to fix the bug:

### Existing Files to Reference
- `README.md` - Contains project structure documentation for Islands Architecture implementation
- `.claude/commands/conditional_docs.md` - Conditional documentation for understanding when to read additional docs
- `.ports.env` - Port configuration (FRONTEND_PORT=9206, BACKEND_PORT=9106)
- `scripts/start.sh` - Script to start both frontend and backend servers
- `.claude/commands/test_e2e.md` - E2E test runner documentation for Playwright-based testing
- `.claude/commands/e2e/test_basic_query.md` - Example E2E test structure to follow

### New Files to Create
- `app/split-lease/pages/search/index.html` - Search page HTML with filter section
- `app/split-lease/pages/search/css/search.css` - Search page specific styles
- `app/split-lease/pages/search/css/filters.css` - Filter section styles
- `app/split-lease/pages/search/js/filters.js` - Filter section JavaScript (if needed for non-React interactions)
- `app/split-lease/components/src/SearchFilters/SearchFilters.tsx` - React component for filter section
- `app/split-lease/components/src/SearchFilters/SearchFilters.styles.ts` - Styled components for filters
- `app/split-lease/components/src/SearchFilters/types.ts` - TypeScript types for filter props
- `app/split-lease/components/src/SearchFilters/index.ts` - Export file for SearchFilters component
- `.claude/commands/e2e/test_search_filters.md` - E2E test for validating filter section matches original

## Step by Step Tasks
IMPORTANT: Execute every step in order, top to bottom.

### 1. Set Up Playwright for Visual Comparison
- Install and configure Playwright browser automation if not already set up
- Create a comparison script that can:
  - Navigate to production: https://app.split.lease/search
  - Take screenshots of the filter section
  - Navigate to local preview: http://localhost:9206/search (once implemented)
  - Take screenshots of the local filter section
  - Provide side-by-side visual comparison

### 2. Document Production Filter Section Requirements
- Use Playwright to inspect production site at app.split.lease/search
- Document all filter options present (e.g., location, price range, dates, number of bedrooms, amenities, etc.)
- Capture screenshots of:
  - Filter section in collapsed/default state
  - Filter section with filters expanded
  - Individual filter controls (dropdowns, sliders, checkboxes, etc.)
  - Filter section on mobile responsive view
- Document styling details:
  - Colors (backgrounds, text, borders, active states)
  - Typography (font families, sizes, weights)
  - Spacing (margins, padding, gaps)
  - Layout (flexbox/grid structure, positioning)
  - Interactive states (hover, focus, active, disabled)

### 3. Create Islands Architecture Foundation (if needed)
- Verify if `app/split-lease/` directory structure exists
- If not, create the directory structure per README:
  - `app/split-lease/components/` - React components library
  - `app/split-lease/pages/` - Static HTML pages
  - `app/split-lease/pages/search/` - Search page directory
- Set up component library:
  - Create `app/split-lease/components/package.json` with dependencies (React, TypeScript, Styled Components, Framer Motion, Vite)
  - Create `app/split-lease/components/vite.config.ts` for UMD bundle build
  - Create `app/split-lease/components/tsconfig.json` for TypeScript configuration
  - Run `npm install` in components directory

### 4. Implement SearchFilters React Component
- Create `app/split-lease/components/src/SearchFilters/` directory
- Implement `SearchFilters.tsx` with all filter options identified from production
- Implement `SearchFilters.styles.ts` using styled-components to match production styling exactly
- Define `types.ts` with TypeScript interfaces for filter props and state
- Create `index.ts` to export the component
- Update `app/split-lease/components/src/index.ts` to export SearchFilters
- Build the component library: `npm run build` in components directory

### 5. Create Search Page HTML
- Create `app/split-lease/pages/search/index.html` following Islands Architecture pattern
- Include React CDN scripts
- Include the UMD components bundle
- Create a mount point for the SearchFilters island: `<div id="search-filters"></div>`
- Add initialization script to mount SearchFilters component
- Ensure the page can be served and viewed in a browser

### 6. Implement Filter Section Styling
- Create `app/split-lease/pages/search/css/filters.css` for additional static styles
- Match all styling from production:
  - Layout and positioning
  - Colors and backgrounds
  - Typography
  - Spacing and dimensions
  - Borders and shadows
  - Responsive breakpoints
- Link the CSS file in the search page HTML

### 7. Iterative Visual Comparison and Refinement
- Start the local development server (or open HTML file directly)
- Use Playwright to automate comparison cycles:
  - Cycle 1: Compare overall filter section layout
  - Cycle 2: Compare individual filter controls
  - Cycle 3: Compare spacing and typography
  - Cycle 4: Compare colors and visual styling
  - Cycle 5: Compare interactive states (hover, focus, etc.)
  - Cycle 6: Compare responsive behavior at different screen sizes
- After each cycle:
  - Document differences found
  - Make necessary code changes to match production
  - Rebuild component library if React components changed
  - Refresh preview and repeat comparison

### 8. Implement Filter Functionality
- Add state management for filter values
- Implement filter change handlers
- Add validation for filter inputs
- Ensure filters work independently and in combination
- Test edge cases (clearing filters, invalid inputs, etc.)

### 9. Final Visual Validation
- Use Playwright to perform final side-by-side comparison
- Verify pixel-perfect alignment where appropriate
- Check all filter interactions work as expected
- Validate responsive behavior on multiple screen sizes
- Ensure no console errors or warnings

### 10. Create E2E Test for Filter Section
- Read `.claude/commands/e2e/test_basic_query.md` and `.claude/commands/test_e2e.md` to understand E2E test structure
- Create `.claude/commands/e2e/test_search_filters.md` that:
  - Validates all filter controls are present
  - Tests filter interactions (selecting options, entering values)
  - Verifies visual match with production (screenshot comparison)
  - Tests responsive behavior
  - Validates no JavaScript errors occur
- Include specific verification steps:
  - Screenshot of filter section in default state matches production
  - Screenshot of filter section with filters applied matches production
  - All filter controls are functional and styled correctly

### 11. Run Validation Commands
- Execute all commands in the Validation Commands section to ensure zero regressions
- Fix any issues that arise
- Re-run validation until all tests pass

## Validation Commands
Execute every command to validate the bug is fixed with zero regressions.

### Manual Comparison
- Navigate to https://app.split.lease/search and http://localhost:9206/search side-by-side
- Verify filter section layouts match visually
- Test all filter interactions work identically
- Check responsive behavior at breakpoints: 320px, 768px, 1024px, 1440px

### Automated E2E Validation
- Read `.claude/commands/test_e2e.md` to understand how to run E2E tests
- Execute the new E2E test: Read and run `.claude/commands/e2e/test_search_filters.md`
- Verify all E2E test steps pass with zero failures
- Review screenshots captured during E2E test to confirm visual match

### Component Build Validation
- `cd app/split-lease/components && npm run typecheck` - Verify TypeScript types are correct
- `cd app/split-lease/components && npm run build` - Verify component library builds without errors
- Verify UMD bundle is generated: `ls -la app/split-lease/components/dist/split-lease-components.umd.cjs`

### Integration Validation
- Open `app/split-lease/pages/search/index.html` in browser
- Open browser console and verify:
  - No JavaScript errors
  - No React warnings
  - `window.SplitLeaseComponents.SearchFilters` is defined
  - Component renders successfully

### Visual Regression Check
- Use Playwright to capture screenshots of:
  - Production filter section: https://app.split.lease/search
  - Local filter section: http://localhost:9206/search (or file:// URL)
- Perform visual diff to ensure <5% difference in visual appearance
- Document any intentional differences (if any)

## Notes

### Important Constraints
- **Only work on the filter section** - Do not modify other parts of the search page (results grid, map, header, footer, etc.)
- Use the Islands Architecture pattern as described in README.md
- Follow the existing project structure and conventions
- Maintain compatibility with React 18 and ES2020 browsers

### Technical Considerations
- The production site is at app.split.lease, while local development uses localhost with ports defined in `.ports.env`
- Use styled-components for component styling to match the README architecture
- Ensure the component is exported via UMD bundle and accessible as `window.SplitLeaseComponents.SearchFilters`
- Consider using Framer Motion for any animations if present in production

### Playwright Automation Strategy
- Use Playwright to automate the comparison process
- Take screenshots programmatically for before/after comparison
- Consider using Playwright's visual regression testing features
- Document all differences found during each comparison cycle

### Potential Challenges
- Production site may require authentication or have dynamic content
- Some styling may be dependent on global styles or parent containers
- Filter data sources (e.g., available locations, price ranges) may need to be mocked initially
- Responsive behavior may require testing at multiple viewport sizes

### Performance Considerations
- Keep the UMD bundle size minimal
- Use code splitting if the filter section becomes too large
- Optimize images and assets used in the filter section
- Ensure fast load times for the React island

### Accessibility
- Ensure all filter controls are keyboard accessible
- Add proper ARIA labels and roles
- Maintain focus management for interactive elements
- Test with screen readers if production site does so

### Browser Compatibility
- Test in modern browsers (Chrome, Firefox, Safari, Edge)
- Ensure ES2020 features are supported
- Verify React 18 CDN loads correctly
- Check for any polyfills needed
