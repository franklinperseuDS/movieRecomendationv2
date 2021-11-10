# -*- coding: utf-8 -*-
from flask import Flask
import numpy as np
from sklearn.model_selection import train_test_split
from flask import Flask, request, jsonfy


#criar app
app = Flask(__name__)


#coluna de dados
colunas = ['filmeId','nota_media','Horror','Crime','Children','Thriller','Film-Noir','Documentary','Fantasy','Mystery',
           'Comedy','Drama','Musical','Adventure','Romance','War','Animation','IMAX','Action','Western','Sci-Fi','class',  ]



@app.route('/reco/<id>')
def show_id(id):
    return f'Recebendo dados \n ID: {id}'


@app.route('/')
def home():
    return 'API de predição de filmes'

app.run(debug=True)



