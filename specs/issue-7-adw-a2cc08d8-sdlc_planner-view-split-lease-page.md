# Feature: Create View Split Lease Page

## Metadata
issue_number: `7`
adw_id: `a2cc08d8`
issue_json: `{"number":7,"title":"Create a new page called view-split-lease","body":"adw_plan_build_iso\n\nThe view split lease page is for showcasing listings on our marketplaces by hosts for guests. Start with a plain page. No elements."}`

## Feature Description
Create a new static HTML page called "view-split-lease" that will serve as the listing detail page for showcasing individual rental properties on the Split Lease marketplace. This page will allow guests to view detailed information about a specific listing posted by a host. The initial implementation will be a plain, foundational page with minimal structure - establishing the basic HTML layout, navigation, and styling patterns consistent with the existing Split Lease pages (home and search).

## User Story
As a guest browsing Split Lease
I want to view detailed information about a specific rental listing
So that I can evaluate the property and decide if it meets my periodic tenancy needs

## Problem Statement
Currently, the Split Lease application has a home page and search page, but there is no dedicated page for viewing individual listing details. When users want to learn more about a specific property from search results or listing previews, there is no destination page to present comprehensive information about that listing. This gap prevents guests from making informed decisions about rentals and limits hosts' ability to showcase their properties effectively.

## Solution Statement
Create a new static HTML page at `app/split-lease/pages/view-split-lease/index.html` following the Islands Architecture pattern established in the codebase. The page will include the standard header and footer React islands, basic HTML structure, and CSS styling consistent with existing pages. This foundational page will serve as the base upon which future enhancements (property images, amenities, booking components, etc.) can be built. The initial implementation focuses on establishing the proper page structure, navigation integration, and responsive layout.

## Relevant Files
Use these files to implement the feature:

- **app/split-lease/pages/index.html** - Reference for Islands Architecture pattern, React CDN setup, header/footer mounting, and overall page structure
- **app/split-lease/pages/search/index.html** - Reference for page layout patterns, CSS structure, and responsive design
- **app/split-lease/pages/home/css/home.css** - Reference for CSS variables, color scheme, and styling conventions (particularly the primary purple color `#31135D`, spacing, and typography)
- **app/split-lease/pages/search/css/styles.css** - Reference for minimal styling approach and layout patterns
- **app/split-lease/pages/shared/js/header.js** - Existing header mounting script that should be reused
- **app/split-lease/pages/shared/js/footer.js** - Existing footer mounting script that should be reused
- **app/split-lease/components/dist/split-lease-components.umd.cjs** - UMD bundle containing Header and Footer components to be mounted as islands
- **app/split-lease/components/dist/style.css** - Component styles to be included in the page
- **README.md** - Project documentation explaining Islands Architecture pattern and development workflow
- **.claude/commands/test_e2e.md** - Instructions for running E2E tests with Playwright
- **.claude/commands/conditional_docs.md** - Guide for determining what documentation to read based on task requirements

### New Files

- **app/split-lease/pages/view-split-lease/index.html** - Main HTML page for viewing individual listings
- **app/split-lease/pages/view-split-lease/css/styles.css** - Page-specific styles following existing conventions
- **app/split-lease/pages/view-split-lease/css/responsive.css** - Responsive layout styles for mobile/tablet/desktop views
- **.claude/commands/e2e/test_view_split_lease_page.md** - E2E test specification to validate the new page works correctly

## Implementation Plan

### Phase 1: Foundation
Establish the basic page structure by creating the HTML file with proper meta tags, document structure, and CDN references. Set up the Islands Architecture pattern by including React CDN scripts and the Split Lease components UMD bundle. Create the mounting points for Header and Footer React islands. Reference existing pages (index.html and search/index.html) to ensure consistency in structure and approach.

### Phase 2: Core Implementation
Implement the minimal page content including header island mount point, main content area with placeholder structure, and footer island mount point. Create the CSS files (styles.css and responsive.css) following the existing color scheme, typography, and layout patterns from home.css and search/css/styles.css. Ensure proper CSS variable usage for consistency across the application. Add scripts to mount the Header and Footer components using the existing shared JavaScript files.

### Phase 3: Integration
Integrate the new page with the existing navigation structure. Verify that the page properly loads all React components from the UMD bundle. Test responsive behavior across mobile, tablet, and desktop viewports. Ensure the page is accessible via the correct URL path and can be navigated to from other pages in the application. Validate that all styling is consistent with the existing Split Lease brand and design system.

## Step by Step Tasks

### 1. Create the view-split-lease page directory structure
- Create directory `app/split-lease/pages/view-split-lease/`
- Create subdirectories `css/` for styles
- Create subdirectory `js/` for page-specific JavaScript (if needed in future)

### 2. Create the main HTML page (index.html)
- Create `app/split-lease/pages/view-split-lease/index.html`
- Add proper DOCTYPE, html, head, and body structure
- Include meta tags for charset, viewport, description, and SEO (following index.html pattern)
- Add title: "View Listing | Split Lease"
- Link to component styles: `../../components/dist/style.css`
- Link to page-specific styles: `css/styles.css` and `css/responsive.css`
- Include React 18 UMD scripts from CDN (react.production.min.js and react-dom.production.min.js)
- Add the Node globals shim for UMD compatibility (process.env)
- Include the Split Lease components UMD bundle: `../../components/dist/split-lease-components.umd.cjs`

### 3. Add React island mount points and structure
- Add header mount point: `<div id="site-header"></div>`
- Create main content area with semantic HTML: `<main class="view-listing-main">`
- Add placeholder content structure in main (simple heading and container for future content)
- Add footer mount point: `<div id="site-footer"></div>`

### 4. Mount Header and Footer React islands
- Include header mounting script: `<script src="../shared/js/header.js"></script>`
- Include footer mounting script: `<script src="../shared/js/footer.js"></script>`
- Verify scripts are loaded after the UMD bundle and mount points are defined

### 5. Create the main styles CSS file
- Create `app/split-lease/pages/view-split-lease/css/styles.css`
- Define CSS variables following home.css pattern (--primary-color: #31135D, etc.)
- Style the html and body elements (font-family: Inter, colors, margins)
- Style the .view-listing-main container (max-width: 1280px, padding, margins)
- Add basic typography styles for headings and paragraphs
- Ensure consistent spacing and layout with other pages

### 6. Create responsive styles CSS file
- Create `app/split-lease/pages/view-split-lease/css/responsive.css`
- Add mobile-first media queries (min-width breakpoints: 768px, 1024px, 1280px)
- Define responsive padding, font sizes, and layout adjustments
- Ensure the page looks good on mobile, tablet, and desktop viewports
- Reference search/css/responsive.css for patterns

### 7. Create E2E test specification
- Create `.claude/commands/e2e/test_view_split_lease_page.md`
- Define user story: validating that the view-split-lease page loads correctly with header and footer islands
- List test steps:
  1. Navigate to http://localhost:8080/view-split-lease/index.html
  2. Verify page title is "View Listing | Split Lease"
  3. Verify header React island mounts successfully (check for #site-header content)
  4. Verify footer React island mounts successfully (check for #site-footer content)
  5. Verify main content area is visible
  6. Capture screenshot of the full page
- Define success criteria: All islands mount, page structure is correct, no console errors
- Specify screenshot outputs with descriptive names

### 8. Validate the page loads in a browser
- Open `app/split-lease/pages/view-split-lease/index.html` in a browser
- Verify the page renders without errors
- Check that Header and Footer components mount correctly
- Inspect the page in browser DevTools for any console errors or warnings
- Test responsive behavior by resizing the browser window

### 9. Run validation commands
- Execute all validation commands to ensure zero regressions
- Run TypeScript type checking in components directory
- Run component build to validate UMD bundle generation
- Run all Playwright tests in test-harness
- Execute the new E2E test for view-split-lease page

## Testing Strategy

### Unit Tests
No new unit tests are required for this initial plain HTML page implementation. The existing component tests in `app/test-harness/` will validate that the Header and Footer components continue to work correctly when mounted as islands.

### E2E Tests
Create a dedicated E2E test file `.claude/commands/e2e/test_view_split_lease_page.md` that uses Playwright to:
- Navigate to the new view-split-lease page
- Verify the page title and meta tags are correct
- Confirm Header React island mounts successfully (check for rendered header elements)
- Confirm Footer React island mounts successfully (check for rendered footer elements)
- Verify no JavaScript console errors occur during page load
- Capture screenshots for visual verification
- Test responsive behavior at different viewport sizes

### Edge Cases
- **Slow network**: Verify React islands gracefully handle delayed CDN script loading
- **JavaScript disabled**: Ensure the page structure is visible even without React components (progressive enhancement)
- **Different viewport sizes**: Test on mobile (375px), tablet (768px), and desktop (1280px+) widths
- **Browser compatibility**: Test on Chrome, Firefox, Safari, and Edge
- **Direct URL access**: Verify the page can be accessed directly via URL (not just through navigation)

## Acceptance Criteria
- [ ] New page exists at `app/split-lease/pages/view-split-lease/index.html` with proper HTML5 structure
- [ ] Page includes proper meta tags for SEO and social media sharing
- [ ] Page title is "View Listing | Split Lease"
- [ ] React CDN scripts (React 18) are properly included and load successfully
- [ ] Split Lease components UMD bundle is included and loads successfully
- [ ] Header React island mounts successfully at `#site-header`
- [ ] Footer React island mounts successfully at `#site-footer`
- [ ] Page uses consistent CSS variables and styling from existing pages (primary color #31135D)
- [ ] CSS files (styles.css and responsive.css) follow existing conventions
- [ ] Page is responsive and displays correctly on mobile, tablet, and desktop viewports
- [ ] No console errors or warnings appear when page loads
- [ ] Page structure is semantic and accessible (proper heading hierarchy, ARIA labels if needed)
- [ ] E2E test file is created and validates the page works correctly
- [ ] All existing tests continue to pass (zero regressions)
- [ ] Component build and typecheck commands execute without errors

## Validation Commands
Execute every command to validate the feature works correctly with zero regressions.

- Read `.claude/commands/test_e2e.md` to understand how to run E2E tests
- Read and execute the new E2E test `.claude/commands/e2e/test_view_split_lease_page.md` to validate the page loads correctly with Header and Footer islands
- Manually open `app/split-lease/pages/view-split-lease/index.html` in a browser to verify visual appearance and functionality
- `cd app/split-lease/components && npm run typecheck` - Run TypeScript type checking to validate zero type errors
- `cd app/split-lease/components && npm run build` - Run component build to validate UMD bundle generation works
- `cd app/test-harness && npm test` - Run all component tests (contracts + diagnostics) to validate zero regressions

## Notes

### Future Enhancements
Once the foundational page is established, future iterations can add:
- Property image gallery component (React island)
- Listing details section (bedrooms, bathrooms, amenities)
- Schedule availability component (showing which days are available)
- Pricing information display
- Host profile section
- Reviews and ratings component
- Booking CTA component (React island)
- Map location component (React island)
- Similar listings recommendations
- Breadcrumb navigation

### Design Considerations
- The page follows the Islands Architecture pattern where static HTML is enhanced with interactive React components
- This approach ensures fast initial page loads and good SEO while enabling rich interactions where needed
- The minimal initial implementation makes it easy to incrementally add features without refactoring the foundation
- Consistent use of CSS variables ensures easy theme updates and maintenance

### Development Notes
- No new npm packages or dependencies are required for this feature
- The page uses existing shared Header and Footer components, promoting code reuse
- The HTML structure is intentionally simple to facilitate future enhancements
- Responsive design is mobile-first, following modern web development best practices
- The E2E test ensures the page continues to work correctly as the codebase evolves
