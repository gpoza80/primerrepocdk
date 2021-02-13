#!/bin/python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hola Caracola!!'
@app.route('/saludo/<persona>')
def saludoDinamico(persona):
    return 'Hola %s, bienvenido!!!!' % persona

@app.route('/cuadrado/<float:num>')
def calculaCuadrado(num):
    resp = num * num,
    return 'Respuesta: %f' % resp

@app.route("/test", methods=["POST"])
def test():
    return _test(request.form["test"])

@app.route("/index")
def index():
    return _test("My Test Data")

def _test(argument):
    return "TEST: %s" % argument

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000, debug=True)
