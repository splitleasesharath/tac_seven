"""
Enhanced Playwright script to analyze production page structure
"""
import asyncio
import json
from playwright.async_api import async_playwright
from pathlib import Path

# Create analysis directory
ANALYSIS_DIR = Path(__file__).parent / "analysis"
ANALYSIS_DIR.mkdir(exist_ok=True)

async def analyze_production_detailed():
    """Detailed analysis of production page to find filter section"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()

        print("Navigating to production page...")
        try:
            await page.goto('https://app.split.lease/search', timeout=60000)
            await page.wait_for_timeout(8000)  # Wait 8 seconds for page to fully load
        except Exception as e:
            print(f"Navigation warning: {e}")

        # Get all elements on the page with their structure
        print("\nAnalyzing page structure...")
        page_structure = await page.evaluate('''
            () => {
                function analyzeElement(element, depth = 0, maxDepth = 5) {
                    if (depth > maxDepth) return null;

                    const info = {
                        tag: element.tagName,
                        id: element.id || null,
                        classes: Array.from(element.classList),
                        text: element.textContent ? element.textContent.trim().substring(0, 100) : '',
                        childCount: element.children.length,
                        children: []
                    };

                    // Only analyze first few children to avoid massive data
                    const childrenToAnalyze = Math.min(element.children.length, 10);
                    for (let i = 0; i < childrenToAnalyze; i++) {
                        const childInfo = analyzeElement(element.children[i], depth + 1, maxDepth);
                        if (childInfo) info.children.push(childInfo);
                    }

                    return info;
                }

                return analyzeElement(document.body);
            }
        ''')

        # Save page structure
        with open(ANALYSIS_DIR / 'production_page_structure.json', 'w', encoding='utf-8') as f:
            json.dump(page_structure, f, indent=2)
        print(f"Saved page structure to production_page_structure.json")

        # Look for the left sidebar that contains property listings
        print("\nLooking for left sidebar...")
        sidebar_info = await page.evaluate('''
            () => {
                // Look for common sidebar patterns
                const selectors = [
                    'aside',
                    '[class*="sidebar"]',
                    '[class*="filter"]',
                    '[role="complementary"]',
                    'div[class*="left"]',
                    'div[class*="panel"]',
                    '.MuiDrawer-root',
                    '[data-testid*="sidebar"]',
                    '[data-testid*="filter"]'
                ];

                for (const selector of selectors) {
                    const elements = document.querySelectorAll(selector);
                    if (elements.length > 0) {
                        return {
                            selector: selector,
                            count: elements.length,
                            firstElementClasses: Array.from(elements[0].classList),
                            firstElementId: elements[0].id || null,
                            outerHTML: elements[0].outerHTML.substring(0, 500)
                        };
                    }
                }

                // If no sidebar found, look for the main container structure
                const body = document.body;
                return {
                    selector: 'body > *',
                    bodyChildrenCount: body.children.length,
                    bodyChildren: Array.from(body.children).map(child => ({
                        tag: child.tagName,
                        id: child.id || null,
                        classes: Array.from(child.classList),
                        childCount: child.children.length
                    }))
                };
            }
        ''')

        print("Sidebar info:", json.dumps(sidebar_info, indent=2))

        with open(ANALYSIS_DIR / 'production_sidebar_info.json', 'w', encoding='utf-8') as f:
            json.dump(sidebar_info, f, indent=2)

        # Extract all visible text elements that might be filter labels
        print("\nExtracting filter-like text...")
        filter_text = await page.evaluate('''
            () => {
                const labels = Array.from(document.querySelectorAll('label'));
                const headings = Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6'));
                const buttons = Array.from(document.querySelectorAll('button'));

                return {
                    labels: labels.slice(0, 20).map(l => ({
                        text: l.textContent.trim(),
                        for: l.getAttribute('for'),
                        classes: Array.from(l.classList)
                    })),
                    headings: headings.slice(0, 20).map(h => ({
                        tag: h.tagName,
                        text: h.textContent.trim(),
                        classes: Array.from(h.classList)
                    })),
                    buttons: buttons.slice(0, 20).map(b => ({
                        text: b.textContent.trim(),
                        classes: Array.from(b.classList)
                    }))
                };
            }
        ''')

        print(f"Found {len(filter_text.get('labels', []))} labels")
        print(f"Found {len(filter_text.get('headings', []))} headings")
        print(f"Found {len(filter_text.get('buttons', []))} buttons")

        with open(ANALYSIS_DIR / 'production_filter_text.json', 'w', encoding='utf-8') as f:
            json.dump(filter_text, f, indent=2)

        # Take screenshot with element highlighting
        print("\nTaking annotated screenshot...")
        await page.screenshot(path=ANALYSIS_DIR / 'production_detailed.png', full_page=True)

        print("\n" + "="*60)
        print("Detailed analysis complete! Check analysis/ directory")
        print("="*60)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(analyze_production_detailed())
