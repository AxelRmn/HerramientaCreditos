# Sistema de registro de créditos
Herramienta web desarrollada con Python - Flask, que permite registrar, visualizar, editar y eliminar créditos otorgados a clientes. También incluye una gráfica dinámica que muestra el total de créditos otorgados.

## Características
- Registro de créditos con los siguientes datos:
  - Nombre del cliente
  - Monto del crédito
  - Tasa de interés
  - Plazo en meses
  - Fecha de otorgamiento
- Listado de créditos registrados en una tabla
- Edición y eliminación de créditos
- Gráfica interactiva del total de créditos otorgados

## Tecnologías utilizadas
- **Flask**: Framework web en Python
- **Flask-SQLAlchemy**: ORM para manejar la base de datos SQLite
- **Flask-CORS**: Para permitir el acceso desde el frontend
- **Bootstrap**: Para el diseño responsivo de la interfaz
- **Chart.js**: Para la generación de gráficas dinámicas

## Requisitos previos
Antes de ejecutar el proyecto, debe de estar instalado:
- **Python 3.7+**
- **pip** (administrador de paquetes de Python)
- **SQLite** (para la base de datos)


## Instalación
1. **Clonar el repositorio**

       git clone https://github.com/AxelRmn/HerramientaCreditos.git
   
       cd HerramientaCreditos

2. **Crear un entorno virtual (opcional pero recomendado)**

        -m venv venv

3. **Activar el entorno virtual**

    En Windows:
   
        venv\Scripts\activate
   
    En macOS y Linux:
   
        source venv/bin/activate

4. **Instalar dependencias**

       pip install -r requirements.txt
   

## Uso
1. **Ejecutar la aplicación**

       python app.py

2. **Abrir en el navegador**

    Accede a la aplicación desde:
    http://127.0.0.1:5000


## Tecnologías utilizadas

- **Backend**: Flask (Python)
- **Base de datos**: SQLite
- **Frontend**: HTML, CSS, JavaScript (Bootstrap, Chart.js)
- **Gráfica**: Chart.js para la visualización de los créditos


## Estructura del proyecto
    /HerramientaCreditos
    │── app.py                # Archivo principal que inicia la aplicación
    │── database.py           # Configuración de la base de datos
    │── routes.py             # Definición de las rutas y lógica de la API
    │── templates/
    │   └── index.html        # Interfaz web de la aplicación
    │── requirements.txt      # Lista de dependencias necesarias
    │── README.md             # Documentación del proyecto

    
