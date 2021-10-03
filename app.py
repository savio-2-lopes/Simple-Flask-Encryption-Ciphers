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
    chave = request.form['deslocamento']
    
    deslocamento = int(chave)
    
    data = encryption_caesar(texto, deslocamento, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
  return render_template('index.html', data=data, option=option)

# Descriptografar

@app.route('/descriptografar/', methods=['GET', 'POST'])
def descriptografar():
  option = "descriptografar"
  add_space_in_text = ''

  if request.method == 'POST':
    texto = request.form['texto']
    chave = request.form['deslocamento']
    
    deslocamento = int(chave)
    
    data = descryption_caesar(texto, deslocamento, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
    add_space_in_text = data.replace("'", "-")
  
  print(add_space_in_text)
  return render_template('index.html', data=add_space_in_text, option=option)

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