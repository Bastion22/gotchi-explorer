document.addEventListener('DOMContentLoaded', function() {
    // Get references to the objects that you want to click on and hide/show
    const hamburger = document.querySelector('.hamburger');
    const backButton = document.querySelectorAll('.master-back-button');
  
    // Add event listeners to the objects that you want to click on
    let clicks = 0;
    hamburger.addEventListener('click', function() {
      clicks++;
      if (clicks === 1) {
        // Hide the backButton element on the first click
        backButton.forEach(function(button) {
          button.classList.add('hidden');
        });
      } else if (clicks === 2) {
        // Show the backButton element on the second click
        backButton.forEach(function(button) {
          button.classList.remove('hidden');
        });
        clicks = 0;
      }
    });
  });







// document.addEventListener('DOMContentLoaded', function() {
//     // Get references to the objects that you want to click on and hide/show
//     const cactiMenus = document.querySelectorAll('.cacti-menu');
//     const backButton = document.querySelectorAll('.master-back-button');
  
//     // Add event listeners to the objects that you want to click on
//     cactiMenus.forEach(function(cactiMenu) {
//       cactiMenu.addEventListener('click', function() {
//         // Hide the backButton element when a cactiMenu element is clicked
//         backButton.forEach(function(button) {
//           setTimeout(function() {
//             button.style.display = 'none';
//           }, 300); // 300 millisecond delay
//         });
//       });
//     });
  
//     const swordMenu = document.querySelector('.menu-sword');
//     if (swordMenu) {
//       swordMenu.addEventListener('click', function() {
//         // Show the backButton element when the swordMenu element is clicked
//         backButton.forEach(function(button) {
//           setTimeout(function() {
//             button.style.display = 'flex';
//           }, 300); // 300 millisecond delay
//         });
//       });
//     }
//   });







// document.addEventListener('DOMContentLoaded', function() {
// // Get references to the objects that you want to click on and hide/show
//     const cactiMenus = document.querySelectorAll('.cacti-menu');
//     const backButton = document.querySelectorAll('.master-back-button');

//     // Add event listeners to the objects that you want to click on
//     cactiMenus.forEach(function(cactiMenu) {
//         cactiMenu.addEventListener('click', function() {
//         // Hide the backButton element when a cactiMenu element is clicked
//         backButton.forEach(function(button) {
//             button.style.display = 'none';
//         });
//         });
//     });

//     const swordMenu = document.querySelector('.menu-sword');
//     if (swordMenu) {
//         swordMenu.addEventListener('click', function() {
//         // Show the backButton element when the swordMenu element is clicked
//         backButton.forEach(function(button) {
//             button.style.display = 'block';
//         });
//         });
//     }
// });






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
