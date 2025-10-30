# E2E Test: View Split Lease Page

## User Story
As a guest browsing Split Lease, I want to verify that the view-split-lease page loads correctly with header and footer React islands mounted successfully.

## Test Steps

1. Navigate to `http://localhost:8080/view-split-lease/index.html`
2. Verify the page title is "View Listing | Split Lease"
3. Verify the header React island mounts successfully (check for `#site-header` content)
4. Verify the footer React island mounts successfully (check for `#site-footer` content)
5. Verify the main content area is visible with class `.view-listing-main`
6. Verify no JavaScript console errors occur during page load
7. Capture screenshot of the full page at desktop resolution (1280x720)
8. Capture screenshot at tablet resolution (768x1024)
9. Capture screenshot at mobile resolution (375x667)

## Success Criteria

- Page loads without errors
- Page title matches "View Listing | Split Lease"
- Header island (#site-header) contains rendered React component content
- Footer island (#site-footer) contains rendered React component content
- Main content area is visible and properly styled
- No JavaScript console errors or warnings
- Screenshots show proper responsive layout at all viewport sizes

## Screenshot Outputs

- `view-split-lease-desktop.png` - Desktop view (1280x720)
- `view-split-lease-tablet.png` - Tablet view (768x1024)
- `view-split-lease-mobile.png` - Mobile view (375x667)

## Notes

This test validates the foundational Islands Architecture implementation for the view-split-lease page. Future tests will verify dynamic content loading and interactive features as they are added.
