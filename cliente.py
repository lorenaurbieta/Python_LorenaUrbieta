from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def llamarServicioSet():
    json_data = request.get_json()
    ci = json_data.get('ci') if json_data else None
    resultado = verificarCi(ci)
    return jsonify(resultado)

def verificarCi(ci):
    # Datos simulados del cliente
    if ci == '6756026':
        return {
            'accion': 'Success',
            'codRes': 'SIN_ERROR',
            'menRes': 'OK',
            'ci': '6756026',
            'nombre': 'Lorena',
            'apellidos': 'Urbieta Campuzano'
        }
    else:
        return {
            'accion': 'Cliente no está en el sistema',
            'codRes': 'ERROR',
            'menRes': 'Error cliente',
            'ci': ci
        }