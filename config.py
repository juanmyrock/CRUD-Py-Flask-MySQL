#Archivo para hacer la conexion. 

# Instalar con pip install Flask
from flask import Flask, request, jsonify, render_template

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------
#variables para configurar la base de datos.
HOST = ''
USER = ''
PASSWORD = '' 
DATABASE = ''
#HOLA = HOLA para poner todo en mayuscula seleccionar ctr + shift y el comando uppercase en la barra 

app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas