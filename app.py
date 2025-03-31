from flask import Flask, render_template, request
from pacientes import gestion_pacientes
from profesionales import gestion_profesionales
from caballos import gestion_caballos
from sesiones import gestion_sesiones
import database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pacientes', methods=['GET', 'POST'])
def pacientes():
    if request.method == 'POST':
        ci = request.form['ci']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        historial_medico = request.form['historial_medico']
        gestion_pacientes.agregar_paciente(ci, nombre, apellidos, historial_medico)
    pacientes = gestion_pacientes.obtener_pacientes()
    return render_template('pacientes.html', pacientes=pacientes)

@app.route('/profesionales', methods=['GET', 'POST'])
def profesionales():
    if request.method == 'POST':
        ci = request.form['ci']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        especialidad = request.form['especialidad']
        gestion_profesionales.agregar_profesional(ci, nombre, apellidos, especialidad)
    profesionales = gestion_profesionales.obtener_profesionales()
    return render_template('profesionales.html', profesionales=profesionales)

# ... (resto del código)

@app.route('/caballos', methods=['GET', 'POST'])
def caballos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        gestion_caballos.agregar_caballo(nombre, raza, edad)
    caballos = gestion_caballos.obtener_caballos()
    return render_template('caballos.html', caballos=caballos)

@app.route('/sesiones', methods=['GET', 'POST'])
def sesiones():
    if request.method == 'POST':
        fecha = request.form['fecha']
        paciente_ci = request.form['paciente_ci']
        profesional_ci = request.form['profesional_ci']
        caballo_nombre = request.form['caballo_nombre']
        observaciones = request.form['observaciones']
        gestion_sesiones.agregar_sesion(fecha, paciente_ci, profesional_ci, caballo_nombre, observaciones)
    sesiones = gestion_sesiones.obtener_sesiones()
    return render_template('sesiones.html', sesiones=sesiones)

if __name__ == '__main__':
    app.run(debug=True)