document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form-materia');
    const erroresDiv = document.getElementById('errores-form');

    if (!form) return;

    form.addEventListener('submit', function (event) {
        erroresDiv.innerHTML = '';
        const errores = [];

        const nombreMateria = document.getElementById('id_nombre_materia');
        const comentario = document.getElementById('id_comentario');
        const calificacion = document.getElementById('id_calificacion');

        if (!nombreMateria.value.trim()) {
            errores.push('El nombre de la materia es obligatorio.');
        }

        if (!comentario.value.trim()) {
            errores.push('El comentario es obligatorio.');
        }

        const calif = parseInt(calificacion.value, 10);
        if (isNaN(calif) || calif < 0 || calif > 100) {
            errores.push('La calificación debe estar entre 0 y 100.');
        }

        if (errores.length > 0) {
            event.preventDefault();
            erroresDiv.innerHTML = errores.map(e => `<p>${e}</p>`).join('');
        }
    });
});
