import string
from utils import descryption_caesar, encryption_caesar 
from flask import Flask, render_template, Blueprint, jsonify, flash, request, redirect, url_for, session
from decouple import config

app = Flask(__name__)

# Chave da aplicação Flask

# app.secret_key = config('SECRET_KEY')

# Criptografar

@app.route('/', methods=['GET', 'POST'])
def criptografar():
  option = "criptografar"
  data = ''

  if request.method == 'POST':
    texto = request.form['texto'].replace(" ", "-").lower()
    deslocamento = request.form['deslocamento']
    desl = int(deslocamento)
    data = encryption_caesar(texto, desl, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
  return render_template('index.html', data=data, option=option)

# Descriptografar

@app.route('/descriptografar/', methods=['GET', 'POST'])
def descriptografar():
  option = "descriptografar"
  new_data = ''

  if request.method == 'POST':
    texto = request.form['texto']
    deslocamento = request.form['deslocamento']
    desl = int(deslocamento)
    data = descryption_caesar(texto, desl, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
    new_data = data.replace("'", "-")
  print(new_data)
  return render_template('index.html', data=new_data, option=option)

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