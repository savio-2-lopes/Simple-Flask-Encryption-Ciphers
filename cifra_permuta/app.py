import string
from utils import descriptografar_permuta, criptografar_permuta 
from flask import Flask, render_template, Blueprint, jsonify, flash, request, redirect, url_for, session
from decouple import config

app = Flask(__name__)

# Chave da aplicação Flask

app.secret_key = config('SECRET_KEY')

# Criptografar

@app.route('/', methods=['GET', 'POST'])
def criptografar():
  option = "criptografar"
  data = ''

  if request.method == 'POST':
    text = request.form['texto'].replace(" ", "-").lower()
    key = request.form['chave'].lower()
    data = criptografar_permuta(text, key)
  return render_template('index.html', data=data, option=option)

# Descriptografar

@app.route('/descriptografar/', methods=['GET', 'POST'])
def descriptografar():
  option = "descriptografar"
  data = ''

  if request.method == 'POST':
    texto = request.form['texto'].replace(" ", "").lower()
    chave = request.form['chave'].lower()
    data = descriptografar_permuta(texto, chave)

  print(data)
  return render_template('index.html', data=data, option=option)

# Tela de erro

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Ocorreu um erro na página ' + request.url,
        'status': 404
    }

    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
  app.run(debug=True)