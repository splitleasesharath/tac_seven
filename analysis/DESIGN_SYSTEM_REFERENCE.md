# Production Design System Reference

## Key Findings from Production Analysis

### Color Palette
**Primary Colors:**
- Primary Purple: `rgb(97, 53, 205)` / `#6135cd` - Used for primary buttons
- Dark Purple: `rgb(49, 19, 93)` / `#31135d` - Used for text and icons
- Light Purple: `rgb(140, 104, 238)` / `#8c68ee`
- Very Dark: `rgb(28, 28, 46)` / `#1c1c2e`
- Deep Purple: `rgb(41, 29, 84)` / `#291d54`

**Neutral Colors:**
- White: `rgb(255, 255, 255)` / `#ffffff`
- Dark Gray Text: `rgb(77, 77, 77)` / `#4d4d4d`
- Medium Gray Text: `rgb(79, 82, 76)` / `#4f524c`
- Light Gray: `rgb(192, 192, 192)` / `#c0c0c0`
- Border Gray: `rgb(196, 198, 208)` / `#c4c6d0`
- Light Border: `rgb(221, 221, 221)` / `#dddddd`
- Medium Gray: `rgb(134, 134, 134)` / `#868686`

**Accent Colors:**
- Accent Purple: `rgb(75, 71, 206)` / `#4b47ce`
- Muted Purple: `rgb(77, 72, 94)` / `#4d485e`

### Typography
**Font Families:**
- Primary: "Avenir Next LT Pro Regular"
- Fallback: Arial

**Font Sizes:**
- Small: 12px (select dropdowns, small text)
- Base: 13.3333px (default/icons)
- Medium: 14px (button text)

**Font Weights:**
- Regular: 400
- Medium: 500

### Form Controls (Selects/Dropdowns)
- **Background**: Transparent `rgba(0, 0, 0, 0)`
- **Text Color**: `rgb(79, 82, 76)` / `#4f524c`
- **Border**: None (`0px none`)
- **Border Radius**: `0px` (sharp corners)
- **Padding**: `0px 25px 0px 10px` (right padding for dropdown arrow)
- **Font Size**: `12px`
- **Height**: `30px`
- **Font Family**: "Avenir Next LT Pro Regular"

### Buttons
**Primary Button (Message):**
- **Background**: `rgb(97, 53, 205)` / `#6135cd`
- **Text Color**: `rgb(255, 255, 255)` / `#ffffff`
- **Border**: None or white
- **Border Radius**: `3px`
- **Font Size**: `14px`
- **Font Weight**: `500`

**Icon Buttons:**
- **Background**: Transparent
- **Border Radius**: `4px`
- **Font Size**: `13.3333px`
- **Font Weight**: `400`

### Spacing
- Standard border radius for buttons: 3-4px
- Select height: 30px
- Minimal padding approach for form controls

### Key Differences from Local Implementation
1. **Font**: Production uses "Avenir Next LT Pro Regular", local uses system fonts
2. **Colors**: Production has purple theme, local has blue theme
3. **Select Inputs**: Production has transparent background with no borders, local has bordered inputs
4. **Border Radius**: Production uses sharp corners (0px) for selects, minimal (3-4px) for buttons

## Recommendations for Local Updates
1. Update primary color from blue to purple (`#6135cd`)
2. Use `#4f524c` for form input text
3. Remove borders from select elements or make them more subtle
4. Use 30px height for select inputs
5. Update button styles to match purple theme
6. Consider adding "Avenir Next LT Pro" font with fallback to system sans-serif
