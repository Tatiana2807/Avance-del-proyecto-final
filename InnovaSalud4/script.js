// Estado actual: ¿está el usuario "logueado" en esta sesión?
let usuarioActivo = null;

// Función para mostrar el panel de citas
function mostrarPanelCitas(usuario) {
  usuarioActivo = usuario;
  
  document.getElementById('agendarCita').style.display = 'block';
  document.getElementById('registro').style.display = 'none';
  document.getElementById('mensajeBienvenida').textContent = 
    `¡Hola, ${usuario.nombre}! Bienvenido a tu panel de citas.`;
  document.getElementById('nombreUsuario').textContent = usuario.nombre;
}

// Función para volver al inicio (cerrar sesión)
function cerrarSesion() {
  usuarioActivo = null;
  
  // Mostrar registro
  document.getElementById('registro').style.display = 'block';
  // Ocultar panel de citas
  document.getElementById('agendarCita').style.display = 'none';
  // Restaurar mensaje de bienvenida
  document.getElementById('mensajeBienvenida').textContent = 
    'Regístrate para acceder a tus citas médicas.';
  // Limpiar mensajes
  document.getElementById('mensajeCita').textContent = '';
  document.getElementById('mensajeRegistro').textContent = '';
  
  // ¡Importante! No guardamos nada en localStorage
  // Pero por seguridad, lo limpiamos si existe
  localStorage.removeItem('usuarioInnovaSalud');
  localStorage.removeItem('citasInnovaSalud');
}

// Al cargar la página: siempre empezamos desde cero
document.addEventListener('DOMContentLoaded', function () {
  // Aseguramos que se muestre solo el registro al inicio
  cerrarSesion();
});

// Registro
document.getElementById('registroForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const nombre = document.getElementById('nombre').value;
  const email = document.getElementById('email').value;
  const telefono = document.getElementById('telefono').value;

  const usuario = { nombre, email, telefono };
  
  // Mostramos el panel (sin guardar en localStorage de forma persistente)
  // Pero igual lo guardamos temporalmente por si se agendan citas
  localStorage.setItem('usuarioInnovaSalud', JSON.stringify(usuario));
  
  mostrarPanelCitas(usuario);
});

// Cerrar sesión
document.getElementById('btnCerrarSesion').addEventListener('click', cerrarSesion);

// Agendar cita
document.getElementById('citaForm').addEventListener('submit', function(e) {
  e.preventDefault();

  if (!usuarioActivo) {
    alert('Debes registrarte primero.');
    return;
  }

  const doctor = document.getElementById('doctor').value;
  const fecha = document.getElementById('fecha').value;
  const hora = document.getElementById('hora').value;

  const cita = { doctor, fecha, hora, paciente: usuarioActivo.nombre };
  let citas = JSON.parse(localStorage.getItem('citasInnovaSalud')) || [];
  citas.push(cita);
  localStorage.setItem('citasInnovaSalud', JSON.stringify(citas));

  document.getElementById('mensajeCita').textContent = 
    `✅ Cita agendada con éxito con ${doctor} el ${fecha} a las ${hora}.`;

  this.reset();
});