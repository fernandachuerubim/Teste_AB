from flask import Flask, render_template, redirect, url_for, request
import numpy as np
from thompson_agent import thompson_agent
from variante import variante
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, Fernanda"

@app.route("/home")
def index():
    best_pege = thompson_agent.get_page()
    pages = {
        'blue': 'pg_layout_blue.html',
        'red': 'pg_layout_red.html'
    }
    return render_template(pages[best_pege])

@app.route('/yes', methods=['POST']) # post é enviar
def yes_event():
    page = request.form['forwardbtn']
    pages = {
        'blue': variante(1,1,'control'), # o primeiro 1 é visitante e o segundo 1 é o click
        'red' : variante(1,1,'treatment')
    }
    pages[page].salvar_experiment()
    return redirect(url_for('index'))

@app.route('/no', methods=['POST'])
def no_event():
    page = request.form['forwardbtn']
    pages = {
        'blue': variante(1,0,'control'), # o primeiro 1 é visitante e o segundo 1 é o click
        'red' : variante(1,0,'treatment')
    }
    pages[page].salvar_experiment()
    return redirect(url_for('index'))

@app.route('/dados', methods=['GET']) # o metodo GET é buscar/pegar
def dados():
    data = variante.load_data() # vai retornar os dados
    data = thompson_agent.convert_to_dataFrame(data) # converte tudo para dataframe

    data = json.dumps(data.to_dict(orient="records")) # converte para json
    return data

@app.route('/apagar', methods=['GET'])
def apagar():
    data = variante.delete_experiment()
    return f"Foi deletado {data} registros"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
