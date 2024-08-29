// Add an event listener to each button with the class "accordion-button"
document.querySelectorAll('.accordion-button').forEach(button => {
  button.addEventListener('click', handleAccordionClick);
});

function handleAccordionClick(event) {
  // Get the button that was clicked
  const button = event.currentTarget;
  // Get the sibling element of the button (the collapse)
  const accordionCollapse = button.nextElementSibling;

  // Toggle the "active" class on the button
  button.classList.toggle('active');
  // Show or hide the collapse based on whether the button has the "active" class
  accordionCollapse.style.display = button.classList.contains('active') ? 'block' : 'none';
}

