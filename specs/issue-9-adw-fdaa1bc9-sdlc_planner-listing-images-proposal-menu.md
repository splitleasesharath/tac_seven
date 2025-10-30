# Feature: Listing Images and Proposal Menu

## Metadata
issue_number: `9`
adw_id: `fdaa1bc9`
issue_json: `{"number":9,"title":"Listing Images and Proposal menu","body":"adw_plan_build_document_iso.py\n\nAdd to the view split lease page, side by side a image grid with 4 images of the listing, and on the right side the menu with the price and proposal settings. I collected context and stored in this directory C:\\Users\\Split Lease\\splitleaseteam\\!Agent Context and Tools\\SL1\\View split lease page context.  use playwright mcp to access the original page https://app.split.lease/version-test/view-split-lease/1637766467338x392186493055059600 only build those two sections "}`

## Feature Description
This feature adds two critical sections to the view split lease page in a side-by-side layout:
1. **Image Gallery (Left)**: A 2x2 grid displaying 4 listing images with a modern, responsive design
2. **Proposal Menu (Right)**: An interactive booking panel containing price display, ideal move-in date selector, weekly schedule selector, reservation span dropdown, and pricing summary

These components will transform the view split lease page from a static display into an interactive listing detail page, matching the design and functionality of the production Split Lease application at https://app.split.lease/version-test/view-split-lease/1637766467338x392186493055059600.

## User Story
As a potential tenant
I want to view listing images in a gallery and configure my rental proposal settings
So that I can evaluate the property visually and create a customized rental proposal that matches my schedule and budget needs

## Problem Statement
Currently, the Split Lease application lacks a dedicated view split lease page that displays listing images and allows users to configure rental proposals. Users need to see high-quality property images to make informed decisions and require an intuitive interface to set their ideal move-in date, select their weekly schedule, and choose reservation duration. Without this functionality, the platform cannot facilitate the core rental proposal workflow.

## Solution Statement
We will create two new React components (ListingImageGrid and ProposalMenu) that work together in a side-by-side layout using the existing Islands Architecture pattern. The ListingImageGrid will display 4 property images in a responsive 2x2 grid with hover effects and potential lightbox expansion. The ProposalMenu will provide an interactive form with date selection, a weekly schedule selector (leveraging patterns from SearchScheduleSelector), reservation span dropdown, and real-time pricing calculations. These components will be built as UMD bundles and mounted on a new view-split-lease page, maintaining consistency with the existing component architecture.

## Relevant Files
Use these files to implement the feature:

### Existing Files for Context and Patterns

- **README.md** - Project overview and Islands Architecture patterns, understanding how to build and integrate UMD components
- **app/split-lease/components/src/SearchScheduleSelector/SearchScheduleSelector.tsx** - Reference for day selector UI patterns, drag selection, and validation logic that will inform the weekly schedule selector in ProposalMenu
- **app/split-lease/components/src/SearchScheduleSelector/SearchScheduleSelector.styles.ts** - Reference for styled-components patterns, color schemes, and animation styles
- **app/split-lease/components/src/SearchScheduleSelector/types.ts** - Reference for TypeScript type patterns for props and state management
- **app/split-lease/components/src/index.ts** - Component export registry where new components must be added
- **app/split-lease/components/vite.config.ts** - UMD build configuration
- **app/split-lease/components/package.json** - Dependencies and build scripts
- **app/split-lease/pages/search/index.html** - Reference for how pages integrate React Islands
- **app/split-lease/pages/index.html** - Reference for page structure and CDN includes
- **C:\Users\Split Lease\splitleaseteam\!Agent Context and Tools\SL1\View split lease page context\COMPREHENSIVE SPLIT LEASE VIEW PAGE DOCUMENTATION-Elements.md** - Detailed specification of the booking panel elements, pricing display, date inputs, weekly schedule selector, reservation span dropdown, and all UI components needed for ProposalMenu
- **C:\Users\Split Lease\splitleaseteam\!Agent Context and Tools\SL1\View split lease page context\split-lease-full-page.png** - Visual reference for the layout and design of the image grid and proposal menu
- **.claude/commands/test_e2e.md** - E2E testing framework documentation for creating validation tests
- **.claude/commands/conditional_docs.md** - Guide for determining additional documentation needs

### New Files

- **app/split-lease/components/src/ListingImageGrid/ListingImageGrid.tsx** - Main component for the 2x2 image grid display
- **app/split-lease/components/src/ListingImageGrid/ListingImageGrid.styles.ts** - Styled components for image grid layout and hover effects
- **app/split-lease/components/src/ListingImageGrid/types.ts** - TypeScript interfaces for ListingImageGrid props
- **app/split-lease/components/src/ListingImageGrid/index.ts** - Component export file
- **app/split-lease/components/src/ProposalMenu/ProposalMenu.tsx** - Main component for the booking/proposal panel
- **app/split-lease/components/src/ProposalMenu/ProposalMenu.styles.ts** - Styled components for proposal menu layout and interactive elements
- **app/split-lease/components/src/ProposalMenu/types.ts** - TypeScript interfaces for ProposalMenu props including price data, date ranges, and schedule options
- **app/split-lease/components/src/ProposalMenu/index.ts** - Component export file
- **app/split-lease/pages/view-split-lease/index.html** - New page integrating both components in side-by-side layout
- **app/split-lease/pages/view-split-lease/css/styles.css** - Page-specific styles for the view split lease layout
- **app/split-lease/pages/view-split-lease/js/mount-islands.js** - JavaScript to mount both React Islands with appropriate props
- **.claude/commands/e2e/test_view_split_lease_page.md** - E2E test specification for validating the image grid and proposal menu functionality

## Implementation Plan

### Phase 1: Foundation
Create the foundational component structure and page infrastructure:
- Set up new component directories following existing patterns (ListingImageGrid and ProposalMenu)
- Create TypeScript type definitions based on the comprehensive element documentation
- Set up the new view-split-lease page directory with HTML, CSS, and JS files
- Review the context documentation and reference screenshot to understand exact requirements

### Phase 2: Core Implementation
Build the two main components with full styling and interactivity:
- Implement ListingImageGrid component with 2x2 responsive grid layout, image loading, and hover effects
- Implement ProposalMenu component with all interactive elements: price display, date input, weekly schedule selector (7 day buttons), reservation span dropdown, checkboxes, and pricing summary
- Apply styled-components patterns consistent with existing components (purple gradients, white backgrounds, rounded corners, shadows)
- Add proper TypeScript typing for all props and state
- Export both components from the main index.ts

### Phase 3: Integration
Connect the components to the page and test the complete workflow:
- Create the view-split-lease HTML page with proper CDN includes and island mount points
- Write mount-islands.js to instantiate both components with realistic test data
- Create page-specific CSS for the side-by-side layout (flex or grid)
- Build the UMD bundle and verify both components render correctly
- Create E2E test specification and validate all interactive elements work properly

## Step by Step Tasks
IMPORTANT: Execute every step in order, top to bottom.

### 1. Create Component Structure and Type Definitions
- Create directories: `app/split-lease/components/src/ListingImageGrid/` and `app/split-lease/components/src/ProposalMenu/`
- Create `ListingImageGrid/types.ts` with interfaces for image data (url, alt, thumbnail properties)
- Create `ProposalMenu/types.ts` with comprehensive interfaces based on the element documentation: price data, date selection, weekly schedule state, reservation span options, pricing summary
- Create basic index.ts export files for both components

### 2. Implement ListingImageGrid Component
- Create `ListingImageGrid.tsx` with React functional component accepting image array prop
- Implement 2x2 CSS Grid layout in `ListingImageGrid.styles.ts` with responsive design (single column on mobile)
- Add image loading states, error handling for missing images, and hover effects (scale/zoom)
- Add proper TypeScript typing for component props
- Consider accessibility (alt text, keyboard navigation)

### 3. Implement ProposalMenu Component - Part 1 (Structure and Styling)
- Create `ProposalMenu.tsx` with component structure matching the documented elements
- Create `ProposalMenu.styles.ts` with styled components for: container, price display (large purple text), section labels, input fields, buttons, and pricing summary
- Apply consistent styling with SearchScheduleSelector (purple gradients, white backgrounds, border-radius, shadows)
- Use responsive design patterns (stack vertically on mobile)

### 4. Implement ProposalMenu Component - Part 2 (Interactive Elements)
- Implement price display section with per-night pricing
- Add ideal move-in date input (text input with date format, checkbox for "strict" option)
- Create weekly schedule selector with 7 day buttons (reuse patterns from SearchScheduleSelector for selection logic)
- Add selection status text ("X days, Y nights Selected", "Check-in day is...", "Check-out day is...")
- Add warning/note sections with conditional rendering

### 5. Implement ProposalMenu Component - Part 3 (Reservation Span and Pricing)
- Create reservation span dropdown with predefined options (6-26 weeks) and "Other" custom input
- Add host preference note display
- Implement pricing summary calculations (4-week rent, total reservation estimate)
- Add action button (CTA) with appropriate styling
- Wire up all state management with React hooks (useState for selections, useEffect for calculations)

### 6. Export Components from Main Index
- Update `app/split-lease/components/src/index.ts` to export both ListingImageGrid and ProposalMenu
- Ensure TypeScript types are exported alongside components
- Verify export syntax matches existing components

### 7. Create View Split Lease Page Structure
- Create directory `app/split-lease/pages/view-split-lease/` with subdirectories: `css/`, `js/`
- Create `index.html` with proper HTML5 structure, meta tags, and title
- Add React CDN includes (react@18, react-dom@18)
- Add component bundle include (`../../components/dist/split-lease-components.umd.cjs`)
- Add stylesheet includes (component styles and page-specific styles)
- Create two mount point divs: `<div id="listing-images"></div>` and `<div id="proposal-menu"></div>`
- Wrap mount points in a container div with class for side-by-side layout

### 8. Create Page Styles and Mount Script
- Create `view-split-lease/css/styles.css` with side-by-side layout (flexbox or grid, 60/40 split)
- Add responsive breakpoints (stack vertically on tablets/mobile)
- Add page-specific spacing, margins, and container max-width
- Create `view-split-lease/js/mount-islands.js` to mount both components using `ReactDOM.createRoot`
- Pass realistic test data: 4 image URLs, price ($434.07/night), date defaults, reservation options
- Add defer attribute to script tag in HTML

### 9. Build Component Bundle
- Run `cd app/split-lease/components && npm run typecheck` to verify zero TypeScript errors
- Fix any type errors that appear
- Run `cd app/split-lease/components && npm run build` to generate UMD bundle
- Verify `dist/split-lease-components.umd.cjs` includes both new components
- Verify `dist/style.css` includes styles for both components

### 10. Manual Verification and Testing
- Open `app/split-lease/pages/view-split-lease/index.html` in a browser (or use live-server)
- Verify ListingImageGrid displays 4 images in a 2x2 grid
- Verify ProposalMenu displays all sections: price, date input, weekly schedule, reservation span, pricing summary
- Test interactivity: click day buttons, change dropdown, input values
- Test responsive design at different screen sizes
- Check browser console for any errors or warnings

### 11. Create E2E Test Specification
- Create `.claude/commands/e2e/test_view_split_lease_page.md` following the pattern in `test_e2e.md`
- Define User Story for the test (viewing listing images and configuring proposal)
- Create Test Steps section with detailed Playwright instructions:
  - Navigate to view-split-lease page
  - Verify ListingImageGrid renders with 4 images
  - Verify ProposalMenu renders with all sections visible
  - Interact with weekly schedule selector (click days, verify selection state)
  - Interact with reservation span dropdown (select option, verify display update)
  - Verify pricing calculations update correctly
  - Capture screenshots at each major step
- Define Success Criteria (all elements visible, interactions work, no console errors)
- Specify screenshot names and paths

### 12. Run Validation Commands
- Execute all validation commands to ensure zero regressions:
  - `cd app/split-lease/components && npm run typecheck` - Verify TypeScript compilation
  - `cd app/split-lease/components && npm run build` - Verify UMD bundle builds successfully
  - `cd app/test-harness && npm test` - Run all component tests (contracts + diagnostics)
- Read `.claude/commands/test_e2e.md` and execute the E2E test spec to validate the new functionality works end-to-end
- Fix any failures or errors that occur
- Ensure all validation commands pass before considering the feature complete

## Testing Strategy

### Unit Tests
While the project currently uses Playwright for component testing via the test-harness, we should ensure:
- ListingImageGrid handles missing or invalid image URLs gracefully
- ProposalMenu validates date inputs and shows appropriate error messages
- Weekly schedule selector enforces any business rules (contiguous days, min/max nights)
- Reservation span calculations are accurate across all options
- Pricing summary updates correctly when inputs change

### Integration Tests
Use the existing test-harness infrastructure:
- Create contract tests for ListingImageGrid (verify it exposes expected API in UMD bundle)
- Create contract tests for ProposalMenu (verify it exposes expected API and accepts props correctly)
- Create diagnostic tests to verify rendering and basic interactivity
- Follow patterns from `app/test-harness/tests/search-schedule-selector-contract.spec.js`

### E2E Tests
Create a comprehensive E2E test using Playwright MCP:
- Test full user workflow: viewing images, selecting dates, choosing schedule, seeing pricing update
- Verify all interactive elements respond to user input
- Capture screenshots showing both components working together
- Test responsive behavior at different viewport sizes
- Validate against the production page at https://app.split.lease/version-test/view-split-lease/1637766467338x392186493055059600

### Edge Cases
- **ListingImageGrid**:
  - Fewer than 4 images provided (show placeholders or empty slots)
  - Image load failures (show fallback image or error state)
  - Very large images (ensure proper scaling and performance)
- **ProposalMenu**:
  - Invalid date formats in ideal move-in input
  - Selecting discontiguous days in weekly schedule (if not allowed)
  - Selecting reservation span outside host's preference range
  - Custom "Other" weeks input with invalid values
  - Edge case calculations (very short or very long reservations)
  - Zero days selected in weekly schedule

## Acceptance Criteria
1. ListingImageGrid component displays 4 images in a responsive 2x2 grid that stacks on mobile
2. Images have hover effects (scale or zoom) and proper alt text for accessibility
3. ProposalMenu component displays all sections with proper styling matching the reference design:
   - Price display showing per-night rate in large purple text
   - Ideal move-in date input with checkbox for "strict" option
   - Weekly schedule with 7 day buttons (S, M, T, W, T, F, S) that toggle selection
   - Selection status showing days, nights, check-in, and check-out information
   - Reservation span dropdown with all options (6-26 weeks) and custom input
   - Pricing summary showing 4-week rent and total reservation estimate
   - Action button (CTA) with appropriate text and styling
4. Weekly schedule selector allows users to select/deselect days by clicking
5. Selection status text updates in real-time as days are selected/deselected
6. Reservation span dropdown changes update the pricing summary calculations
7. Pricing calculations are accurate based on per-night rate, selected days, and reservation span
8. Warning/note messages display when user selections don't match host preferences
9. View split lease page (/view-split-lease/index.html) renders both components side-by-side on desktop
10. Layout is responsive: components stack vertically on mobile/tablet breakpoints
11. TypeScript compilation passes with zero errors
12. Component build succeeds and generates valid UMD bundle
13. All existing tests continue to pass (zero regressions)
14. E2E test validates full user interaction workflow with screenshots
15. Components follow existing code patterns and styling conventions (purple gradients, styled-components, Islands Architecture)

## Validation Commands
Execute every command to validate the feature works correctly with zero regressions.

- `cd app/split-lease/components && npm run typecheck` - Run TypeScript type checking to validate zero type errors
- `cd app/split-lease/components && npm run build` - Run component build to validate UMD bundle generation works
- `cd app/test-harness && npm test` - Run all component tests (contracts + diagnostics) to validate zero regressions
- Read `.claude/commands/test_e2e.md`, then read and execute the new E2E test file `.claude/commands/e2e/test_view_split_lease_page.md` to validate this functionality works end-to-end

## Notes

### Design Reference
The comprehensive documentation in `C:\Users\Split Lease\splitleaseteam\!Agent Context and Tools\SL1\View split lease page context\COMPREHENSIVE SPLIT LEASE VIEW PAGE DOCUMENTATION-Elements.md` provides exact specifications for all ProposalMenu elements including:
- Exact text labels and formatting
- Reference IDs for each UI element
- Dropdown options and their display format
- Calculation formulas and business rules
- Warning/note message conditions

Use this documentation as the source of truth for all UI text, options, and behavior.

### Production Page Reference
The live page at https://app.split.lease/version-test/view-split-lease/1637766467338x392186493055059600 should be accessed via Playwright MCP during E2E testing to:
- Capture reference screenshots for visual comparison
- Understand exact interaction patterns and animations
- Validate that our implementation matches production behavior
- Extract any missing details not in the documentation

### Image Data
For initial implementation, use placeholder image URLs or sample images. In production, these would come from an API or be passed as props from the page. The ListingImageGrid component should accept an array of image objects with properties: `url`, `alt`, `thumbnail` (optional).

### Pricing Logic
The pricing calculations should be configurable via props. Initial implementation can use:
- Per-night rate: $434.07 (from documentation)
- 4-week rent calculation: (nights per week) × 4 × per-night rate
- Total reservation: 4-week rent × (reservation span in weeks / 4)

Ensure all calculations round appropriately for currency display.

### Weekly Schedule Integration
The weekly schedule selector in ProposalMenu can reuse significant logic from SearchScheduleSelector:
- Day button styling and animations
- Selection state management
- Validation logic for contiguous days
- Status text generation

However, it should be a simplified version without drag-to-select, focusing on click-to-toggle functionality.

### Responsive Design
Follow the mobile-first approach used in SearchScheduleSelector:
- Define base styles for mobile
- Use `@media (min-width: 768px)` for tablet adjustments
- Use `@media (min-width: 1024px)` for desktop side-by-side layout
- Ensure touch targets are at least 44x44px for mobile usability

### Future Enhancements
Consider for future iterations (not part of this feature):
- Lightbox/modal for full-screen image viewing
- Image carousel/slider for more than 4 images
- Integration with real backend API for pricing and availability
- Form validation and submission for proposal creation
- Calendar picker for ideal move-in date instead of text input
- Tooltips or help text for info icons
- Animation/transition effects when switching between reservation spans
