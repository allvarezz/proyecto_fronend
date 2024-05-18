$(document).ready(function() {
  
   
    $('#formulario').submit(function(e) {
        e.preventDefault(); 
        var rut = $('#rut').val();
        if (rut.length < 9 || rut.length > 10) {
            alert('El RUT debe tener entre 9 y 10 caracteres.');
            return;
        }
        
        var nombre = $('#nombre').val();
        var apellidoPaterno = $('#apellido_paterno').val();
        var apellidoMaterno = $('#apellido_materno').val();
        if (nombre.length < 3 || nombre.length > 20 || apellidoPaterno.length < 3 || apellidoPaterno.length > 20 || apellidoMaterno.length < 3 || apellidoMaterno.length > 20) {
            alert('Los nombres y apellidos deben tener entre 3 y 20 caracteres.');
            return;
        }
        var f_nacimiento=$('#fecha_nacimiento').val();
        if(f_nacimiento===''){
            return alert('No se olvide de completar su fecha de nacimiento')
        }

        var edad = $('#edad').val();
        if (edad < 18 || edad > 35) {
            alert('La edad debe estar entre 18 y 35 años.');
            return;
        }

        var genero = $('#genero').val();
        if (genero === '') {
            alert('Por favor selecciona un género.');
            return;
        }

        var email=$('#email').val();
        if(email===''){
            return alert('No se permite email vacio')
        }
        
        var celular = $('#celular').val();
        if (celular.length < 9 || celular.length > 12) {
            alert('El teléfono celular debe tener entre 9 y 12 caracteres.');
            return;
        }

        var carta = 'Estimados,\nMe llamo ' + nombre + ' ' + apellidoPaterno + ' ' + apellidoMaterno + '\nRUT ' + rut +
                    ', de ' + edad + ' años de edad, género ' + genero + '.\n' +
                    'Quisiera postular al trabajo de apoyo ambiental en Chiloé porque ' + $('#motivacion').val() + '.\n\n' +
                    'Quedo atento a su respuesta.\n\nSaludos cordiales, ' + nombre;
        
        $('#carta').val(carta);
        
        console.log(carta);
       
    });
});
