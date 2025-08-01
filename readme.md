# 🗃 Administrador de Colección de Libros/Películas/Música

---

## 📝 Descripción

El Administrador de Colección es una aplicación de consola desarrollada en Python que permite al usuario gestionar una colección personal de elementos culturales, como libros, películas o música. El objetivo principal es ofrecer una herramienta sencilla y eficaz para organizar títulos, registrar detalles como el autor/artista, género y una valoración personal.
Esta herramienta es ideal para quienes desean mantener un registro estructurado de su colección, consultar rápidamente cualquier elemento o simplemente tener una base de datos personal de sus gustos.

---

## 🎯 Problemática 

**Para muchas personas, organizar su colección de libros, películas o música puede ser un desafío, especialmente cuando el número de elementos crece y es difícil recordar detalles específicos. Sin un sistema centralizado, es complicado:**

- Mantener un registro ordenado de cada elemento con sus características.
- Consultar detalles de cada título, como autor, género o valoraciones, sin tener que revisar manualmente cada uno.
- Realizar búsquedas rápidas por título, género o autor.
- Asegurar que la información persista entre usos de la aplicación.

Este administrador de colección resuelve estas problemáticas al ofrecer una interfaz de consola donde los datos quedan organizados, accesibles y persistentes gracias al guardado en un archivo JSON.

---

## ✨ Funciones Principales

**La aplicación cuenta con las siguientes funcionalidades para una gestión completa de la colección:**

- Añadir Elemento a la Colección
- Permite al usuario registrar un nuevo elemento especificando su título, autor/director/artista, género y una valoración.
- Listar Elementos de la Colección
- Muestra todos los elementos registrados en la colección en un formato de tabla claro y legible.
- Buscar Elemento
- Facilita la búsqueda de un elemento específico en la colección a través de filtros por título, autor o género.
- Editar Elemento
- Permite modificar la información de un elemento ya existente, como su título, autor o valoración.
- Eliminar Elemento
- Elimina un elemento de la colección de forma permanente, ayudando a mantener la base de datos actualizada.

---

## 🛠️ Tecnologías y Herramientas

- **Lenguaje:** Python
- **Interfaz:** Aplicación de consola.
- **GitHub:** Para la gestión del código fuente y el versionado del proyecto.

---

## 🚀 Instalación y Uso

**Para ejecutar este proyecto en tu máquina local, sigue estos pasos**

- abre visual estudio code 

- installa la extencion de python 

- Clona el repositorio copiando y peghando el sigiente link:

git clone https://github.com/wen-27/proyecto-python.git

- Ejecuta la aplicación desde python, main.py

---

## 💻 estructura del proyecto

- **🗂 controllers:** 

- **buscar.py:** nos busca la informacion completa del libro, musica o pelicula 
- **editar.py:**  nos permite editar la informacion ya ingresada del libro, musica o pelicula
- **eliminar.py:** nos permite eliminar la informacion ya ingresada en libro, musica o pelicula 
- **libros.py** nos registra libros nuevos y nos muestra los mismos guardandolos en un archivo json 
- **musica.py** nos registra musica nueva y nos muestra las mismas guardandolos en un archivo json 
- **peliculas.py** nos registra peliculas nuevas y nos muestra las mismas guardandolas en un archivo json

- **🗂 data:**

- **libros.json:** nos guarda toda la informacion registrada por el autor en libros
- **musica.json:** nos guarda toda la informacion registrada por el autor en musica
- **peliculas.json:** nos guarda toda la informacion registrada por el autor en peliculas

- **🗂 utils**

- **helpers.py:** guarda las funciones exenciales del codigo y que se usan repetidamente en los modulos
- **menus.py:** me guarda todos los menus usados en el proyecto 

- **main.py:** el archivo ejecutable y en donde llamamos todo lo necesario parta que funcione aqui se encuentra la funcion menu que es exencial para la ejecucion

---

## 👥 Contribuidores

**Este proyecto fue realizado por:**

- wendy angelica vega sanchez
- felipe corredor silva
