# Split Lease Search Page - Filter Section

This directory contains the Split Lease search page implementation with a comprehensive filter section.

## Structure

```
app/split-lease/
├── pages/
│   ├── search/
│   │   ├── index.html          # Main search page with filter section
│   │   ├── css/
│   │   │   ├── search.css      # Search page layout styles
│   │   │   └── filters.css     # Filter section specific styles
│   │   └── js/
│   │       └── search.js       # Filter interaction logic
│   └── shared/
│       ├── css/
│       │   └── common.css      # Shared CSS utilities
│       └── js/
│           └── common.js       # Shared JavaScript utilities
├── serve.py                    # Development server
└── validate_structure.py       # HTML structure validation script
```

## Filter Section Features

The filter section includes:

1. **Location Filter** - Text input for city/neighborhood search
2. **Price Range** - Min/max price inputs
3. **Schedule Options** - Checkboxes for Weekdays, Weekends, Custom
4. **Property Types** - Checkboxes for Apartment, House, Condo, Townhouse
5. **Bedrooms** - Selectable buttons (Studio, 1, 2, 3, 4+)
6. **Bathrooms** - Selectable buttons (1, 1.5, 2, 2.5, 3+)
7. **Amenities** - Checkboxes for Parking, Laundry, Gym, Pool, Pet Friendly, Doorman
8. **Clear All** - Reset all filters
9. **Apply Filters** - Submit filter selections

## Running the Development Server

Start the server on port 9212 (configured in .ports.env):

```bash
cd app/split-lease
python serve.py
```

The search page will be available at:
- http://localhost:9212/search/

## Validation

Validate the HTML structure:

```bash
cd app/split-lease
python validate_structure.py
```

This checks that all required filter elements are present and properly structured.

## Design Specifications

### Layout
- **Filter Section**: Left sidebar, 320px wide, sticky positioning
- **Results Section**: Right side, flexible width

### Color Palette
- Primary Blue: `#0066cc`
- Background: `#ffffff` (filter section), `#fafafa` (results area)
- Text: `#1a1a1a` (headings), `#333333` (body), `#666666` (secondary)
- Borders: `#d0d0d0` (inputs), `#e0e0e0` (section), `#f0f0f0` (dividers)

### Typography
- Headings: 600 weight
- Body: 400-500 weight
- Font Stack: System fonts (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, etc.)

### Interactive States
- **Hover**: Border changes to primary blue, background tint
- **Focus**: Border color changes, subtle box shadow
- **Active**: Scale transform, darker background
- **Selected**: Primary blue background with white text

### Spacing
- Section padding: 24px 20px
- Filter group margin: 28px bottom
- Input padding: 10px 12px
- Border radius: 6px (inputs), 8px (buttons)

## CSS Organization

### filters.css
Contains all filter-specific styling:
- Filter section layout
- Filter groups and titles
- Input fields and controls
- Checkbox and button styles
- Interactive states
- Responsive breakpoints

### search.css
Contains page layout:
- Container flex layout
- Results section styling
- Grid layout for results
- Page-level responsive design

### common.css
Contains shared utilities:
- CSS reset
- Base typography
- Form element defaults
- Utility classes

## JavaScript Functionality

### search.js
- Filter initialization
- Clear all filters
- Apply filters
- Collect filter values
- Update results count
- Handle interactive states

### common.js
- Currency formatting utility
- Debounce utility for inputs

## Responsive Design

Mobile breakpoint at 768px:
- Filter section becomes full-width
- Stacks above results section
- Adjusts padding and spacing
- Single-column results grid

## Browser Support

- Modern browsers with ES2020 support
- CSS Grid and Flexbox required
- Supports system fonts
- Accessible via keyboard navigation

## Accessibility

- Semantic HTML5 elements
- ARIA labels on inputs
- Focus states for keyboard navigation
- Proper label associations
- Color contrast compliance

## Future Enhancements

- React component integration (Islands Architecture)
- Backend API integration
- Real-time filter updates
- Advanced search features
- Map integration
- Save search functionality
