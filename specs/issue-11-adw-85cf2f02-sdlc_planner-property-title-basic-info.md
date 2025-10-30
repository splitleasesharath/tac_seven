# Feature: Property Title and Basic Information Display

## Metadata
issue_number: `11`
adw_id: `85cf2f02`
issue_json: `{"number":11,"title":"Property title and basic information","body":"adw_plan_build_document_iso\n\nAdd to the view split lease page under the listing images secion a property header section displaying the main listing title \"Holiday Rental: Luxurious, Sunny, and Quiet Apt on Central Park West\" in a large, bold heading font. Below the title, add a location line with a purple map pin icon and the text \"Located in Manhattan Valley, Manhattan\". Underneath, display the property type information \"Private Room - 2 guests max\" in a smaller, secondary text style.\n\nContext stored in: \"C:\\Users\\Split Lease\\splitleaseteam!Agent Context and Tools\\SL1\\View split lease page context \"or  \"C:\\Users\\igor\\splitleaseteam!Agent Context and Tools\\SL1\\View split lease page context\"\n\nUse Playwright MCP to access original page: https://app.split.lease/version-test/view-split-lease/1637766467338x392186493055059600"}`

## Feature Description
This feature adds a property header section to the view split lease page that displays key property information in a clear, hierarchical layout. The component will show the property title as a prominent heading, followed by location details with an icon, and property type information with guest capacity. This improves the user experience by immediately presenting the most important property details at the top of the listing page, allowing users to quickly assess if the property meets their needs before scrolling through additional details.

## User Story
As a potential guest browsing split lease listings
I want to immediately see the property title, location, and basic details when viewing a listing page
So that I can quickly determine if this property matches my requirements before investing time reviewing additional details

## Problem Statement
Currently, the view split lease page lacks a clear, prominent header section that displays essential property information. Users viewing a property listing need to immediately see:
- The property title to understand what type of accommodation is being offered
- The location with visual indicators to know where the property is situated
- Basic property details like room type and guest capacity

Without this information prominently displayed at the top of the page, users may have difficulty quickly assessing whether a property meets their needs, leading to a poor browsing experience and potentially higher bounce rates.

## Solution Statement
We will create a new React component called `PropertyHeader` that displays property information in a structured, visually appealing format. The component will:

1. Display the property title in a large, bold heading (H1) for maximum visibility
2. Show location information with a purple map pin icon, creating a clear visual association with geographic location
3. Present property type and guest capacity in a smaller, secondary text style for supporting details

The component will follow the Islands Architecture pattern used throughout the application, being built as part of the UMD component bundle and mounted on static HTML pages. It will use the same styling conventions as existing components (CSS-in-JS with separate CSS files) and support responsive design for mobile and desktop viewports.

## Relevant Files
Use these files to implement the feature:

- **app/split-lease/components/src/PropertyHeader/PropertyHeader.tsx** - Main component implementation with props interface
  - Will contain the React component logic for displaying property title, location, and basic info
  - Follows existing component patterns seen in Header.tsx and Footer.tsx

- **app/split-lease/components/src/PropertyHeader/PropertyHeader.css** - Component-specific styles
  - Will define CSS variables for customization (purple color for map pin, typography scales)
  - Includes responsive styles for mobile and desktop viewports
  - Follows the styling approach used in Header.css and Footer.css

- **app/split-lease/components/src/PropertyHeader/index.ts** - Component export
  - Re-exports the PropertyHeader component and its types
  - Makes the component available to the UMD bundle

- **app/split-lease/components/src/index.ts** - Main component library entry point
  - Needs to export PropertyHeader to include it in the UMD bundle
  - Makes component accessible via window.SplitLeaseComponents.PropertyHeader

- **app/test-harness/tests/PropertyHeader.contract.spec.js** - Contract test file
  - Validates PropertyHeader component mounts correctly in isolation
  - Tests component with various prop configurations
  - Ensures TypeScript types are working correctly

- **app/test-harness/tests/PropertyHeader.diagnostics.spec.js** - Diagnostics test file
  - Validates visual rendering and styling
  - Tests responsive behavior
  - Verifies icon display and layout structure

### New Files

- **app/split-lease/pages/view-split-lease/index.html** - New HTML page for viewing split lease listings
  - Static HTML page following Islands Architecture pattern
  - Includes React CDN, component UMD bundle, Header, Footer, and PropertyHeader islands
  - Contains placeholder for listing images section above PropertyHeader

- **app/split-lease/pages/view-split-lease/css/styles.css** - Page-specific styles
  - Page layout and structure styles
  - Spacing and positioning for component islands
  - Does not duplicate component-specific styles

- **.claude/commands/e2e/test_property_header.md** - E2E test specification
  - Validates PropertyHeader displays correctly on view-split-lease page
  - Tests title, location, and property type rendering
  - Verifies purple map pin icon is visible
  - Captures screenshots for visual verification

## Implementation Plan

### Phase 1: Foundation
Create the PropertyHeader React component with TypeScript interfaces, following the existing component patterns in the codebase. Set up the component directory structure with PropertyHeader.tsx, PropertyHeader.css, and index.ts files. Define the component props interface to accept title, location (neighborhood and city), property type, and guest capacity. Implement responsive CSS using CSS variables for consistency with other components. This phase establishes the foundational component that can be reused across different pages.

### Phase 2: Core Implementation
Implement the PropertyHeader component rendering logic with proper semantic HTML (H1 for title, appropriate elements for location and details). Style the component using the CSS file with proper typography hierarchy - large bold heading for title, medium weight for location with icon, and lighter weight for property details. Add an SVG map pin icon inline in the component (purple color, matching brand) or use an icon from the existing shared assets. Ensure the component follows responsive design principles with proper scaling on mobile devices. Write comprehensive contract and diagnostics tests to validate component behavior and visual rendering.

### Phase 3: Integration
Create the view-split-lease page HTML file and mount the PropertyHeader component as an island along with Header and Footer components. Export PropertyHeader from the main component index to include it in the UMD bundle. Build the component library and verify the PropertyHeader appears in the bundle. Create an E2E test specification that validates the complete user experience on the view-split-lease page. Test the component integration with static content and ensure proper styling, layout, and responsive behavior across different viewport sizes.

## Step by Step Tasks
IMPORTANT: Execute every step in order, top to bottom.

### 1. Create PropertyHeader Component Structure
- Create directory `app/split-lease/components/src/PropertyHeader/`
- Create `PropertyHeader.tsx` with TypeScript interface for props (title, location object with neighborhood and city, propertyType, maxGuests)
- Create `PropertyHeader.css` with CSS variables for purple map pin color (#7C3AED or similar), typography scales, and spacing
- Create `index.ts` that exports PropertyHeader component and types
- Follow the same pattern used in Header and Footer components

### 2. Implement PropertyHeader Component
- Implement the PropertyHeader React component with proper semantic HTML structure
- Use H1 for the property title with large, bold styling
- Create a location section with purple map pin icon (inline SVG or from shared assets) and location text
- Add property type and guest capacity display in smaller, secondary text
- Import and apply CSS from PropertyHeader.css
- Ensure component accepts props with TypeScript types: title (string), location ({ neighborhood: string, city: string }), propertyType (string), maxGuests (number)
- Add proper className prop support for additional styling customization

### 3. Style PropertyHeader Component
- Define CSS variables in PropertyHeader.css: --property-header-purple (#7C3AED), --title-font-size, --location-font-size, --details-font-size
- Style the title as a large, bold heading (2rem+ font size, font-weight 700+)
- Style location with flexbox layout, gap between icon and text, medium font weight
- Style property details in smaller, gray text (#6b7280 or similar)
- Add responsive breakpoints for mobile (reduce font sizes, adjust spacing)
- Use consistent spacing units (rem) and follow existing component styling patterns
- Ensure proper vertical spacing between title, location, and property details sections

### 4. Export PropertyHeader from Component Library
- Edit `app/split-lease/components/src/index.ts`
- Add export statement: `export { PropertyHeader } from './PropertyHeader';`
- This makes PropertyHeader available in the UMD bundle as `window.SplitLeaseComponents.PropertyHeader`

### 5. Create PropertyHeader Contract Tests
- Create file `app/test-harness/tests/PropertyHeader.contract.spec.js`
- Write tests that validate:
  - Component mounts without errors
  - Component accepts and displays title prop correctly
  - Component accepts and displays location props (neighborhood, city)
  - Component accepts and displays propertyType and maxGuests props
  - Component handles missing optional props gracefully
  - TypeScript types work correctly
- Follow the same testing patterns used for other components in the test harness

### 6. Create PropertyHeader Diagnostics Tests
- Create file `app/test-harness/tests/PropertyHeader.diagnostics.spec.js`
- Write tests that validate:
  - Title renders with correct styling (large, bold font)
  - Location section displays with purple map pin icon visible
  - Property details display in correct secondary style
  - Component layout is correct (title on top, location below, details at bottom)
  - Responsive behavior works (component scales properly on mobile viewport)
  - CSS classes are applied correctly
- Use Playwright for visual regression testing where appropriate

### 7. Create E2E Test Specification
- Create directory `.claude/commands/e2e/` if it doesn't exist
- Create file `.claude/commands/e2e/test_property_header.md`
- Read `.claude/commands/test_e2e.md` to understand the E2E test format and structure
- Write E2E test specification that includes:
  - User story describing what we're validating
  - Test steps to navigate to view-split-lease page and verify PropertyHeader displays
  - Success criteria for title visibility, location with purple icon, property details
  - Screenshot capture points for visual verification
  - Follow the format used in other E2E test files

### 8. Create View Split Lease Page
- Create directory `app/split-lease/pages/view-split-lease/`
- Create `index.html` with Islands Architecture pattern:
  - Include React 18 CDN scripts (production UMD)
  - Include ReactDOM 18 CDN scripts (production UMD)
  - Include component UMD bundle: `../../components/dist/split-lease-components.umd.js`
  - Mount Header island in a div with id="site-header"
  - Add placeholder section for listing images (commented HTML or placeholder div)
  - Mount PropertyHeader island in a div with id="property-header" below images section
  - Mount Footer island in a div with id="site-footer"
  - Pass sample props to PropertyHeader via React.createElement
- Create `css/` subdirectory and `css/styles.css` for page-specific layout styles

### 9. Implement PropertyHeader Island Mounting
- In `view-split-lease/index.html`, add script block to mount PropertyHeader:
  ```javascript
  const { PropertyHeader } = window.SplitLeaseComponents || {};
  if (PropertyHeader) {
    ReactDOM.createRoot(document.getElementById('property-header'))
      .render(React.createElement(PropertyHeader, {
        title: 'Holiday Rental: Luxurious, Sunny, and Quiet Apt on Central Park West',
        location: { neighborhood: 'Manhattan Valley', city: 'Manhattan' },
        propertyType: 'Private Room',
        maxGuests: 2
      }));
  }
  ```
- Mount Header and Footer islands following the same pattern
- Ensure proper error handling if components are not available in bundle

### 10. Style View Split Lease Page
- Create `app/split-lease/pages/view-split-lease/css/styles.css`
- Add page layout styles (body, container widths, spacing between islands)
- Add placeholder styles for listing images section (e.g., gray box with text "Listing Images")
- Position PropertyHeader island with appropriate top margin below images section
- Ensure consistent spacing between Header, content sections, and Footer
- Add responsive styles for mobile and tablet viewports
- Do not duplicate component-specific styles (those belong in component CSS files)

### 11. Run Validation Commands
- Execute all validation commands from the "Validation Commands" section below
- Verify zero TypeScript type errors
- Verify UMD bundle builds successfully with PropertyHeader included
- Verify all contract and diagnostic tests pass
- Execute E2E test to validate end-to-end user experience
- Fix any errors or failing tests before marking feature complete

## Testing Strategy

### Unit Tests

**Contract Tests (PropertyHeader.contract.spec.js)**
- Test component mounts successfully in isolation
- Verify component accepts all required and optional props
- Test prop validation and TypeScript types
- Verify component renders without errors when props are valid
- Test edge cases: empty strings, missing location fields, zero guests

**Diagnostics Tests (PropertyHeader.diagnostics.spec.js)**
- Verify visual rendering matches design requirements
- Test title displays in large, bold font
- Verify purple map pin icon is visible and colored correctly
- Test location text displays neighborhood and city correctly
- Verify property details display in secondary styling
- Test responsive behavior at different viewport sizes (mobile, tablet, desktop)
- Verify proper spacing and layout hierarchy

**E2E Tests (test_property_header.md)**
- Navigate to view-split-lease page at http://localhost:8080/view-split-lease/
- Verify page loads successfully with no console errors
- Verify Header, PropertyHeader, and Footer islands mount correctly
- Verify PropertyHeader displays title: "Holiday Rental: Luxurious, Sunny, and Quiet Apt on Central Park West"
- Verify location displays: "Located in Manhattan Valley, Manhattan" with purple map pin icon
- Verify property details display: "Private Room - 2 guests max"
- Capture screenshots for visual verification
- Test on mobile viewport (375px width) and desktop viewport (1280px width)

### Edge Cases

1. **Missing or Empty Props**
   - Component should handle missing title gracefully (show placeholder or hide section)
   - Component should handle partial location data (only neighborhood or only city)
   - Component should handle zero or negative maxGuests (show "Contact host for details" or similar)

2. **Long Text Content**
   - Title longer than 100 characters should wrap properly, not overflow
   - Location names with special characters or very long names should display correctly
   - Property type with multiple details should format nicely

3. **Responsive Viewports**
   - Component should scale typography and spacing appropriately on mobile (< 768px)
   - Component should maintain readability on very small screens (< 375px)
   - Component should not cause horizontal scrolling on any viewport size

4. **Icon Display**
   - Map pin SVG icon should render correctly in all browsers
   - Icon color (purple) should match brand guidelines
   - Icon should scale proportionally with text on different viewports

5. **Component Bundle**
   - PropertyHeader should be available in window.SplitLeaseComponents after bundle loads
   - Component should work when React/ReactDOM are loaded from CDN
   - Component should not cause console errors if mounted before bundle is loaded

## Acceptance Criteria

1. **PropertyHeader Component Created**
   - ✅ PropertyHeader component exists at `app/split-lease/components/src/PropertyHeader/PropertyHeader.tsx`
   - ✅ Component has TypeScript interface defining props: title, location, propertyType, maxGuests
   - ✅ Component CSS file exists at `app/split-lease/components/src/PropertyHeader/PropertyHeader.css`
   - ✅ Component is exported from `app/split-lease/components/src/index.ts`

2. **Visual Requirements Met**
   - ✅ Property title displays in large, bold heading font (H1, 2rem+, font-weight 700+)
   - ✅ Location displays with purple map pin icon (#7C3AED or similar) and text "Located in [neighborhood], [city]"
   - ✅ Property type and guest capacity display in smaller, secondary text style
   - ✅ Component layout follows hierarchy: title → location → property details

3. **View Split Lease Page Created**
   - ✅ Page exists at `app/split-lease/pages/view-split-lease/index.html`
   - ✅ Page includes Header, PropertyHeader, and Footer islands
   - ✅ PropertyHeader is positioned below listing images section (placeholder)
   - ✅ PropertyHeader island displays with correct sample data from issue description

4. **Component Integration**
   - ✅ PropertyHeader is included in UMD bundle (`split-lease-components.umd.js`)
   - ✅ Component is accessible via `window.SplitLeaseComponents.PropertyHeader`
   - ✅ Component mounts successfully on view-split-lease page
   - ✅ No console errors when page loads

5. **Testing Complete**
   - ✅ Contract tests pass (PropertyHeader.contract.spec.js)
   - ✅ Diagnostics tests pass (PropertyHeader.diagnostics.spec.js)
   - ✅ E2E test specification created (test_property_header.md)
   - ✅ E2E test executes successfully and validates feature
   - ✅ All validation commands execute without errors

6. **Responsive Design**
   - ✅ Component displays correctly on desktop viewports (1280px+)
   - ✅ Component displays correctly on tablet viewports (768px-1279px)
   - ✅ Component displays correctly on mobile viewports (< 768px)
   - ✅ Typography scales appropriately across viewport sizes
   - ✅ No horizontal scrolling on any viewport size

7. **Code Quality**
   - ✅ TypeScript type checking passes with zero errors
   - ✅ Component follows existing patterns from Header and Footer components
   - ✅ CSS follows existing conventions with CSS variables and responsive design
   - ✅ Code is properly formatted and readable
   - ✅ No linting errors or warnings

## Validation Commands
Execute every command to validate the feature works correctly with zero regressions.

Read `.claude/commands/test_e2e.md`, then read and execute your new E2E `.claude/commands/e2e/test_property_header.md` test file to validate this functionality works.

- `cd app/split-lease/components && npm run typecheck` - Run TypeScript type checking to validate zero type errors
- `cd app/split-lease/components && npm run build` - Run component build to validate UMD bundle generation works and PropertyHeader is included
- `cd app/test-harness && npm test` - Run all component tests (contracts + diagnostics) to validate zero regressions
- Verify the PropertyHeader component is exported correctly: `grep -r "PropertyHeader" app/split-lease/components/dist/split-lease-components.umd.js` - Should find references to PropertyHeader in the bundle
- Open `app/split-lease/pages/view-split-lease/index.html` in a browser and verify:
  - Header displays at top of page
  - Placeholder for listing images section is visible
  - PropertyHeader displays below images with correct title, location, and property details
  - Purple map pin icon is visible next to location text
  - Footer displays at bottom of page
  - No console errors
  - Page is responsive on mobile viewport

## Notes

### Technology Stack
- React 18 (loaded via CDN on static pages)
- TypeScript for component development
- CSS for styling (not styled-components, following Header and Footer patterns)
- Islands Architecture (static HTML + React component islands)
- Vite for UMD bundle generation

### Design Considerations
- Purple brand color (#7C3AED or similar) should be used for the map pin icon to match the Split Lease brand
- Typography hierarchy is critical: title should be immediately noticeable, location should be easy to scan, property details should be supportive
- Component should be flexible enough to accept different property data via props, not hardcoded to one listing
- The component should work with the existing Islands Architecture pattern without requiring server-side rendering

### Future Enhancements (Not in Scope)
- Dynamic data loading from an API for property information
- Interactive map pin that opens a map modal when clicked
- Property availability calendar integration
- Host profile section below property header
- Social sharing buttons for the listing
- Favorite/bookmark functionality

### SVG Map Pin Icon
Consider using this inline SVG for the purple map pin icon:
```html
<svg width="16" height="20" viewBox="0 0 16 20" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 0C3.58 0 0 3.58 0 8C0 12 8 20 8 20C8 20 16 12 16 8C16 3.58 12.42 0 8 0ZM8 11C6.34 11 5 9.66 5 8C5 6.34 6.34 5 8 5C9.66 5 11 6.34 11 8C11 9.66 9.66 11 8 11Z" fill="#7C3AED"/>
</svg>
```

### Context Files
The issue mentions context stored at specific paths. These context files may contain additional design details or screenshots that should be referenced if available:
- `C:\Users\Split Lease\splitleaseteam!Agent Context and Tools\SL1\View split lease page context`
- `C:\Users\igor\splitleaseteam!Agent Context and Tools\SL1\View split lease page context`

The original page can be accessed for reference at: https://app.split.lease/version-test/view-split-lease/1637766467338x392186493055059600

Use Playwright MCP to capture screenshots of the original page if needed for design reference.
