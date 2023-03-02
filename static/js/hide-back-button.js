document.addEventListener('DOMContentLoaded', function() {
// Get references to the objects that you want to click on and hide/show
    const cactiMenus = document.querySelectorAll('.cacti-menu');
    const backButton = document.querySelectorAll('.master-back-button');

    // Add event listeners to the objects that you want to click on
    cactiMenus.forEach(function(cactiMenu) {
        cactiMenu.addEventListener('click', function() {
        // Hide the backButton element when a cactiMenu element is clicked
        backButton.forEach(function(button) {
            button.style.display = 'none';
        });
        });
    });

    const swordMenu = document.querySelector('.menu-sword');
    if (swordMenu) {
        swordMenu.addEventListener('click', function() {
        // Show the backButton element when the swordMenu element is clicked
        backButton.forEach(function(button) {
            button.style.display = 'block';
        });
        });
    }
});

// document.addEventListener('DOMContentLoaded', function() {
//     // Get references to the objects that you want to click on and hide/show
//     const cactiMenu = document.querySelector('.cacti-menu');
//     const backButton = document.querySelector('.master-back-button');
  
//     // Add event listeners to the objects that you want to click on
//     cactiMenu.addEventListener('click', function() {
//         backButton.style.display = 'none';
//     });

//     const swordMenu = document.querySelector('.menu-sword');
//     if (swordMenu) {
//       swordMenu.addEventListener('click', function() {
//         // Show the backButton element when the swordMenu element is clicked
//         backButton.style.display = 'block';
//       });
//     }

//   });
