// Asegúrate de que el documento se haya cargado antes de ejecutar el script
document.addEventListener('DOMContentLoaded', function () {
    // Cargar el archivo JSON
    fetch('/static/json/data.json')
        .then(response => response.json())
        .then(data => {
            // Obtener el contenedor donde se insertarán las tarjetas
            const container = document.querySelector('.row');
            
            // Limpiar el contenedor antes de agregar las nuevas tarjetas
            container.innerHTML = '';

            // Recorrer cada objeto en el archivo JSON
            data.forEach(item => {
                // Crear una nueva tarjeta con la estructura HTML y los datos
                const cardHTML = `
                    <div class="col s12 m4">
                        <div class="card">
                            <div class="card-image">
                                <img src="${item.imagen}" alt="${item.titulo}">
                                <span class="card-title">${item.titulo}</span>
                            </div>
                            <div class="card-content">
                                <p>${item.descripcion}</p>
                            </div>
                        </div>
                    </div>
                `;
                
                // Insertar la tarjeta dentro del contenedor
                container.innerHTML += cardHTML;
            });
        })
        .catch(error => {
            console.error('Error cargando JSON:', error);
        });
});
