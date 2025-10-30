const { test, expect } = require('@playwright/test');
const path = require('path');

const config = require('../config.json');
const project = config.projects[0]; // split-lease

test.describe('PropertyHeader Contract Tests', () => {

  test('UMD bundle exposes PropertyHeader component correctly', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);

    // Wait for component to load
    await page.waitForTimeout(1000);

    // Check global exists
    const globalExists = await page.evaluate((globalName) => {
      return typeof window[globalName] !== 'undefined';
    }, project.globalName);

    expect(globalExists).toBe(true);

    // Check PropertyHeader export exists
    const propertyHeaderExists = await page.evaluate((globalName) => {
      return typeof window[globalName].PropertyHeader === 'function';
    }, project.globalName);

    expect(propertyHeaderExists).toBe(true);
  });

  test('PropertyHeader component renders without errors', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');

    const errors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') {
        errors.push(msg.text());
      }
    });

    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(2000);

    // Check for property-header element
    const propertyHeaderExists = await page.locator('.property-header').count();
    expect(propertyHeaderExists).toBeGreaterThan(0);

    // Check no console errors
    expect(errors).toEqual([]);
  });

  test('PropertyHeader displays title correctly', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Check for title element
    const title = await page.locator('.property-title').textContent();
    expect(title).toBe('Holiday Rental: Luxurious, Sunny, and Quiet Apt on Central Park West');

    // Verify it's an h1 element
    const isH1 = await page.locator('h1.property-title').count();
    expect(isH1).toBe(1);
  });

  test('PropertyHeader displays location with icon', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Check location section exists
    const locationSection = await page.locator('.property-location').count();
    expect(locationSection).toBe(1);

    // Check location text
    const locationText = await page.locator('.location-text').textContent();
    expect(locationText).toContain('Manhattan Valley');
    expect(locationText).toContain('Manhattan');
    expect(locationText).toContain('Located in');

    // Check map pin icon exists
    const mapPinIcon = await page.locator('.map-pin-icon').count();
    expect(mapPinIcon).toBe(1);
  });

  test('PropertyHeader displays property details', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Check property details element
    const detailsText = await page.locator('.property-details').textContent();
    expect(detailsText).toContain('Private Room');
    expect(detailsText).toContain('2 guests max');
  });

  test('PropertyHeader accepts props correctly', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Test with different props
    await page.evaluate((globalName) => {
      const PropertyHeader = window[globalName].PropertyHeader;
      const rootEl = document.getElementById('property-header-root');

      const testProps = {
        title: 'Test Property Title',
        location: {
          neighborhood: 'Test Neighborhood',
          city: 'Test City'
        },
        propertyType: 'Entire Home',
        maxGuests: 4
      };

      const root = ReactDOM.createRoot(rootEl);
      root.render(React.createElement(PropertyHeader, testProps));
    }, project.globalName);

    await page.waitForTimeout(500);

    // Verify new props are rendered
    const title = await page.locator('.property-title').textContent();
    expect(title).toBe('Test Property Title');

    const locationText = await page.locator('.location-text').textContent();
    expect(locationText).toContain('Test Neighborhood');
    expect(locationText).toContain('Test City');

    const detailsText = await page.locator('.property-details').textContent();
    expect(detailsText).toContain('Entire Home');
    expect(detailsText).toContain('4 guests max');
  });

  test('PropertyHeader handles singular guest correctly', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Test with 1 guest
    await page.evaluate((globalName) => {
      const PropertyHeader = window[globalName].PropertyHeader;
      const rootEl = document.getElementById('property-header-root');

      const testProps = {
        title: 'Single Guest Property',
        location: {
          neighborhood: 'Brooklyn',
          city: 'New York'
        },
        propertyType: 'Private Room',
        maxGuests: 1
      };

      const root = ReactDOM.createRoot(rootEl);
      root.render(React.createElement(PropertyHeader, testProps));
    }, project.globalName);

    await page.waitForTimeout(500);

    // Verify singular "guest" not "guests"
    const detailsText = await page.locator('.property-details').textContent();
    expect(detailsText).toContain('1 guest max');
    expect(detailsText).not.toContain('1 guests max');
  });

  test('PropertyHeader has correct CSS classes', async ({ page }) => {
    const previewPath = path.join(__dirname, '../previews/property-header-preview.html');
    await page.goto(`file://${previewPath}`);
    await page.waitForTimeout(1000);

    // Check main container class
    const hasPropertyHeaderClass = await page.locator('.property-header').count();
    expect(hasPropertyHeaderClass).toBe(1);

    // Check title class
    const hasTitleClass = await page.locator('.property-title').count();
    expect(hasTitleClass).toBe(1);

    // Check location class
    const hasLocationClass = await page.locator('.property-location').count();
    expect(hasLocationClass).toBe(1);

    // Check details class
    const hasDetailsClass = await page.locator('.property-details').count();
    expect(hasDetailsClass).toBe(1);
  });

});
