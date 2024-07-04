document.addEventListener("DOMContentLoaded", function () {
    // Event listener para el botón de Modificar
    document.getElementById("btnModificar").addEventListener("click", function (event) {
        event.preventDefault();
        // Aquí colocarías la lógica para la acción de Modificar
        console.log("Se ha seleccionado Modificar");
        // Cierra el modal después de realizar la acción
        $("#staticBackdrop").modal("hide");
    });

    // Event listener para el botón de Eliminar
    document.getElementById("btnEliminar").addEventListener("click", function (event) {
        event.preventDefault();
        // Aquí colocarías la lógica para la acción de Eliminar
        console.log("Se ha seleccionado Eliminar");
        // Cierra el modal después de realizar la acción
        $("#staticBackdrop").modal("hide");
    });
});
