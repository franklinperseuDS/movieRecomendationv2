# -*- coding: utf-8 -*-
from flask import Flask
import numpy as np
from sklearn.model_selection import train_test_split
from flask import Flask, request, jsonify
import pickle

#criar app
app = Flask(__name__)


#coluna de dados
#colunas = ['filmeId','nota_media','Horror','Crime','Children','Thriller','Film-Noir','Documentary','Fantasy','Mystery',
#           'Comedy','Drama','Musical','Adventure','Romance','War','Animation','IMAX','Action','Western','Sci-Fi','class',  ]
colunas = ['id','filmeId']


def load_model( file_name = ''):
    return pickle.load(open(file_name, "rb"))

@app.route('/reco/<id>')
def show_id(id):
    return f'Recebendo dados \n ID: {id}'

@app.route('/reco/', methods=['POST'])
def get_recomendations():
    dados = request.get_json()
    # playload = np.array([dados[col] for col in colunas])
    #playload = fit_transform([playload], feature_names=colunas)
    #score = np.float64(modelo.predict(playload)[0])
    if(dados):
        return f'chegou aqui {dados}'
    else:
        return 'nada aqui'
    
    

@app.route('/')
def home():
    return 'API de predição de filmes'

app.run(debug=True)



