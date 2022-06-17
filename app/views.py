from flask import render_template
from app import app 
from datetime import datetime

@app.route('/')
def home():
    return "<b>There has been a change</b>"

@app.route('/template')
def template():
    return render_template('home.html')

@app.route('/soma/<int:n1>+<int:n2>')
def soma(n1, n2):
   soma = n1 + n2
   return f'Soma = {soma}'

@app.route('/hora')
def hora():
   return f'Hora atual: {datetime.now()}'
