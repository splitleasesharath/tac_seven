const playwright = require('playwright');
const path = require('path');

async function captureScreenshots() {
  const browser = await playwright.chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const baseDir = path.resolve(__dirname, 'agents/85cf2f02/reviewer/review_img');
  const url = 'http://localhost:9214/pages/view-split-lease/index.html';

  // Log console messages
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.error('PAGE ERROR:', err));

  console.log(`Navigating to ${url}...`);
  await page.goto(url, { waitUntil: 'networkidle' });

  // Wait for React components to mount
  console.log('Waiting for components to mount...');
  await page.waitForTimeout(3000);

  // Check what's on the page
  const content = await page.content();
  console.log('Page loaded, checking for PropertyHeader...');

  // 1. Full page screenshot (desktop)
  console.log('Capturing desktop full page view...');
  await page.setViewportSize({ width: 1280, height: 1024 });
  await page.waitForTimeout(500);
  await page.screenshot({
    path: path.join(baseDir, '01_desktop_full_page.png'),
    fullPage: true
  });

  // 2. PropertyHeader component close-up (if exists)
  console.log('Attempting to capture PropertyHeader...');
  try {
    const propertyHeader = page.locator('#property-header');
    const isVisible = await propertyHeader.isVisible({ timeout: 5000 });
    if (isVisible) {
      await propertyHeader.screenshot({
        path: path.join(baseDir, '02_property_header_detail.png')
      });
      console.log('PropertyHeader captured successfully');
    }
  } catch (e) {
    console.error('PropertyHeader not found or not visible:', e.message);
  }

  // 3. Try capturing the main content area
  console.log('Capturing main content area...');
  try {
    const mainContent = page.locator('.main-content');
    const isVisible = await mainContent.isVisible({ timeout: 5000 });
    if (isVisible) {
      await mainContent.screenshot({
        path: path.join(baseDir, '03_main_content.png')
      });
    }
  } catch (e) {
    console.error('Main content not found:', e.message);
  }

  // 4. Mobile viewport
  console.log('Capturing mobile view...');
  await page.setViewportSize({ width: 375, height: 812 });
  await page.waitForTimeout(500);
  await page.screenshot({
    path: path.join(baseDir, '04_mobile_full_page.png'),
    fullPage: true
  });

  console.log('All screenshots captured!');

  await browser.close();
}

captureScreenshots().catch(console.error);
