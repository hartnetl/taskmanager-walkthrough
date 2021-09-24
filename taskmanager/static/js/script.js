document.addEventListener('DOMContentLoaded', function() {
    // sidenav inialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // modal initialization
    let delModal = document.querySelectorAll('.modal');
    M.Modal.init(delModal);
  });

