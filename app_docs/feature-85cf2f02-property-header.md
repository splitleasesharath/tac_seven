# Property Header Component

**ADW ID:** 85cf2f02
**Date:** October 30, 2025
**Specification:** specs/issue-11-adw-85cf2f02-sdlc_planner-property-title-basic-info.md

## Overview

The PropertyHeader component displays essential property information at the top of the view split lease page. It presents the property title as a prominent heading, location details with a purple map pin icon, and property type information with guest capacity. This component follows the Islands Architecture pattern and is built as a reusable React component in the UMD bundle.

## What Was Built

- **PropertyHeader React Component** - A TypeScript component that displays property title, location, and basic details
- **View Split Lease Page** - A new static HTML page that mounts Header, PropertyHeader, and Footer islands
- **Component Tests** - Contract and diagnostics tests validating component behavior and visual rendering
- **E2E Test Specification** - End-to-end test for validating the complete user experience

## Technical Implementation

### Files Modified

- `app/split-lease/components/src/PropertyHeader/PropertyHeader.tsx`: New React component with TypeScript interface for props (title, location, propertyType, maxGuests)
- `app/split-lease/components/src/PropertyHeader/PropertyHeader.css`: Component styles with CSS variables for purple brand color, typography scales, and responsive design
- `app/split-lease/components/src/PropertyHeader/index.ts`: Component export for UMD bundle
- `app/split-lease/components/src/index.ts`: Added PropertyHeader export to main component library
- `app/split-lease/pages/view-split-lease/index.html`: New page with Islands Architecture pattern mounting Header, PropertyHeader, and Footer
- `app/split-lease/pages/view-split-lease/css/styles.css`: Page-specific layout and spacing styles
- `app/test-harness/tests/PropertyHeader.contract.spec.js`: Contract tests validating component mounting and props
- `app/test-harness/tests/PropertyHeader.diagnostics.spec.js`: Diagnostics tests validating visual rendering and styling
- `app/test-harness/previews/property-header-preview.html`: Preview page for testing the PropertyHeader component in isolation
- `.claude/commands/e2e/test_property_header.md`: E2E test specification for validation
- `.claude/commands/conditional_docs.md`: Updated with entry for this documentation

### Key Changes

- **Component Structure**: PropertyHeader uses semantic HTML with H1 for title, flexbox layout for location with SVG map pin icon, and secondary styling for property details
- **Styling Approach**: CSS variables define customizable values (--property-header-purple: #7C3AED, typography scales) with responsive breakpoints for mobile viewports
- **Islands Architecture**: Component is mounted on static HTML using React 18 CDN and the UMD bundle, following the same pattern as Header and Footer components
- **TypeScript Types**: PropertyHeaderProps interface ensures type safety with required props (title, location object, propertyType, maxGuests) and optional className
- **Responsive Design**: Font sizes and spacing scale down at 768px and 480px breakpoints, map pin icon scales to 14x18px on smallest screens

## How to Use

### In a Static HTML Page (Islands Architecture)

1. Include React 18 and ReactDOM from CDN:
```html
<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
```

2. Include the component UMD bundle:
```html
<script src="../../components/dist/split-lease-components.umd.cjs"></script>
```

3. Create a container div for the PropertyHeader island:
```html
<div id="property-header"></div>
```

4. Mount the PropertyHeader component with props:
```javascript
var PropertyHeader = window.SplitLeaseComponents.PropertyHeader;
var props = {
  title: 'Holiday Rental: Luxurious, Sunny, and Quiet Apt on Central Park West',
  location: {
    neighborhood: 'Manhattan Valley',
    city: 'Manhattan'
  },
  propertyType: 'Private Room',
  maxGuests: 2
};
ReactDOM.createRoot(document.getElementById('property-header'))
  .render(React.createElement(PropertyHeader, props));
```

### In a React Application

```tsx
import { PropertyHeader } from '@split-lease/components';

<PropertyHeader
  title="Holiday Rental: Luxurious, Sunny, and Quiet Apt on Central Park West"
  location={{ neighborhood: 'Manhattan Valley', city: 'Manhattan' }}
  propertyType="Private Room"
  maxGuests={2}
  className="custom-class" // optional
/>
```

## Configuration

### CSS Variables

The component uses CSS variables that can be customized:

```css
:root {
  --property-header-purple: #7C3AED;           /* Map pin icon color */
  --property-header-text-color: #1a1a1a;       /* Primary text color */
  --property-header-secondary-color: #6b7280;  /* Secondary text color */
  --title-font-size: 2rem;                     /* Title size (desktop) */
  --location-font-size: 1.125rem;              /* Location size (desktop) */
  --details-font-size: 1rem;                   /* Details size (desktop) */
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
```

### Props Interface

```typescript
interface PropertyHeaderProps {
  title: string;                    // Property title
  location: {
    neighborhood: string;           // Neighborhood name
    city: string;                   // City name
  };
  propertyType: string;             // Type of property (e.g., "Private Room")
  maxGuests: number;                // Maximum number of guests
  className?: string;               // Optional additional CSS class
}
```

## Testing

### Running Tests

```bash
# Type checking
cd app/split-lease/components && npm run typecheck

# Build component bundle
cd app/split-lease/components && npm run build

# Run all component tests
cd app/test-harness && npm test
```

### E2E Testing

Read `.claude/commands/test_e2e.md`, then execute `.claude/commands/e2e/test_property_header.md` to validate:
- PropertyHeader displays on view-split-lease page
- Title, location with purple icon, and property details render correctly
- Component is responsive on mobile and desktop viewports

### Preview Page

Test the component in isolation at: `app/test-harness/previews/property-header-preview.html`

## Notes

- **Removed Components**: This implementation replaced the previous ListingImageGrid and ProposalMenu components that were removed from the codebase
- **Brand Color**: The purple map pin icon (#7C3AED) matches the Split Lease brand guidelines
- **Accessibility**: Map pin SVG includes `aria-hidden="true"` as it's decorative; location text provides the necessary information
- **Guest Pluralization**: Component intelligently handles singular vs plural "guest/guests" based on maxGuests value
- **Error Handling**: Islands mounting script includes error handling if React, ReactDOM, or components are not available
- **Future Enhancement**: Component could be extended to support clickable map pin that opens an interactive map modal
