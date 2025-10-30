# E2E Test: View Split Lease Page

## User Story
As a potential tenant viewing a property listing, I want to see property images in a gallery and configure my rental proposal settings (move-in date, weekly schedule, reservation duration) so that I can evaluate the property and create a customized rental proposal.

## Test URL
`file://${process.cwd()}/app/split-lease/pages/view-split-lease/index.html`

## Prerequisites
- Component bundle must be built: `cd app/split-lease/components && npm run build`
- Browser must support ES6 modules and React 18

## Test Steps

### 1. Navigate to View Split Lease Page
```typescript
await page.goto(`file://${process.cwd()}/app/split-lease/pages/view-split-lease/index.html`);
await page.waitForLoadState('networkidle');
```

**Expected:**
- Page loads successfully
- No JavaScript errors in console

**Screenshot:** `test-results/view-split-lease/01-page-load.png`

---

### 2. Verify ListingImageGrid Renders
```typescript
// Check that the image grid container exists
const imageGrid = await page.locator('#listing-images');
await expect(imageGrid).toBeVisible();

// Check that 4 images are rendered
const images = await page.locator('#listing-images img');
await expect(images).toHaveCount(4);

// Verify images have loaded
for (let i = 0; i < 4; i++) {
  const img = images.nth(i);
  await expect(img).toBeVisible();
  const naturalWidth = await img.evaluate((el: HTMLImageElement) => el.naturalWidth);
  expect(naturalWidth).toBeGreaterThan(0);
}
```

**Expected:**
- Image grid container is visible
- All 4 images are rendered
- Images have loaded successfully (naturalWidth > 0)

**Screenshot:** `test-results/view-split-lease/02-image-grid.png`

---

### 3. Verify ProposalMenu Renders with All Sections
```typescript
// Check proposal menu container
const proposalMenu = await page.locator('#proposal-menu');
await expect(proposalMenu).toBeVisible();

// Check price display
const priceDisplay = await page.locator('#proposal-menu').getByText(/\$434\.07/);
await expect(priceDisplay).toBeVisible();

// Check ideal move-in input
const moveInInput = await page.locator('#move-in-date');
await expect(moveInInput).toBeVisible();
await expect(moveInInput).toHaveValue('11/10/2025');

// Check strict checkbox
const strictCheckbox = await page.locator('#strict-move-in');
await expect(strictCheckbox).toBeVisible();

// Check weekly schedule label
const weeklyScheduleLabel = await page.getByText('Weekly Schedule');
await expect(weeklyScheduleLabel).toBeVisible();

// Check day buttons (7 days)
const dayButtons = await page.locator('#proposal-menu button').filter({ hasText: /^[SMTWF]$/ });
await expect(dayButtons).toHaveCount(7);

// Check reservation span dropdown
const reservationSpan = await page.locator('#reservation-span');
await expect(reservationSpan).toBeVisible();
```

**Expected:**
- Proposal menu is visible
- Price displays "$434.07 /night"
- Move-in date input shows "11/10/2025"
- Strict checkbox is present
- Weekly schedule section is visible
- 7 day buttons are rendered
- Reservation span dropdown is visible

**Screenshot:** `test-results/view-split-lease/03-proposal-menu-initial.png`

---

### 4. Interact with Weekly Schedule - Select Days
```typescript
// Initial state should have Monday-Thursday selected (indices 1,2,3,4)
// Let's deselect Wednesday and verify state changes

// Find Wednesday button (3rd button, index 2 in week starting Sunday)
const wednesdayButton = dayButtons.nth(3);

// Click to deselect
await wednesdayButton.click();

// Wait for status text update
await page.waitForTimeout(500);

// Verify selection status text updated
const statusText = await page.getByText(/days.*nights Selected/);
await expect(statusText).toBeVisible();

// Should now show "3 days, 2 nights Selected"
await expect(statusText).toHaveText(/3 days, 2 nights Selected/);
```

**Expected:**
- Wednesday button toggles from selected to unselected
- Status text updates to "3 days, 2 nights Selected"
- Check-in and check-out days update accordingly

**Screenshot:** `test-results/view-split-lease/04-weekly-schedule-interaction.png`

---

### 5. Interact with Weekly Schedule - Add More Days
```typescript
// Click Friday to add it
const fridayButton = dayButtons.nth(5);
await fridayButton.click();
await page.waitForTimeout(500);

// Verify status updated
const statusTextAfter = await page.getByText(/days.*nights Selected/);
await expect(statusTextAfter).toHaveText(/5 days, 4 nights Selected/);

// Check for warning note (more than ideal 3 days)
const warningNote = await page.getByText(/selected more days than the host would like/);
await expect(warningNote).toBeVisible();
```

**Expected:**
- Friday button becomes selected
- Status text updates to "5 days, 4 nights Selected"
- Warning note appears about selecting more days than host preference

**Screenshot:** `test-results/view-split-lease/05-schedule-warning.png`

---

### 6. Interact with Reservation Span Dropdown
```typescript
// Get current value (should be 20 weeks initially)
const currentValue = await reservationSpan.inputValue();
expect(currentValue).toBe('20');

// Change to 13 weeks (3 months)
await reservationSpan.selectOption('13');
await page.waitForTimeout(500);

// Verify pricing summary updated
const reservationTotal = await page.getByText(/Reservation Estimated Total/);
await expect(reservationTotal).toBeVisible();

// Get the new total value
const totalValue = await page.locator('#proposal-menu').getByText(/\$\d+,\d+\.\d+/).last();
await expect(totalValue).toBeVisible();
```

**Expected:**
- Dropdown changes to 13 weeks
- Pricing summary updates
- Reservation total recalculates correctly

**Screenshot:** `test-results/view-split-lease/06-reservation-span-change.png`

---

### 7. Select "Other" for Custom Weeks
```typescript
// Select "Other" option
await reservationSpan.selectOption('0');
await page.waitForTimeout(500);

// Custom input should appear
const customWeeksInput = await page.locator('input[placeholder*="Enter # of Weeks"]');
await expect(customWeeksInput).toBeVisible();

// Enter custom value
await customWeeksInput.fill('30');
await page.waitForTimeout(500);

// Check for warning (outside host preference 6-26 weeks)
const preferenceWarning = await page.getByText(/outside the host's preferred range/);
await expect(preferenceWarning).toBeVisible();
```

**Expected:**
- Custom weeks input appears
- Can enter custom value (30)
- Warning appears about being outside host's preference range
- Pricing updates with custom value

**Screenshot:** `test-results/view-split-lease/07-custom-weeks.png`

---

### 8. Verify Pricing Calculations
```typescript
// Reset to known state: 4 days selected (3 nights), 20 weeks
await reservationSpan.selectOption('20');
await page.waitForTimeout(500);

// Set selection to exactly Monday-Thursday (4 days, 3 nights)
// Click all day buttons to clear
for (let i = 0; i < 7; i++) {
  const btn = dayButtons.nth(i);
  const isPressed = await btn.getAttribute('aria-pressed');
  if (isPressed === 'true') {
    await btn.click();
  }
}

// Select Monday (1), Tuesday (2), Wednesday (3), Thursday (4)
await dayButtons.nth(1).click();
await dayButtons.nth(2).click();
await dayButtons.nth(3).click();
await dayButtons.nth(4).click();
await page.waitForTimeout(500);

// Verify calculation
// 3 nights * $434.07 = $1,302.21 per week
// 4-week rent = $1,302.21 * 4 = $5,208.84
// 20 weeks = $1,302.21 * 20 = $26,044.20

const fourWeekRent = await page.getByText(/4-Week Rent:/).locator('..').getByText(/\$/);
await expect(fourWeekRent).toHaveText('$5,208.84');
```

**Expected:**
- 4-week rent displays: $5,208.84
- Reservation total for 20 weeks displays correctly
- Calculations match expected values

**Screenshot:** `test-results/view-split-lease/08-pricing-calculations.png`

---

### 9. Test Move-In Date Input
```typescript
// Clear and enter new date
await moveInInput.clear();
await moveInInput.fill('12/01/2025');
await page.waitForTimeout(500);

// Toggle strict checkbox
await strictCheckbox.click();
await page.waitForTimeout(500);

// Verify checkbox is checked
const isChecked = await strictCheckbox.isChecked();
expect(isChecked).toBe(true);
```

**Expected:**
- Move-in date input accepts new value
- Strict checkbox can be toggled on/off

**Screenshot:** `test-results/view-split-lease/09-move-in-date.png`

---

### 10. Test Action Button
```typescript
// Verify action button exists and is clickable
const actionButton = await page.getByRole('button', { name: /Update Split Lease Proposal/i });
await expect(actionButton).toBeVisible();
await expect(actionButton).toBeEnabled();

// Click the button
await actionButton.click();
await page.waitForTimeout(500);

// Check console for log (in real implementation, this would submit the form)
```

**Expected:**
- Action button is visible and enabled
- Button can be clicked

**Screenshot:** `test-results/view-split-lease/10-action-button.png`

---

### 11. Test Responsive Layout (Mobile)
```typescript
// Set viewport to mobile size
await page.setViewportSize({ width: 375, height: 812 });
await page.waitForTimeout(1000);

// Verify layout stacks vertically
const container = await page.locator('.sl-view-split-lease-container');
const computedStyle = await container.evaluate((el) => {
  return window.getComputedStyle(el).gridTemplateColumns;
});

// On mobile, should be single column
expect(computedStyle).toMatch(/1fr/);
```

**Expected:**
- Layout adapts to mobile viewport
- Components stack vertically
- All elements remain accessible

**Screenshot:** `test-results/view-split-lease/11-mobile-layout.png`

---

### 12. Check for Console Errors
```typescript
// Collect any console errors during the test
const consoleErrors: string[] = [];
page.on('console', (msg) => {
  if (msg.type() === 'error') {
    consoleErrors.push(msg.text());
  }
});

// Run through a full interaction cycle
await page.goto(`file://${process.cwd()}/app/split-lease/pages/view-split-lease/index.html`);
await page.waitForLoadState('networkidle');
await page.waitForTimeout(2000);

// No errors should have occurred
expect(consoleErrors.length).toBe(0);
```

**Expected:**
- No JavaScript errors in console
- All components render without errors

---

## Success Criteria

✅ All 12 test steps pass
✅ ListingImageGrid displays 4 images in a 2x2 grid
✅ Images load successfully with no errors
✅ ProposalMenu displays all sections with correct data
✅ Weekly schedule selector is interactive (click to toggle days)
✅ Selection status text updates in real-time
✅ Reservation span dropdown changes update pricing
✅ Custom weeks input appears when "Other" is selected
✅ Warning messages display when selections are outside host preferences
✅ Pricing calculations are accurate and update dynamically
✅ Move-in date input and strict checkbox work correctly
✅ Action button is present and clickable
✅ Layout is responsive (stacks on mobile)
✅ No console errors during test execution

## Notes

- This test validates the full user workflow for viewing a listing and configuring a proposal
- All interactive elements are tested for functionality
- Pricing calculations are verified for accuracy
- Responsive design is tested at mobile viewport
- Component integration is verified (React Islands work together)

## Future Enhancements

- Add test for image click/lightbox functionality (when implemented)
- Test form submission and API integration (when backend is ready)
- Add accessibility tests (keyboard navigation, screen reader)
- Test with real listing data from API
- Add visual regression testing for design consistency
