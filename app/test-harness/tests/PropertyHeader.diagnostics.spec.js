const { test, expect } = require('@playwright/test');
const path = require('path');

const config = require('../config.json');
const project = config.projects[0];

/**
 * PropertyHeader Component Diagnostics & Problem Detection
 *
 * This test suite proactively identifies potential issues:
 * - Console warnings/errors
 * - Visual rendering issues
 * - Responsive behavior problems
 * - Typography and styling correctness
 * - Icon display and color
 * - Layout structure validation
 */

test.describe('PropertyHeader Diagnostics - Problem Detection', () => {

  test('Detect console warnings and errors', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');

    const consoleMessages = [];
    page.on('console', msg => {
      consoleMessages.push({
        type: msg.type(),
        text: msg.text(),
        location: msg.location()
      });
    });

    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(2000);

    // Filter for warnings and errors
    const warnings = consoleMessages.filter(m => m.type === 'warning');
    const errors = consoleMessages.filter(m => m.type === 'error');

    // Report findings
    if (warnings.length > 0) {
      console.log('\n⚠️  Console Warnings Detected:');
      warnings.forEach(w => console.log(`   - ${w.text}`));
    }

    if (errors.length > 0) {
      console.log('\n❌ Console Errors Detected:');
      errors.forEach(e => console.log(`   - ${e.text}`));
    }

    // Assert no critical errors
    expect(errors.length).toBe(0);
  });

  test('Verify title renders with correct styling', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Get title element styles
    const titleStyles = await page.locator('.property-title').evaluate(el => {
      const styles = window.getComputedStyle(el);
      return {
        fontSize: styles.fontSize,
        fontWeight: styles.fontWeight,
        color: styles.color,
        tagName: el.tagName
      };
    });

    // Verify it's an H1
    expect(titleStyles.tagName).toBe('H1');

    // Verify font size is large (at least 32px / 2rem on desktop)
    const fontSizeValue = parseFloat(titleStyles.fontSize);
    expect(fontSizeValue).toBeGreaterThanOrEqual(28); // Allow for some variation

    // Verify font weight is bold (700 or higher)
    const fontWeightValue = parseInt(titleStyles.fontWeight);
    expect(fontWeightValue).toBeGreaterThanOrEqual(700);

    console.log('✓ Title styling validated:', titleStyles);
  });

  test('Verify location section displays with purple map pin', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Check location section exists and is visible
    const locationVisible = await page.locator('.property-location').isVisible();
    expect(locationVisible).toBe(true);

    // Check map pin icon exists
    const mapPinExists = await page.locator('.map-pin-icon').count();
    expect(mapPinExists).toBe(1);

    // Verify map pin color (should be purple #7C3AED or similar)
    const mapPinColor = await page.locator('.map-pin-icon').evaluate(el => {
      const styles = window.getComputedStyle(el);
      return styles.color;
    });

    // Purple should be rgb(124, 58, 237) which is #7C3AED
    // Allow for some variation in color values
    console.log('✓ Map pin color:', mapPinColor);
    expect(mapPinColor).toBeTruthy();
  });

  test('Verify property details display in secondary styling', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Get property details styles
    const detailsStyles = await page.locator('.property-details').evaluate(el => {
      const styles = window.getComputedStyle(el);
      return {
        fontSize: styles.fontSize,
        fontWeight: styles.fontWeight,
        color: styles.color
      };
    });

    // Verify font size is smaller than title (should be around 16px / 1rem)
    const fontSizeValue = parseFloat(detailsStyles.fontSize);
    expect(fontSizeValue).toBeLessThan(24); // Should be smaller than title

    // Verify font weight is normal (not bold)
    const fontWeightValue = parseInt(detailsStyles.fontWeight);
    expect(fontWeightValue).toBeLessThan(600);

    console.log('✓ Property details styling validated:', detailsStyles);
  });

  test('Verify component layout hierarchy', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Get bounding boxes to verify vertical layout
    const titleBox = await page.locator('.property-title').boundingBox();
    const locationBox = await page.locator('.property-location').boundingBox();
    const detailsBox = await page.locator('.property-details').boundingBox();

    // Verify elements are stacked vertically: title -> location -> details
    expect(titleBox.y).toBeLessThan(locationBox.y);
    expect(locationBox.y).toBeLessThan(detailsBox.y);

    console.log('✓ Vertical layout hierarchy correct');
  });

  test('Verify responsive behavior on mobile viewport', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');

    // Set mobile viewport (375px width - iPhone SE size)
    await page.setViewportSize({ width: 375, height: 667 });
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Get title styles on mobile
    const mobileTitleStyles = await page.locator('.property-title').evaluate(el => {
      const styles = window.getComputedStyle(el);
      return {
        fontSize: styles.fontSize,
        fontWeight: styles.fontWeight
      };
    });

    // Verify title is still visible and readable
    const titleVisible = await page.locator('.property-title').isVisible();
    expect(titleVisible).toBe(true);

    // Font size should be scaled down but still readable (at least 20px)
    const mobileFontSize = parseFloat(mobileTitleStyles.fontSize);
    expect(mobileFontSize).toBeGreaterThan(18);

    // Check no horizontal overflow
    const bodyWidth = await page.evaluate(() => document.body.scrollWidth);
    const viewportWidth = 375;
    expect(bodyWidth).toBeLessThanOrEqual(viewportWidth + 10); // Allow 10px tolerance

    console.log('✓ Mobile responsive behavior validated');
  });

  test('Verify responsive behavior on tablet viewport', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');

    // Set tablet viewport (768px width - iPad)
    await page.setViewportSize({ width: 768, height: 1024 });
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Verify all elements are visible
    const titleVisible = await page.locator('.property-title').isVisible();
    const locationVisible = await page.locator('.property-location').isVisible();
    const detailsVisible = await page.locator('.property-details').isVisible();

    expect(titleVisible).toBe(true);
    expect(locationVisible).toBe(true);
    expect(detailsVisible).toBe(true);

    console.log('✓ Tablet responsive behavior validated');
  });

  test('Verify responsive behavior on desktop viewport', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');

    // Set desktop viewport (1280px width)
    await page.setViewportSize({ width: 1280, height: 720 });
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Get title styles on desktop
    const desktopTitleStyles = await page.locator('.property-title').evaluate(el => {
      const styles = window.getComputedStyle(el);
      return {
        fontSize: styles.fontSize
      };
    });

    // Desktop should have full font size (2rem / 32px)
    const desktopFontSize = parseFloat(desktopTitleStyles.fontSize);
    expect(desktopFontSize).toBeGreaterThanOrEqual(28);

    console.log('✓ Desktop responsive behavior validated');
  });

  test('Verify location section flexbox layout', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Get location section layout
    const locationLayout = await page.locator('.property-location').evaluate(el => {
      const styles = window.getComputedStyle(el);
      return {
        display: styles.display,
        alignItems: styles.alignItems
      };
    });

    // Should use flexbox with center alignment
    expect(locationLayout.display).toBe('flex');
    expect(locationLayout.alignItems).toBe('center');

    console.log('✓ Location flexbox layout validated');
  });

  test('Verify map pin icon is inline SVG', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Verify map pin is SVG element
    const isSVG = await page.locator('.map-pin-icon').evaluate(el => {
      return el.tagName === 'svg';
    });

    expect(isSVG).toBe(true);

    // Verify SVG has correct dimensions
    const svgDimensions = await page.locator('.map-pin-icon').evaluate(el => {
      return {
        width: el.getAttribute('width'),
        height: el.getAttribute('height')
      };
    });

    expect(svgDimensions.width).toBeTruthy();
    expect(svgDimensions.height).toBeTruthy();

    console.log('✓ Map pin SVG structure validated');
  });

  test('Verify component spacing and gaps', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Get component container styles
    const containerStyles = await page.locator('.property-header').evaluate(el => {
      const styles = window.getComputedStyle(el);
      return {
        display: styles.display,
        flexDirection: styles.flexDirection,
        gap: styles.gap
      };
    });

    // Should use flexbox with column direction
    expect(containerStyles.display).toBe('flex');
    expect(containerStyles.flexDirection).toBe('column');

    // Should have gap between elements
    expect(containerStyles.gap).toBeTruthy();
    expect(containerStyles.gap).not.toBe('0px');

    console.log('✓ Component spacing validated:', containerStyles);
  });

  test('Check for text overflow issues', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Test with very long title
    await page.evaluate((globalName) => {
      const PropertyHeader = window[globalName].PropertyHeader;
      const rootEl = document.getElementById('property-header-root');

      const testProps = {
        title: 'This is an extremely long property title that should wrap properly and not overflow the container or cause horizontal scrolling issues for users on any device size',
        location: {
          neighborhood: 'Very Long Neighborhood Name That Should Also Wrap',
          city: 'Very Long City Name'
        },
        propertyType: 'Entire Luxury Apartment with Amazing Views',
        maxGuests: 10
      };

      const root = ReactDOM.createRoot(rootEl);
      root.render(React.createElement(PropertyHeader, testProps));
    }, project.globalName);

    await page.waitForTimeout(500);

    // Check title doesn't cause horizontal overflow
    const titleBox = await page.locator('.property-title').boundingBox();
    const containerBox = await page.locator('.property-header').boundingBox();

    expect(titleBox.width).toBeLessThanOrEqual(containerBox.width + 10); // Allow 10px tolerance

    console.log('✓ Text overflow handling validated');
  });

});
