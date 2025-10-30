# Feature: Search Page Filter Updates

## Metadata
issue_number: `4`
adw_id: `abcff73b`
issue_json: `{"number":4,"title":"Search page filter","body":"adw_plan_build\n\nGet rid of the Room type filter, only focus on getting the filters to be the same as in the screenshot at: C:\\Users\\Split Lease\\splitleaseteam\\!Agent Context and Tools\\SL1\\Search lite context with additional context. Focus on the screenshots on desktop, to bring in the same set of filters in this version, also replace the current search schedule selector(weeks of the day as buttons) and replace it with the React module inside the components.\n\n"}`

## Feature Description
Update the search page filters to match the reference design screenshots. This involves removing the Room type filter, updating the filter set to match the desktop screenshots from the reference directory, and replacing the current button-based weekly schedule selector with the existing React SearchScheduleSelector component from the components library.

## User Story
As a Split Lease user searching for properties
I want to use an improved filter interface with a visual schedule selector
So that I can find properties that match my specific schedule and preferences more effectively

## Problem Statement
The current search page has a Room type filter that needs to be removed, and the filter interface doesn't match the approved design specifications. The existing button-based schedule selector is less intuitive than the React component available in the components library. Users need a more streamlined, visually appealing filter experience that matches the reference design.

## Solution Statement
Remove the Room type filter from the search page, update the remaining filters to match the reference screenshots (focusing on desktop layout), and integrate the existing SearchScheduleSelector React component from the components library to replace the button-based weekly schedule selector. This will provide a consistent, intuitive search experience that aligns with the approved design system.

## Relevant Files
Use these files to implement the feature:

- **README.md** - Contains project structure overview, Islands Architecture pattern, and component integration documentation
  - Needed to understand the Islands Architecture and how to integrate React components
  - Documents the SearchScheduleSelector component and its props
  - Shows how to mount components as islands in HTML pages

- **app/server/** - Server-side code (if filters interact with backend)
  - May need to be examined to understand filter data structure
  - Could contain API endpoints for search filtering

- **.claude/commands/test_e2e.md** - E2E test execution framework
  - Needed to understand how to create E2E tests
  - Contains test structure and screenshot requirements

- **.claude/commands/e2e/test_basic_query.md** - Example E2E test file
  - Reference for creating new E2E test structure
  - Shows test step format and verification approach

### New Files

- **.claude/commands/e2e/test_search_filters.md** - New E2E test file for validating search filter functionality
  - Will contain test steps to verify filter removal
  - Will validate SearchScheduleSelector integration
  - Will capture screenshots of updated filter interface

## Implementation Plan
### Phase 1: Foundation
- Review reference screenshots to identify exact filter requirements
- Document current search page structure and existing filters
- Identify the SearchScheduleSelector component location and props
- Examine current button-based schedule selector implementation
- Create E2E test file structure for validation

### Phase 2: Core Implementation
- Remove Room type filter from search page HTML/code
- Update remaining filters to match reference design
- Replace button-based schedule selector with SearchScheduleSelector React component
- Ensure proper styling and responsive behavior
- Integrate component using Islands Architecture pattern

### Phase 3: Integration
- Test filter interactions and data flow
- Verify SearchScheduleSelector properly communicates selected schedule
- Ensure filters work together cohesively
- Validate responsive design on desktop and mobile
- Update any server-side filter logic if necessary

## Step by Step Tasks
IMPORTANT: Execute every step in order, top to bottom.

### 1. Research and Documentation
- Read README.md to understand Islands Architecture and SearchScheduleSelector component
- Locate and examine reference screenshots at "C:\Users\Split Lease\splitleaseteam\!Agent Context and Tools\SL1\Search lite context with additional context"
- Document current search page structure by finding and reading existing search page files
- Identify current filters and Room type filter location
- Document SearchScheduleSelector component props and usage from README.md

### 2. Create E2E Test File
- Read .claude/commands/test_e2e.md to understand E2E test structure
- Read .claude/commands/e2e/test_basic_query.md as a reference example
- Create .claude/commands/e2e/test_search_filters.md with:
  - User story for search filter functionality
  - Test steps to verify Room type filter is removed
  - Test steps to verify new filter layout matches reference
  - Test steps to verify SearchScheduleSelector integration
  - Test steps to verify schedule selection functionality
  - Success criteria including all filter interactions
  - Screenshot capture points for initial state, filter interactions, and schedule selection

### 3. Locate Search Page Files
- Use Glob to find search page HTML files (pattern: **/search*.html, **/search/**/*.html)
- Use Grep to search for "Room type" or "room-type" filter references
- Use Grep to search for current schedule selector button implementation
- Identify CSS files for search page styling
- Identify JavaScript files for search page interactivity

### 4. Remove Room Type Filter
- Read the search page HTML file
- Identify and remove Room type filter HTML elements
- Remove associated CSS styling for Room type filter
- Remove any JavaScript logic related to Room type filter
- Remove Room type filter from any data models or API calls

### 5. Update Filter Layout
- Compare reference screenshots with current filter implementation
- Update filter HTML structure to match reference design
- Update filter CSS styling to match reference design
- Ensure proper spacing, typography, and visual hierarchy
- Verify responsive behavior matches reference

### 6. Replace Schedule Selector
- Locate current button-based schedule selector code
- Remove existing schedule selector HTML and JavaScript
- Add SearchScheduleSelector component mount point (div with id)
- Add component initialization script following Islands Architecture pattern:
  - Include React CDN scripts if not already present
  - Include components bundle script
  - Mount SearchScheduleSelector using ReactDOM.createRoot
  - Configure props: minDays, maxDays, requireContiguous, onSelectionChange callback
- Ensure proper styling integration with existing page styles

### 7. Integrate Component Callbacks
- Implement onSelectionChange callback to capture selected days
- Integrate selected schedule with search/filter logic
- Ensure schedule selection persists during filter interactions
- Update any search query parameters to include schedule data

### 8. Test Filter Interactions
- Manually test all remaining filters
- Test SearchScheduleSelector day selection (click, drag)
- Test filter combinations
- Test clearing filters
- Test responsive behavior on different screen sizes

### 9. Run Validation Commands
- Execute all validation commands listed in the Validation Commands section
- Read .claude/commands/test_e2e.md
- Execute .claude/commands/e2e/test_search_filters.md E2E test
- Verify all screenshots are captured correctly
- Ensure zero regressions in existing functionality

## Testing Strategy
### Unit Tests
- Test filter state management
- Test SearchScheduleSelector integration
- Test schedule data serialization for search queries
- Test filter removal (verify Room type filter is gone)

### Edge Cases
- Empty filter state (no filters selected)
- All filters selected
- Invalid schedule selections (handled by component validation)
- Mobile/tablet responsive behavior
- Browser compatibility (modern browsers)
- Component loading failures (graceful degradation)

## Acceptance Criteria
- Room type filter is completely removed from search page
- Filter layout matches reference screenshots on desktop
- SearchScheduleSelector React component is integrated using Islands Architecture
- Schedule selector allows visual day-of-week selection
- Schedule selection integrates with search/filter logic
- All filters work together without errors
- Responsive design works on desktop and mobile
- E2E test passes with all verifications successful
- Zero regressions in existing search functionality
- Component bundle loads correctly via CDN pattern
- Page maintains Islands Architecture pattern

## Validation Commands
Execute every command to validate the feature works correctly with zero regressions.

- Read .claude/commands/test_e2e.md
- Read and execute .claude/commands/e2e/test_search_filters.md to validate search filter functionality
- `cd app/server && uv run pytest` - Run server tests to validate the feature works with zero regressions (if server tests exist)
- Manually verify in browser that:
  - Room type filter is removed
  - Remaining filters match reference screenshots
  - SearchScheduleSelector component loads and renders
  - Day selection works via click and drag
  - Schedule integrates with search logic
  - Page is responsive on different screen sizes

## Notes
- The SearchScheduleSelector component is already built and documented in README.md with props: listing, onSelectionChange, onError, className, minDays, maxDays, requireContiguous, initialSelection
- Islands Architecture pattern means the component is loaded as a UMD bundle via CDN and mounted at specific DOM nodes
- Reference screenshots are located at: "C:\Users\Split Lease\splitleaseteam\!Agent Context and Tools\SL1\Search lite context with additional context"
- Focus on desktop layout as specified in the requirements
- The component already includes validation, animations (Framer Motion), and drag selection functionality
- Ensure the components bundle is built (npm run build in components/) before integration
- The SearchScheduleSelector uses styled-components and Framer Motion, which are already included in the UMD bundle
- Consider adding error handling for component loading failures
- Future enhancement: Add mobile-specific optimizations for schedule selector if needed
