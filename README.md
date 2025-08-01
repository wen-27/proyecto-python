Administrador de Colección de Libros/Películas/Música
📝 Descripción
El Administrador de Colección es una aplicación de consola desarrollada en Python que permite al usuario gestionar una colección personal de elementos culturales, como libros, películas o música. El objetivo principal es ofrecer una herramienta sencilla y eficaz para organizar títulos, registrar detalles como el autor/artista, género y una valoración personal.
Esta herramienta es ideal para quienes desean mantener un registro estructurado de su colección, consultar rápidamente cualquier elemento o simplemente tener una base de datos personal de sus gustos.
🎯 Problemática
Para muchas personas, organizar su colección de libros, películas o música puede ser un desafío, especialmente cuando el número de elementos crece y es difícil recordar detalles específicos. Sin un sistema centralizado, es complicado:
Mantener un registro ordenado de cada elemento con sus características.
Consultar detalles de cada título, como autor, género o valoraciones, sin tener que revisar manualmente cada uno.
Realizar búsquedas rápidas por título, género o autor.
Asegurar que la información persista entre usos de la aplicación.
Este administrador de colección resuelve estas problemáticas al ofrecer una interfaz de consola donde los datos quedan organizados, accesibles y persistentes gracias al guardado en un archivo JSON.
✨ Funciones Principales
La aplicación cuenta con las siguientes funcionalidades para una gestión completa de la colección:
Añadir Elemento a la Colección
Permite al usuario registrar un nuevo elemento especificando su título, autor/director/artista, género y una valoración.
Listar Elementos de la Colección
Muestra todos los elementos registrados en la colección en un formato de tabla claro y legible.
Buscar Elemento
Facilita la búsqueda de un elemento específico en la colección a través de filtros por título, autor o género.
Editar Elemento
Permite modificar la información de un elemento ya existente, como su título, autor o valoración.
Eliminar Elemento
Elimina un elemento de la colección de forma permanente, ayudando a mantener la base de datos actualizada.
Cargar y Guardar Colección
Al iniciar, la aplicación carga automáticamente la colección desde el archivo coleccion.json.
Al cerrar, todos los cambios realizados se guardan de forma automática en el mismo archivo, asegurando la persistencia de los datos.
🛠️ Tecnologías y Herramientas
Lenguaje: Python
Interfaz: Aplicación de consola.
Librerías:
tabulate: Para mostrar los datos de la colección en tablas bien formateadas. Puedes encontrarla en PyPI.
Recursos de Diseño:
La estructura de los menús de la consola se inspiró en el siguiente recurso: Menu Design Gist.
Control de Versiones:
GitHub: Para la gestión del código fuente y el versionado del proyecto.
🚀 Instalación y Uso
Para ejecutar este proyecto en tu máquina local, sigue estos pasos:
Clona el repositorio:
Generated bash
git clone https://github.com/wen-27/proyecto-python.git
Use code with caution.
Bash
Navega al directorio del proyecto:
Generated bash
cd proyecto-python
Use code with caution.
Bash
Instala las dependencias:
El único requisito externo es la librería tabulate.
Generated bash
pip install tabulate
Use code with caution.
Bash
Ejecuta la aplicación:
Generated bash
python main.py
Use code with caution.
Bash
Nota: Asegúrate de que tu archivo principal se llame main.py o reemplaza el comando con el nombre correcto.
📂 Estructura del Proyecto
El repositorio está organizado de la siguiente manera para mantener el código limpio y modular:
Generated code
Proyecto_Python_ApellidoNombre/
├── main.py                 # Archivo principal de ejecución de la aplicación.
├── modulos/                # Directorio con los archivos modularizados.
│   ├── funciones.py        # Ejemplo de módulo con la lógica de la aplicación.
│   └── ...                 # Otros módulos necesarios.
├── coleccion.json          # Archivo JSON que almacena los datos de la colección.
└── README.md               # Este archivo.
Use code with caution.
👥 Contribuidores
Este proyecto fue realizado por:
wendy angelica vega sanchez
felipe corredor silva
