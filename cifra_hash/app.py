import string
import hashlib
from flask import Flask, render_template, Blueprint, jsonify, flash, request, redirect, url_for, session
from decouple import config

app = Flask(__name__)

# Chave da aplicação Flask

app.secret_key = config('SECRET_KEY')

# Criptografar

@app.route('/', methods=['GET', 'POST'])
def create_hash():
  data=""
  if request.method == 'POST':
    text = request.form['texto'].replace(" ", "-").lower()
    data = int(hashlib.sha1(text.encode("utf-8")).hexdigest(), 16) % (10 ** 2)
  return render_template('index.html', data=data)

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