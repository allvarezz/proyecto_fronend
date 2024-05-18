$(document).ready(function () {
  $("#login").submit(function (e) {
    e.preventDefault();
    var usuario = $("#usuario").val();
    if (usuario === "") {
      return swal("Complete campo usuario");
    }
    var pass = $("#password").val();
    if (pass === "") {
       return  swal("ingrese su password");
      }

      if(usuario!="" && pass!=""){
        return Swal.fire({
          title: "Login Perfecto!! 😎😎😎",
          text: "Bienvenido"+" "+usuario,
          icon: "success"
        });
      }




  });
  
});
