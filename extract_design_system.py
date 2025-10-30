"""
Extract design system (colors, typography, spacing) from production
"""
import asyncio
import json
from playwright.async_api import async_playwright
from pathlib import Path

ANALYSIS_DIR = Path(__file__).parent / "analysis"
ANALYSIS_DIR.mkdir(exist_ok=True)

async def extract_design_system():
    """Extract design system from production page"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()

        print("Navigating to production page...")
        await page.goto('https://app.split.lease/search', timeout=60000)
        await page.wait_for_timeout(8000)

        print("\nExtracting design system...")

        design_system = await page.evaluate('''
            () => {
                const results = {
                    colors: {
                        backgrounds: new Set(),
                        text: new Set(),
                        borders: new Set(),
                        buttons: []
                    },
                    typography: {
                        fontFamilies: new Set(),
                        fontSizes: new Set(),
                        fontWeights: new Set()
                    },
                    spacing: {
                        padding: new Set(),
                        margin: new Set(),
                        gaps: new Set()
                    },
                    borders: {
                        borderRadius: new Set(),
                        borderWidth: new Set()
                    },
                    inputs: [],
                    labels: []
                };

                // Sample elements throughout the page
                const allElements = document.querySelectorAll('*');

                // Limit to first 500 elements for performance
                const elementsToSample = Array.from(allElements).slice(0, 500);

                elementsToSample.forEach(el => {
                    const computed = window.getComputedStyle(el);

                    // Colors
                    if (computed.backgroundColor && computed.backgroundColor !== 'rgba(0, 0, 0, 0)') {
                        results.colors.backgrounds.add(computed.backgroundColor);
                    }
                    if (computed.color) {
                        results.colors.text.add(computed.color);
                    }
                    if (computed.borderColor && computed.borderColor !== 'rgb(0, 0, 0)') {
                        results.colors.borders.add(computed.borderColor);
                    }

                    // Typography
                    if (computed.fontFamily) {
                        results.typography.fontFamilies.add(computed.fontFamily);
                    }
                    if (computed.fontSize) {
                        results.typography.fontSizes.add(computed.fontSize);
                    }
                    if (computed.fontWeight) {
                        results.typography.fontWeights.add(computed.fontWeight);
                    }

                    // Spacing
                    if (computed.padding && computed.padding !== '0px') {
                        results.spacing.padding.add(computed.padding);
                    }
                    if (computed.margin && computed.margin !== '0px') {
                        results.spacing.margin.add(computed.margin);
                    }
                    if (computed.gap && computed.gap !== 'normal' && computed.gap !== '0px') {
                        results.spacing.gaps.add(computed.gap);
                    }

                    // Borders
                    if (computed.borderRadius && computed.borderRadius !== '0px') {
                        results.borders.borderRadius.add(computed.borderRadius);
                    }
                    if (computed.borderWidth && computed.borderWidth !== '0px') {
                        results.borders.borderWidth.add(computed.borderWidth);
                    }
                });

                // Specific button styles
                document.querySelectorAll('button').forEach(btn => {
                    const computed = window.getComputedStyle(btn);
                    results.colors.buttons.push({
                        text: btn.textContent.trim().substring(0, 30),
                        backgroundColor: computed.backgroundColor,
                        color: computed.color,
                        borderColor: computed.borderColor,
                        borderRadius: computed.borderRadius,
                        padding: computed.padding,
                        fontSize: computed.fontSize,
                        fontWeight: computed.fontWeight
                    });
                });

                // Input field styles (select dropdowns)
                document.querySelectorAll('select, input').forEach(input => {
                    const computed = window.getComputedStyle(input);
                    results.inputs.push({
                        type: input.tagName + (input.type ? `[${input.type}]` : ''),
                        backgroundColor: computed.backgroundColor,
                        color: computed.color,
                        border: computed.border,
                        borderRadius: computed.borderRadius,
                        padding: computed.padding,
                        fontSize: computed.fontSize,
                        height: computed.height
                    });
                });

                // Label styles
                document.querySelectorAll('label').forEach(label => {
                    const computed = window.getComputedStyle(label);
                    results.labels.push({
                        text: label.textContent.trim().substring(0, 50),
                        color: computed.color,
                        fontSize: computed.fontSize,
                        fontWeight: computed.fontWeight,
                        fontFamily: computed.fontFamily
                    });
                });

                // Convert Sets to Arrays for JSON serialization
                return {
                    colors: {
                        backgrounds: Array.from(results.colors.backgrounds),
                        text: Array.from(results.colors.text),
                        borders: Array.from(results.colors.borders),
                        buttons: results.colors.buttons
                    },
                    typography: {
                        fontFamilies: Array.from(results.typography.fontFamilies),
                        fontSizes: Array.from(results.typography.fontSizes),
                        fontWeights: Array.from(results.typography.fontWeights)
                    },
                    spacing: {
                        padding: Array.from(results.spacing.padding),
                        margin: Array.from(results.spacing.margin),
                        gaps: Array.from(results.spacing.gaps)
                    },
                    borders: {
                        borderRadius: Array.from(results.borders.borderRadius),
                        borderWidth: Array.from(results.borders.borderWidth)
                    },
                    inputs: results.inputs,
                    labels: results.labels
                };
            }
        ''')

        # Save design system
        with open(ANALYSIS_DIR / 'production_design_system.json', 'w', encoding='utf-8') as f:
            json.dump(design_system, f, indent=2)

        print(f"\nDesign System Extracted:")
        print(f"  - {len(design_system['colors']['backgrounds'])} background colors")
        print(f"  - {len(design_system['colors']['text'])} text colors")
        print(f"  - {len(design_system['colors']['borders'])} border colors")
        print(f"  - {len(design_system['colors']['buttons'])} buttons analyzed")
        print(f"  - {len(design_system['typography']['fontFamilies'])} font families")
        print(f"  - {len(design_system['typography']['fontSizes'])} font sizes")
        print(f"  - {len(design_system['inputs'])} inputs analyzed")
        print(f"  - {len(design_system['labels'])} labels analyzed")

        # Extract specific filter panel styles if visible
        print("\nLooking for filter controls...")
        filter_controls = await page.evaluate('''
            () => {
                const selects = document.querySelectorAll('select');
                const filterInfo = [];

                selects.forEach(select => {
                    const computed = window.getComputedStyle(select);
                    const label = select.previousElementSibling;
                    const labelComputed = label ? window.getComputedStyle(label) : null;

                    filterInfo.push({
                        hasLabel: !!label,
                        labelText: label ? label.textContent.trim() : null,
                        labelStyles: labelComputed ? {
                            color: labelComputed.color,
                            fontSize: labelComputed.fontSize,
                            fontWeight: labelComputed.fontWeight
                        } : null,
                        selectStyles: {
                            backgroundColor: computed.backgroundColor,
                            color: computed.color,
                            border: computed.border,
                            borderRadius: computed.borderRadius,
                            padding: computed.padding,
                            fontSize: computed.fontSize,
                            height: computed.height,
                            fontFamily: computed.fontFamily
                        }
                    });
                });

                return filterInfo;
            }
        ''')

        with open(ANALYSIS_DIR / 'production_filter_controls.json', 'w', encoding='utf-8') as f:
            json.dump(filter_controls, f, indent=2)

        print(f"Found {len(filter_controls)} filter controls")

        print("\n" + "="*60)
        print("Design system extraction complete!")
        print("="*60)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(extract_design_system())
