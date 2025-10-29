# E2E Test: Search Filter Section Visual Alignment

Test that the search page filter section visually aligns with the production page at app.split.lease/search.

## User Story

As a user
I want the search filter section to match the production design
So that I have a consistent and familiar user experience

## Test Steps

1. Navigate to the local search page at `Application URL/search`
2. Take a screenshot of the initial page state
3. **Verify** the filter section is visible and properly rendered
4. **Verify** core filter UI elements are present:
   - Filter header with "Filters" title
   - "Clear all" button
   - Location search input
   - Price range inputs (min and max)
   - Schedule checkboxes (Weekdays, Weekends, Custom Schedule)
   - Property type checkboxes (Apartment, House, Condo, Townhouse)
   - Bedroom option buttons (Studio, 1, 2, 3, 4+)
   - Bathroom option buttons (1, 1.5, 2, 2.5, 3+)
   - Amenities checkboxes (Parking, Laundry, Gym, Pool, Pet Friendly, Doorman)
   - "Apply Filters" button

5. Take a focused screenshot of the filter section
6. **Verify** filter section styling:
   - Filter section has white background
   - Filter section has right border
   - Filter groups are properly separated
   - Input fields have proper borders and border-radius
   - Buttons have proper styling and hover states

7. Navigate to production page: https://app.split.lease/search
8. Take a screenshot of the production page
9. Take a focused screenshot of the production filter section
10. **Verify** key visual elements match between local and production:
    - Similar layout structure
    - Similar spacing and padding
    - Similar typography
    - Similar color scheme
    - Similar interactive elements

11. Test filter interactions on local page:
    - Click a bedroom option button
    - **Verify** button shows active state
    - Check an amenity checkbox
    - **Verify** checkbox is checked
    - Enter text in location input
    - **Verify** text appears in input

12. Click "Apply Filters" button
13. **Verify** button click is registered (check console or visual feedback)
14. Take final screenshot of the filter section with active states

## Success Criteria

- Filter section is visible and properly positioned on the left side
- All filter groups are present and properly structured
- Filter inputs and controls are functional
- Visual styling matches modern web standards
- Interactive elements respond to user input
- Layout is responsive and well-organized
- Minimum 5 screenshots are captured:
  1. Initial local page state
  2. Local filter section detail
  3. Production page state
  4. Production filter section detail
  5. Local filter section with active states

## Expected Behavior

- Filter section should be a left sidebar with white background
- All filter groups should be clearly separated with visual hierarchy
- Input fields should have focus states
- Buttons should have hover and active states
- Checkboxes should toggle on click
- Option buttons should show active state when clicked
- "Clear all" button should reset all filters
- "Apply Filters" button should trigger filter application

## Notes

- This test validates the visual structure and basic functionality of the filter section
- Due to Playwright MCP limitations, manual visual comparison may be required
- Focus is exclusively on the filter section, not the results area
- The filter section should follow modern UI/UX best practices for search interfaces
