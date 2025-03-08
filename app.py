from flask import Flask, render_template
from database import db
from routes import main

def create_app():
    # Función para crear y configurar la aplicación Flask.
    app = Flask(__name__)

    # Configuración de la base de datos SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///creditos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos con la aplicación
    db.init_app(app)

    # Crear las tablas en la base de datos si no existen
    with app.app_context():
        db.create_all()

    # Registrar el Blueprint que maneja las rutas principales
    app.register_blueprint(main)

    @app.route('/')
    def index(): 
        # Ruta principal que renderiza la página de inicio.
        return render_template('index.html')

    return app

if __name__ == '__main__':
    # Crear la aplicación y ejecutarla en modo depuración
    app = create_app()
    app.run(debug=True)
    