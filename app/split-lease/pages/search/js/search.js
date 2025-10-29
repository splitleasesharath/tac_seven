// Search page JavaScript

document.addEventListener('DOMContentLoaded', () => {
    // Initialize filter functionality
    initializeFilters();
});

function initializeFilters() {
    // Clear filters button
    const clearBtn = document.getElementById('clear-filters');
    if (clearBtn) {
        clearBtn.addEventListener('click', clearAllFilters);
    }

    // Apply filters button
    const applyBtn = document.getElementById('apply-filters');
    if (applyBtn) {
        applyBtn.addEventListener('click', applyFilters);
    }

    // Option buttons (bedrooms/bathrooms)
    const optionButtons = document.querySelectorAll('.option-button');
    optionButtons.forEach(button => {
        button.addEventListener('click', () => {
            button.classList.toggle('active');
        });
    });

    // Initialize results count
    updateResultsCount();
}

function clearAllFilters() {
    // Clear text inputs
    document.querySelectorAll('.filter-input').forEach(input => {
        input.value = '';
    });

    // Uncheck all checkboxes
    document.querySelectorAll('.filter-checkbox').forEach(checkbox => {
        checkbox.checked = false;
    });

    // Deactivate all option buttons
    document.querySelectorAll('.option-button').forEach(button => {
        button.classList.remove('active');
    });

    // Update results
    updateResultsCount();
}

function applyFilters() {
    // Collect filter values
    const filters = getFilterValues();

    console.log('Applying filters:', filters);

    // Update results count
    updateResultsCount();

    // TODO: Fetch and display filtered results
}

function getFilterValues() {
    return {
        location: document.getElementById('location-input')?.value || '',
        minPrice: document.getElementById('min-price')?.value || '',
        maxPrice: document.getElementById('max-price')?.value || '',
        schedule: Array.from(document.querySelectorAll('.schedule-options .filter-checkbox:checked'))
            .map(cb => cb.value),
        propertyTypes: Array.from(document.querySelectorAll('.property-type-options .filter-checkbox:checked'))
            .map(cb => cb.value),
        bedrooms: Array.from(document.querySelectorAll('.bedroom-options .option-button.active'))
            .map(btn => btn.dataset.value),
        bathrooms: Array.from(document.querySelectorAll('.bathroom-options .option-button.active'))
            .map(btn => btn.dataset.value),
        amenities: Array.from(document.querySelectorAll('.amenities-options .filter-checkbox:checked'))
            .map(cb => cb.value)
    };
}

function updateResultsCount() {
    const countElement = document.getElementById('results-count');
    if (countElement) {
        // Placeholder - would be updated with actual results
        countElement.textContent = 'Select filters to search';
    }
}
