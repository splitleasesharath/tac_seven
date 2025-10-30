# E2E Test: Search Page Filter Updates

Test the updated search page filters including verification that Room type filter is removed and SearchScheduleSelector component is integrated.

## User Story

As a Split Lease user searching for properties
I want to use an improved filter interface with a visual schedule selector
So that I can find properties that match my specific schedule and preferences more effectively

## Test Steps

1. Navigate to the search page at `Application URL/app/split-lease/pages/search/index.html`
2. Take a screenshot of the initial page state
3. **Verify** the page loads successfully
4. **Verify** core UI elements are present:
   - Filter sidebar on the left
   - Results list in the center
   - Map container on the right
   - Header navigation

5. **Verify** Room type filter is NOT present in the filter sidebar
6. Take a screenshot of the filter sidebar to confirm Room type filter is removed

7. **Verify** the following filters ARE present:
   - Schedule selector (React component island)
   - Price Range inputs
   - Amenities checkboxes (WiFi, Parking, Laundry, Furnished, Pet friendly)
   - Available Date inputs
   - Clear all button
   - Apply filters button

8. **Verify** SearchScheduleSelector component is rendered:
   - Component mount point exists
   - Day buttons are visible (Mon, Tue, Wed, Thu, Fri, Sat, Sun)
   - Component title "Select your preferred days" is present

9. Test schedule selector interaction:
   - Click on "Mon" day button
   - **Verify** the button becomes selected (changes color to green)
   - Take a screenshot of single day selected

10. Test schedule selector drag selection:
    - Click and hold on "Tue"
    - Drag to "Thu"
    - Release mouse
    - **Verify** Tue, Wed, Thu are selected (contiguous days)
    - Take a screenshot of multiple days selected

11. Test schedule selector validation:
    - Try to select only 1 day
    - **Verify** error message appears: "Please select at least 2 days"
    - Take a screenshot of validation error

12. Test price range filter:
    - Enter "500" in min price input
    - Enter "1500" in max price input
    - **Verify** price display updates to show $500 - $1500
    - Take a screenshot of price filter updated

13. Test amenities filter:
    - Check "WiFi" checkbox
    - Check "Parking" checkbox
    - **Verify** both checkboxes are checked
    - Take a screenshot of amenities selected

14. Test filter combination:
    - Select Wed, Thu, Fri in schedule selector
    - Set price range to 300-800
    - Check "Furnished" amenity
    - Click "Apply filters" button
    - **Verify** results list updates (results count changes)
    - Take a screenshot of filtered results

15. Test clear filters:
    - Click "Clear all" button
    - **Verify** all filters reset:
      - No days selected in schedule selector
      - Price range resets to 0-5000
      - All amenity checkboxes unchecked
      - Date inputs cleared
    - Take a screenshot of cleared filters

16. Test responsive behavior (if browser can be resized):
    - Resize browser to mobile width (375px)
    - **Verify** layout adapts responsively
    - Take a screenshot of mobile layout

## Success Criteria

- Room type filter is completely removed from search page
- SearchScheduleSelector React component loads and renders correctly
- Day selection works via click
- Drag selection works for multiple contiguous days
- Validation error appears when selecting less than 2 days
- Price range filter updates correctly
- Amenities checkboxes work correctly
- Filter combinations apply successfully
- Clear all button resets all filters
- Results update based on filter selections
- Component integrates seamlessly with Islands Architecture pattern
- At least 12 screenshots are captured showing all test steps

## Expected Console Output

The browser console should show:
- No React errors
- SearchScheduleSelector component mounted successfully
- "Selected days: [array]" when days are selected
- No missing component bundle errors
