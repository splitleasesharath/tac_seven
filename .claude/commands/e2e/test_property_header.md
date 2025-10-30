# E2E Test: PropertyHeader Component on View Split Lease Page

## Test Metadata
- **Test Name**: PropertyHeader Component Display
- **Feature**: Property Title and Basic Information Display
- **Page URL**: http://localhost:8080/view-split-lease/
- **Components Tested**: PropertyHeader, Header, Footer

## User Story
As a potential guest browsing split lease listings
I want to immediately see the property title, location, and basic details when viewing a listing page
So that I can quickly determine if this property matches my requirements before investing time reviewing additional details

## Test Objective
Validate that the PropertyHeader component displays correctly on the view-split-lease page with the correct title, location (including purple map pin icon), and property details. Ensure the component renders below the listing images placeholder and follows the expected visual hierarchy.

## Test Steps

### Step 1: Navigate to View Split Lease Page
- **Action**: Navigate to http://localhost:8080/view-split-lease/
- **Verify**: Page loads successfully without errors
- **Verify**: HTTP status is 200 or page is accessible
- **Screenshot**: Capture full page view

### Step 2: Verify Header Island Mounts
- **Action**: Check that the Header component (site navigation) is present at the top of the page
- **Verify**: Element with id="site-header" or class="main-header" is visible
- **Verify**: Header displays "Split Lease" logo and navigation links

### Step 3: Verify Listing Images Section Placeholder
- **Action**: Check that there is a placeholder or section for listing images
- **Verify**: Element with id="listing-images" or similar is present
- **Verify**: This element appears before the PropertyHeader component

### Step 4: Verify PropertyHeader Island Mounts
- **Action**: Check that the PropertyHeader component is present on the page
- **Verify**: Element with id="property-header" exists
- **Verify**: Element with class="property-header" is visible
- **Screenshot**: Capture PropertyHeader component area

### Step 5: Verify Property Title Display
- **Action**: Locate the property title element
- **Verify**: Title displays: "Holiday Rental: Luxurious, Sunny, and Quiet Apt on Central Park West"
- **Verify**: Title is rendered as an H1 element
- **Verify**: Title uses large, bold font (visually prominent)
- **Verify**: Title text is fully visible and not truncated

### Step 6: Verify Location Display with Purple Map Pin
- **Action**: Locate the property location section
- **Verify**: Location text displays: "Located in Manhattan Valley, Manhattan"
- **Verify**: Purple map pin icon is visible next to the location text
- **Verify**: Map pin icon is the correct color (purple, approximately #7C3AED)
- **Verify**: Icon and text are horizontally aligned
- **Screenshot**: Capture close-up of location section with map pin icon

### Step 7: Verify Property Details Display
- **Action**: Locate the property details section
- **Verify**: Property type displays: "Private Room"
- **Verify**: Guest capacity displays: "2 guests max"
- **Verify**: Details are in smaller, secondary text style (lighter than title)
- **Verify**: Format is: "[Property Type] - [X] guest[s] max"

### Step 8: Verify Component Hierarchy
- **Action**: Validate the visual hierarchy of PropertyHeader elements
- **Verify**: Title appears at the top of PropertyHeader
- **Verify**: Location section appears below title
- **Verify**: Property details appear below location
- **Verify**: Proper vertical spacing between all sections

### Step 9: Verify Footer Island Mounts
- **Action**: Check that the Footer component is present at the bottom of the page
- **Verify**: Element with id="site-footer" or class="main-footer" is visible
- **Verify**: Footer displays copyright and links

### Step 10: Test Mobile Responsive Behavior
- **Action**: Resize viewport to mobile width (375px x 667px)
- **Verify**: PropertyHeader component scales appropriately
- **Verify**: Title text wraps if needed and remains readable
- **Verify**: No horizontal scrolling occurs
- **Verify**: All elements remain visible and properly formatted
- **Screenshot**: Capture mobile view of PropertyHeader

### Step 11: Test Desktop Responsive Behavior
- **Action**: Resize viewport to desktop width (1280px x 720px)
- **Verify**: PropertyHeader component displays with full desktop styling
- **Verify**: Title uses large font size (2rem or approximately 32px)
- **Verify**: All elements maintain proper spacing and layout
- **Screenshot**: Capture desktop view of PropertyHeader

### Step 12: Check for Console Errors
- **Action**: Review browser console for any errors or warnings
- **Verify**: No JavaScript errors related to PropertyHeader component
- **Verify**: No CSS loading errors
- **Verify**: No React rendering errors or warnings

## Success Criteria

1. ✅ View split lease page loads successfully at http://localhost:8080/view-split-lease/
2. ✅ Header component mounts and displays at top of page
3. ✅ PropertyHeader component mounts and displays on the page
4. ✅ Property title displays correctly: "Holiday Rental: Luxurious, Sunny, and Quiet Apt on Central Park West"
5. ✅ Title is rendered as H1 with large, bold font
6. ✅ Location displays: "Located in Manhattan Valley, Manhattan"
7. ✅ Purple map pin icon is visible next to location text
8. ✅ Map pin icon color is purple (approximately #7C3AED)
9. ✅ Property details display: "Private Room - 2 guests max"
10. ✅ Component hierarchy is correct: title → location → details
11. ✅ PropertyHeader appears below listing images placeholder
12. ✅ Footer component mounts and displays at bottom of page
13. ✅ Component is responsive on mobile viewport (375px width)
14. ✅ Component is responsive on desktop viewport (1280px width)
15. ✅ No horizontal scrolling on any viewport size
16. ✅ No console errors or warnings

## Expected Screenshots

1. **01_full_page_view.png** - Full page view showing Header, PropertyHeader, and Footer
2. **02_property_header_detail.png** - Close-up of PropertyHeader component
3. **03_location_with_map_pin.png** - Close-up of location section showing purple map pin icon
4. **04_mobile_view.png** - Mobile viewport (375px) showing responsive PropertyHeader
5. **05_desktop_view.png** - Desktop viewport (1280px) showing full PropertyHeader

## Notes

- Ensure the static file server is running on port 8080 before executing this test
- The PropertyHeader component is loaded via the UMD bundle at `../../components/dist/split-lease-components.umd.js`
- React 18 is loaded from CDN (unpkg.com)
- Allow sufficient time for React islands to mount (at least 1-2 seconds after page load)
- If the page returns 404, verify that the view-split-lease directory exists at `app/split-lease/pages/view-split-lease/`

## Output Format

```json
{
  "test_name": "PropertyHeader Component Display",
  "status": "passed|failed",
  "screenshots": [
    "<absolute path>/agents/<adw_id>/<agent_name>/img/property_header/01_full_page_view.png",
    "<absolute path>/agents/<adw_id>/<agent_name>/img/property_header/02_property_header_detail.png",
    "<absolute path>/agents/<adw_id>/<agent_name>/img/property_header/03_location_with_map_pin.png",
    "<absolute path>/agents/<adw_id>/<agent_name>/img/property_header/04_mobile_view.png",
    "<absolute path>/agents/<adw_id>/<agent_name>/img/property_header/05_desktop_view.png"
  ],
  "error": null
}
```
