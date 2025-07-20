#-*- Coding: utf-8 -*- 
#Caracateres especiales
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/', methods=['GET'])
def unida():
    return 'Hola desde la UNIDA'
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
'''
0.0.0.0 es una dirección IP que permite que la aplicación Flask sea accesible desde cualquier dirección IP en la red local. 
'''
