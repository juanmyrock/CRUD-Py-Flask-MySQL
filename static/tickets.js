document.addEventListener("DOMContentLoaded", function () {
    // Selección de elementos principales
    const cardBodies = document.querySelectorAll(".card-body");
    const categoriaSelect = document.getElementById("categoriaSelect");
    const resumenBtn = document.getElementById("resumen");
    const borrarBtn = document.getElementById("borrar");
    const form = document.querySelector("form");
    const totalElement = document.getElementById("total");
    const fileInput = document.getElementById("fotos");
    const fileLabel = document.querySelector("label[for='fotos']");

    // Event listeners para cada card-body
    cardBodies.forEach(function (cardBody) {
        cardBody.addEventListener("click", function () {
            const categoria = cardBody.closest(".card").querySelector("h4").textContent.trim().toLowerCase();
            categoriaSelect.value = getCategoriaValue(categoria);
            calcularDescuento();
        });

        cardBody.addEventListener("mouseover", function () {
            cardBody.style.backgroundColor = "#d3d3d3";
        });

        cardBody.addEventListener("mouseout", function () {
            cardBody.style.backgroundColor = "";
        });
    });

    // Event listener para el cambio de categoría
    categoriaSelect.addEventListener("change", calcularDescuento);

    // Event listener para el botón de Calcular Total
    resumenBtn.addEventListener("click", function (event) {
        event.preventDefault();
        calcularDescuento();
    });

    // Event listener para el botón Borrar
    borrarBtn.addEventListener("click", function (event) {
        event.preventDefault();
        resetForm();
    });

    // Event listener para el envío del formulario
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        alert("Compra realizada. ¡Gracias!");
        resetForm();
    });

    // Función para calcular el descuento y actualizar el total a pagar
    function calcularDescuento() {
        const precioBase = 100000;
        let descuento = 0;

        switch (categoriaSelect.value) {
            case "1":
                descuento = 0.8; // 80%
                break;
            case "2":
                descuento = 0.5; // 50%
                break;
            case "3":
                descuento = 0.15; // 15%
                break;
            default:
                descuento = 0; // Sin descuento
                break;
        }

        const cantidad = parseFloat(document.getElementById("cant").value) || 0;
        const total = precioBase * cantidad * (1 - descuento);

        totalElement.textContent = `Total a pagar: $${total.toFixed(2)}`;
    }

    // Función para resetear el formulario
    function resetForm() {
        document.getElementById("name").value = "";
        document.getElementById("apellido").value = "";
        document.getElementById("mail").value = "";
        document.getElementById("cant").value = "";
        document.getElementById("categoriaSelect").selectedIndex = 0; // Resetea el select de categoría seleccionando el primer elemento
        document.getElementById("artistas").selectedIndex = 0; // Resetea el select de artistas seleccionando el primer elemento
    
        // Para resetear el campo de archivos (input type="file")
        const fileInput = document.getElementById("fotos");
        fileInput.value = null; // Establece el valor del campo de archivos a null
    
        // Mostrar nuevamente el label para subir archivos
        const fileLabel = document.querySelector("label[for='fotos']");
        fileLabel.style.display = "block";
    
        // Ocultar el input de archivos
        fileInput.style.display = "none";
    
        totalElement.textContent = "Total a pagar: $"; // Resetea el texto del total
    }
    

    // Función para obtener el valor de la categoría
    function getCategoriaValue(categoria) {
        switch (categoria) {
            case "estudiante cac":
                return "1";
            case "jubilado":
                return "2";
            case "programador":
                return "3";
            default:
                return "0";
        }
    }

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            fileLabel.style.display = "none";
            fileInput.style.display = "block";
        } else {
            fileLabel.style.display = "block";
            fileInput.style.display = "none";
        }
    });
});