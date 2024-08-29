// JavaScript logic to handle dynamic updates of the subcategories based on the selected department
// Add event listeners, handle AJAX calls, or any other necessary logic for cascading functionality

document.addEventListener('DOMContentLoaded', function () {
    const categoryField = document.querySelector('select[name="category"]');
    const subcategoryField = document.querySelector('select[name="subcategory"]');

    if (categoryField && subcategoryField) {
        categoryField.addEventListener('change', function () {
            const selectedCategory = categoryField.value;

            fetch(`/path/to/api/endpoint/?category=${selectedCategory}`)
                .then(response => response.json())
                .then(data => {
                    subcategoryField.innerHTML = '';
                    data.subcategories.forEach(subcategory => {
                        const option = document.createElement('option');
                        option.value = subcategory.pk;
                        option.textContent = subcategory.name;
                        subcategoryField.appendChild(option);
                    });
                });
        });
    }
});
