from flask import Blueprint, request, jsonify
from database import db, Credito
from flask_cors import CORS
from datetime import datetime

main = Blueprint('main', __name__)
CORS(main)  # Habilita CORS para solicitudes desde el frontend


@main.route('/creditos', methods=['POST'])
def registrar_credito():
    # Registra un nuevo crédito en la base de datos
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({'error': 'Datos JSON inválidos o mal formateados'}), 400

        required_fields = ['cliente', 'monto', 'tasa_interes', 'plazo', 'fecha_otorgamiento']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Faltan datos requeridos'}), 400

        monto = float(data['monto'])
        tasa_interes = float(data['tasa_interes'])
        plazo = int(data['plazo'])
        fecha_otorgamiento = data['fecha_otorgamiento']

        if monto <= 0 or tasa_interes <= 0 or plazo <= 0:
            return jsonify({'error': 'Los valores deben ser positivos'}), 400

        nuevo_credito = Credito(
            cliente=data['cliente'],
            monto=monto,
            tasa_interes=tasa_interes,
            plazo=plazo,
            fecha_otorgamiento=fecha_otorgamiento
        )
        db.session.add(nuevo_credito)
        db.session.commit()

        return jsonify({'message': 'Crédito registrado exitosamente', 'credito': nuevo_credito.to_dict()}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/creditos', methods=['GET'])
def listar_creditos():
    # Lista todos los créditos ordenados por fecha de otorgamiento
    try:
        creditos = Credito.query.order_by(Credito.fecha_otorgamiento.desc()).all()
        return jsonify([credito.to_dict() for credito in creditos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/creditos/<int:id>', methods=['GET'])
def obtener_credito(id):
    # Obtiene un crédito específico por su ID
    try:
        credito = Credito.query.get_or_404(id)
        return jsonify(credito.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/creditos/<int:id>', methods=['PUT'])
def editar_credito(id):
    # Edita un crédito existente en la base de datos
    try:
        credito = Credito.query.get_or_404(id)

        credito_dict = credito.to_dict()
        credito_dict['fecha_otorgamiento'] = credito_dict['fecha_otorgamiento']
        
        data = request.get_json(silent=True)

        if not data:
            return jsonify({'error': 'Datos JSON inválidos o mal formateados'}), 400

        for key in ['cliente', 'monto', 'tasa_interes', 'plazo', 'fecha_otorgamiento']:
            if key in data:
                try:
                    if key == 'monto' or key == 'tasa_interes':
                        setattr(credito, key, float(data[key]))
                    elif key == 'plazo':
                        setattr(credito, key, int(data[key]))
                    elif key == 'fecha_otorgamiento':
                        setattr(credito, key, datetime.strptime(data[key], '%Y-%m-%d').date())
                    else:
                        setattr(credito, key, data[key])
                except ValueError:
                    return jsonify({'error': f'Formato incorrecto para {key}'}), 400

        db.session.commit()
        return jsonify({'message': 'Crédito actualizado exitosamente', 'credito': credito.to_dict()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/creditos/<int:id>', methods=['DELETE'])
def eliminar_credito(id):
    # Elimina un crédito de la base de datos
    try:
        credito = Credito.query.get_or_404(id)
        db.session.delete(credito)
        db.session.commit()
        return jsonify({'message': 'Crédito eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
