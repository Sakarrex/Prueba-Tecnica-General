from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['MYSQL_HOST'] =  os.getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")
mysql = MySQL(app)

def create_profTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS profesionales(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255),
                    rubro VARCHAR(255),
                    ubicacion VARCHAR(255),
                    descripcion VARCHAR(255)
                    )
    ''')
        mysql.connection.commit()
        cur.close()

with app.app_context():
    create_profTable()

@app.route('/')
def hello_world():
    return 'Hello, World!'

#Con JSON

@app.route('/cargarprof', methods=['POST'])
def cargarprof():
    cur = mysql.connection.cursor()
    nombre = request.json['nombre']
    rubro = request.json['rubro']
    ubicacion = request.json['ubicacion']
    descripcion = request.json['descripcion']
    cur.execute('''INSERT INTO profesionales (nombre, rubro, ubicacion, descripcion) VALUES (%s, %s, %s, %s)''', (nombre, rubro, ubicacion, descripcion))
    mysql.connection.commit()
    cur.close()
    return jsonify({'mensage': 'Profesional cargado correctamente'})



@app.route('/profesionales', methods=['GET'])
def get_profesionales():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM profesionales''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

#Query con url

@app.route('/buscarprof')
def buscarprof():
    cur = mysql.connection.cursor()
    rubro = request.args.get('rubro', '')
    ubicacion = request.args.get('ubicacion', '')
    cur.execute(''' SELECT * FROM profesionales WHERE rubro=%s OR ubicacion=%s ''',(rubro,ubicacion))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

app.run()
