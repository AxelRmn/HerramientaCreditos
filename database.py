from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializar la base de datos
db = SQLAlchemy()

class Credito(db.Model):
    __tablename__ = 'creditos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tasa_interes = db.Column(db.Float, nullable=False)
    plazo = db.Column(db.Integer, nullable=False)
    fecha_otorgamiento = db.Column(db.String(10), nullable=False, default=datetime)

    def to_dict(self) -> dict:
        # Convierte el objeto en un diccionario para JSON.
        return {
            'id': self.id,
            'cliente': self.cliente,
            'monto': round(self.monto, 2),
            'tasa_interes': round(self.tasa_interes, 2),
            'plazo': self.plazo,
            'fecha_otorgamiento': self.fecha_otorgamiento
        }

def init_db(app):
    # Inicializa la base de datos con la aplicación Flask.
    db.init_app(app)
    with app.app_context():
        db.create_all()
