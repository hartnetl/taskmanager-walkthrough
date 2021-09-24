document.addEventListener('DOMContentLoaded', function() {
    // sidenav inialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // modal initialization
    let delModal = document.querySelectorAll('.modal');
    M.Modal.init(delModal);

    // datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy",
      autoClose: true,
      i18n: {done: "Select"}
    });

    // category dropdown
    let dDown = document.querySelectorAll('select');
    M.FormSelect.init(dDown);
  });

