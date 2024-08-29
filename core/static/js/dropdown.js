document.addEventListener("click", function (e) {
  // Close all dropdowns if the click is outside of any dropdown group
  if (!e.target.closest(".group")) {
    document.querySelectorAll(".dropdown-menu").forEach(function (menu) {
      menu.style.visibility = "hidden";
      menu.style.opacity = "0";
    });
  }
});
