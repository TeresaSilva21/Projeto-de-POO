from flask import Flask, request

from aplicacao import Aplicacao

app = Flask(__name__)

aplicacao = Aplicacao()

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>" 

@app.route("/dados_inicial")
def dados_inicial():
    jwt = request.cookies.get('access_token')

    return aplicacao.carregar_dados_inicial(jwt)