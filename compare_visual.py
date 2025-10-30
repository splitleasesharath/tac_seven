"""
Visual comparison script
"""
import asyncio
from playwright.async_api import async_playwright
from pathlib import Path

ANALYSIS_DIR = Path(__file__).parent / "analysis"
ANALYSIS_DIR.mkdir(exist_ok=True)

async def compare_visual():
    """Compare local and production visually"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})

        # Take screenshot of local page
        print("Capturing local page...")
        local_page = await context.new_page()
        await local_page.goto('http://localhost:9212/search/', timeout=60000)
        await local_page.wait_for_timeout(2000)
        await local_page.screenshot(path=ANALYSIS_DIR / 'local_after_updates.png', full_page=True)

        # Try to screenshot just the filter section
        try:
            filter_section = await local_page.query_selector('.filter-section')
            if filter_section:
                await filter_section.screenshot(path=ANALYSIS_DIR / 'local_filter_after_updates.png')
                print("Local filter section captured")
        except Exception as e:
            print(f"Could not capture filter section: {e}")

        # Take screenshot of production page
        print("Capturing production page...")
        prod_page = await context.new_page()
        await prod_page.goto('https://app.split.lease/search', timeout=60000)
        await prod_page.wait_for_timeout(8000)
        await prod_page.screenshot(path=ANALYSIS_DIR / 'production_after_comparison.png', full_page=True)

        print("\n" + "="*60)
        print("Visual comparison screenshots captured!")
        print("Check analysis/ directory:")
        print("  - local_after_updates.png")
        print("  - local_filter_after_updates.png")
        print("  - production_after_comparison.png")
        print("="*60)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(compare_visual())
