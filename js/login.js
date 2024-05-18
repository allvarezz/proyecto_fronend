$(document).ready(function () {
  $("#login").submit(function (e) {
    e.preventDefault();
    var usuario = $("#usuario").val();
    if (usuario === "") {
      return swal("Completar datos del usuario");
    }
    var pass = $("#password").val();
    if (pass === "") {
       return  swal("ingrese su password");
      }

      if(usuario!="" && pass!=""){
        return swal("Bienvenido!!!!!!😊😊😊😊😊")
      }




  });
  
});
