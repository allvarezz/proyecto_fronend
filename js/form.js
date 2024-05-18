$(document).ready(function() {
  
   
    $('#formulario').submit(function(e) {
        e.preventDefault(); 
        

        var nombre = $("#nombre").val();
        if(nombre===""){
            return swal("Ingrese su nombre");
        }

        

        var apellido = $("#apellido_paterno").val();
        if(apellido===""){
            return swal("Ingrese apellido Paterno");
        }

        var celular = $("#celular").val();
        if(celular.length < 5 ){
            return swal("Ingrese numero valido");
            
        }
        var motivo =$("#motivo").val();
        if(motivo===""){
            return swal("Campo motivo obligatorio");
        }

        var mensaje = $("#mensaje").val();

        return swal("Mensaje de:"+nombre+" "+apellido+"\n"+ "Asunto "+motivo+" \n"+mensaje );

    });
});
