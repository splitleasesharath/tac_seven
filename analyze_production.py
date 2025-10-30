"""
Playwright script to analyze production filter section for visual parity
"""
import asyncio
import json
from playwright.async_api import async_playwright
from pathlib import Path

# Create analysis directory
ANALYSIS_DIR = Path(__file__).parent / "analysis"
ANALYSIS_DIR.mkdir(exist_ok=True)

async def analyze_production():
    """Analyze production page filter section structure and styles"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()

        print("Step 1: Navigating to production page...")
        try:
            await page.goto('https://app.split.lease/search', timeout=60000)
            await page.wait_for_timeout(5000)  # Wait 5 seconds for page to settle
        except Exception as e:
            print(f"Navigation warning: {e}")
            print("Continuing with analysis...")

        # Take full page screenshot
        print("Taking full page screenshot...")
        await page.screenshot(path=ANALYSIS_DIR / 'production_full_page.png', full_page=True)

        # Try to identify filter section
        print("\nStep 2: Analyzing filter section structure...")

        # Common selectors for filter sections
        filter_selectors = [
            '.filters',
            '.filter-section',
            '.search-filters',
            'aside',
            '[class*="filter"]',
            '[class*="sidebar"]',
            'form'
        ]

        filter_element = None
        filter_selector_used = None

        for selector in filter_selectors:
            try:
                element = await page.query_selector(selector)
                if element:
                    filter_element = element
                    filter_selector_used = selector
                    print(f"Found filter section with selector: {selector}")
                    break
            except:
                continue

        if filter_element:
            # Take screenshot of filter section
            print("Taking filter section screenshot...")
            await filter_element.screenshot(path=ANALYSIS_DIR / 'production_filter_section.png')

            # Extract HTML structure
            print("\nStep 3: Extracting HTML structure...")
            html_structure = await page.evaluate(f'''
                () => {{
                    const element = document.querySelector('{filter_selector_used}');
                    return element ? element.outerHTML : null;
                }}
            ''')

            if html_structure:
                with open(ANALYSIS_DIR / 'production_filter_html.html', 'w', encoding='utf-8') as f:
                    f.write(html_structure)
                print(f"Saved HTML structure ({len(html_structure)} chars)")

            # Extract computed styles
            print("\nStep 4: Extracting computed CSS styles...")

            # Extract styles for container
            container_styles = await page.evaluate(f'''
                () => {{
                    const element = document.querySelector('{filter_selector_used}');
                    if (!element) return null;

                    const computed = window.getComputedStyle(element);
                    return {{
                        // Box model
                        display: computed.display,
                        position: computed.position,
                        width: computed.width,
                        height: computed.height,
                        padding: computed.padding,
                        margin: computed.margin,

                        // Colors
                        backgroundColor: computed.backgroundColor,
                        color: computed.color,

                        // Borders
                        border: computed.border,
                        borderRadius: computed.borderRadius,
                        borderColor: computed.borderColor,
                        borderWidth: computed.borderWidth,

                        // Effects
                        boxShadow: computed.boxShadow,

                        // Typography
                        fontFamily: computed.fontFamily,
                        fontSize: computed.fontSize,
                        fontWeight: computed.fontWeight,
                        lineHeight: computed.lineHeight,

                        // Spacing
                        gap: computed.gap,
                        rowGap: computed.rowGap,
                        columnGap: computed.columnGap
                    }};
                }}
            ''')

            # Extract all interactive elements and their styles
            interactive_styles = await page.evaluate(f'''
                () => {{
                    const container = document.querySelector('{filter_selector_used}');
                    if (!container) return null;

                    const results = {{
                        headings: [],
                        inputs: [],
                        buttons: [],
                        checkboxes: [],
                        labels: []
                    }};

                    // Headings
                    container.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(el => {{
                        const computed = window.getComputedStyle(el);
                        results.headings.push({{
                            tag: el.tagName,
                            text: el.textContent.trim().substring(0, 50),
                            fontFamily: computed.fontFamily,
                            fontSize: computed.fontSize,
                            fontWeight: computed.fontWeight,
                            color: computed.color,
                            lineHeight: computed.lineHeight,
                            marginBottom: computed.marginBottom
                        }});
                    }});

                    // Input fields
                    container.querySelectorAll('input[type="text"], input[type="number"], input[type="search"]').forEach(el => {{
                        const computed = window.getComputedStyle(el);
                        results.inputs.push({{
                            type: el.type,
                            placeholder: el.placeholder,
                            border: computed.border,
                            borderRadius: computed.borderRadius,
                            padding: computed.padding,
                            fontSize: computed.fontSize,
                            backgroundColor: computed.backgroundColor,
                            color: computed.color,
                            height: computed.height
                        }});
                    }});

                    // Buttons
                    container.querySelectorAll('button, input[type="submit"]').forEach(el => {{
                        const computed = window.getComputedStyle(el);
                        results.buttons.push({{
                            text: el.textContent.trim().substring(0, 30),
                            backgroundColor: computed.backgroundColor,
                            color: computed.color,
                            border: computed.border,
                            borderRadius: computed.borderRadius,
                            padding: computed.padding,
                            fontSize: computed.fontSize,
                            fontWeight: computed.fontWeight
                        }});
                    }});

                    // Checkboxes
                    container.querySelectorAll('input[type="checkbox"]').forEach(el => {{
                        const computed = window.getComputedStyle(el);
                        results.checkboxes.push({{
                            width: computed.width,
                            height: computed.height,
                            border: computed.border,
                            borderRadius: computed.borderRadius
                        }});
                    }});

                    // Labels
                    container.querySelectorAll('label').forEach(el => {{
                        const computed = window.getComputedStyle(el);
                        results.labels.push({{
                            text: el.textContent.trim().substring(0, 50),
                            fontSize: computed.fontSize,
                            fontWeight: computed.fontWeight,
                            color: computed.color
                        }});
                    }});

                    return results;
                }}
            ''')

            # Save all extracted styles
            styles_data = {
                'container': container_styles,
                'interactive_elements': interactive_styles
            }

            with open(ANALYSIS_DIR / 'production_styles.json', 'w', encoding='utf-8') as f:
                json.dump(styles_data, f, indent=2)

            print(f"Saved computed styles")
            print(f"  - {len(interactive_styles.get('headings', []))} headings")
            print(f"  - {len(interactive_styles.get('inputs', []))} input fields")
            print(f"  - {len(interactive_styles.get('buttons', []))} buttons")
            print(f"  - {len(interactive_styles.get('checkboxes', []))} checkboxes")
            print(f"  - {len(interactive_styles.get('labels', []))} labels")

        else:
            print("WARNING: Could not find filter section on production page!")
            print("Taking full page screenshot for manual inspection...")
            await page.screenshot(path=ANALYSIS_DIR / 'production_page_for_inspection.png')

        # Now analyze local page
        print("\n" + "="*60)
        print("Step 5: Analyzing local page...")
        print("="*60)

        local_page = await context.new_page()
        try:
            await local_page.goto('http://localhost:9212/search/', timeout=60000)
            await local_page.wait_for_timeout(2000)  # Wait 2 seconds for page to settle
        except Exception as e:
            print(f"Local navigation warning: {e}")
            print("Continuing with analysis...")

        # Take full page screenshot
        print("Taking local full page screenshot...")
        await local_page.screenshot(path=ANALYSIS_DIR / 'local_full_page.png', full_page=True)

        # Find filter section on local page
        local_filter = None
        local_selector = None

        for selector in filter_selectors:
            try:
                element = await local_page.query_selector(selector)
                if element:
                    local_filter = element
                    local_selector = selector
                    print(f"Found local filter section with selector: {selector}")
                    break
            except:
                continue

        if local_filter:
            # Take screenshot of local filter section
            print("Taking local filter section screenshot...")
            await local_filter.screenshot(path=ANALYSIS_DIR / 'local_filter_section.png')

            # Extract HTML structure
            local_html = await local_page.evaluate(f'''
                () => {{
                    const element = document.querySelector('{local_selector}');
                    return element ? element.outerHTML : null;
                }}
            ''')

            if local_html:
                with open(ANALYSIS_DIR / 'local_filter_html.html', 'w', encoding='utf-8') as f:
                    f.write(local_html)
                print(f"Saved local HTML structure ({len(local_html)} chars)")

        print("\n" + "="*60)
        print("Analysis complete! Files saved to:", ANALYSIS_DIR)
        print("="*60)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(analyze_production())
