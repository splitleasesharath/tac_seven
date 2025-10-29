#!/usr/bin/env python3
"""
Validate the search page HTML structure
Ensures all required filter elements are present
"""

import sys
from pathlib import Path
from html.parser import HTMLParser

class FilterElementParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = {
            'filter_section': False,
            'filter_title': False,
            'clear_button': False,
            'location_input': False,
            'min_price': False,
            'max_price': False,
            'schedule_checkboxes': 0,
            'property_type_checkboxes': 0,
            'bedroom_buttons': 0,
            'bathroom_buttons': 0,
            'amenity_checkboxes': 0,
            'apply_button': False
        }
        self.current_context = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        elem_id = attrs_dict.get('id', '')
        elem_class = attrs_dict.get('class', '')

        # Check for filter section
        if elem_id == 'filter-section':
            self.elements['filter_section'] = True

        # Check for clear button
        if elem_id == 'clear-filters':
            self.elements['clear_button'] = True

        # Check for inputs
        if elem_id == 'location-input':
            self.elements['location_input'] = True
        if elem_id == 'min-price':
            self.elements['min_price'] = True
        if elem_id == 'max-price':
            self.elements['max_price'] = True

        # Check for apply button
        if elem_id == 'apply-filters':
            self.elements['apply_button'] = True

        # Track context for checkboxes
        if 'schedule-options' in elem_class:
            self.current_context = 'schedule'
        elif 'property-type-options' in elem_class:
            self.current_context = 'property_type'
        elif 'amenities-options' in elem_class:
            self.current_context = 'amenity'
        elif 'bedroom-options' in elem_class:
            self.current_context = 'bedroom'
        elif 'bathroom-options' in elem_class:
            self.current_context = 'bathroom'

        # Count checkboxes and buttons
        if tag == 'input' and attrs_dict.get('type') == 'checkbox':
            if self.current_context == 'schedule':
                self.elements['schedule_checkboxes'] += 1
            elif self.current_context == 'property_type':
                self.elements['property_type_checkboxes'] += 1
            elif self.current_context == 'amenity':
                self.elements['amenity_checkboxes'] += 1

        if tag == 'button' and 'option-button' in elem_class:
            if self.current_context == 'bedroom':
                self.elements['bedroom_buttons'] += 1
            elif self.current_context == 'bathroom':
                self.elements['bathroom_buttons'] += 1

    def handle_data(self, data):
        if 'Filters' in data and not self.elements['filter_title']:
            self.elements['filter_title'] = True

def validate_html():
    html_path = Path(__file__).parent / "pages" / "search" / "index.html"

    if not html_path.exists():
        print(f"ERROR: HTML file not found at {html_path}")
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = FilterElementParser()
    parser.feed(html_content)

    print("Filter Section Structure Validation")
    print("=" * 50)

    all_passed = True

    # Required elements
    checks = [
        ('Filter Section', parser.elements['filter_section']),
        ('Filter Title', parser.elements['filter_title']),
        ('Clear Button', parser.elements['clear_button']),
        ('Location Input', parser.elements['location_input']),
        ('Min Price Input', parser.elements['min_price']),
        ('Max Price Input', parser.elements['max_price']),
        ('Schedule Checkboxes (>=3)', parser.elements['schedule_checkboxes'] >= 3),
        ('Property Type Checkboxes (>=4)', parser.elements['property_type_checkboxes'] >= 4),
        ('Bedroom Buttons (>=5)', parser.elements['bedroom_buttons'] >= 5),
        ('Bathroom Buttons (>=5)', parser.elements['bathroom_buttons'] >= 5),
        ('Amenity Checkboxes (>=6)', parser.elements['amenity_checkboxes'] >= 6),
        ('Apply Button', parser.elements['apply_button']),
    ]

    for name, passed in checks:
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status}: {name}")
        if not passed:
            all_passed = False

    print("=" * 50)

    if all_passed:
        print("All validation checks passed!")
        return True
    else:
        print("Some validation checks failed!")
        return False

if __name__ == "__main__":
    success = validate_html()
    sys.exit(0 if success else 1)
