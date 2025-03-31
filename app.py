from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/pacientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):
    if request.method == 'POST':
        ci = request.form['ci']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        historial_medico = request.form['historial_medico']
        gestion_pacientes.editar_paciente(id, ci, nombre, apellidos, historial_medico)
        return redirect(url_for('pacientes'))
    pacientes = gestion_pacientes.obtener_pacientes()
    paciente = next((p for p in pacientes if p[0] == id), None)
    return render_template('editar_paciente.html', paciente=paciente)

@app.route('/pacientes/eliminar/<int:id>')
def eliminar_paciente(id):
    gestion_pacientes.eliminar_paciente(id)
    return redirect(url_for('pacientes'))

# Profesionales
@app.route('/profesionales/editar/<int:id>', methods=['GET', 'POST'])
def editar_profesional(id):
    if request.method == 'POST':
        ci = request.form['ci']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        especialidad = request.form['especialidad']
        gestion_profesionales.editar_profesional(id, ci, nombre, apellidos, especialidad)
        return redirect(url_for('profesionales'))
    profesionales = gestion_profesionales.obtener_profesionales()
    profesional = next((p for p in profesionales if p[0] == id), None)
    return render_template('editar_profesional.html', profesional=profesional)

@app.route('/profesionales/eliminar/<int:id>')
def eliminar_profesional(id):
    gestion_profesionales.eliminar_profesional(id)
    return redirect(url_for('profesionales'))

# Caballos
@app.route('/caballos/editar/<int:id>', methods=['GET', 'POST'])
def editar_caballo(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        gestion_caballos.editar_caballo(id, nombre, raza, edad)
        return redirect(url_for('caballos'))
    caballos = gestion_caballos.obtener_caballos()
    caballo = next((c for c in caballos if c[0] == id), None)
    return render_template('editar_caballo.html', caballo=caballo)

@app.route('/caballos/eliminar/<int:id>')
def eliminar_caballo(id):
    gestion_caballos.eliminar_caballo(id)
    return redirect(url_for('caballos'))

# Sesiones
@app.route('/sesiones/editar/<int:id>', methods=['GET', 'POST'])
def editar_sesion(id):
    if request.method == 'POST':
        fecha = request.form['fecha']
        paciente_ci = request.form['paciente_ci']
        profesional_ci = request.form['profesional_ci']
        caballo_nombre = request.form['caballo_nombre']
        observaciones = request.form['observaciones']
        gestion_sesiones.editar_sesion(id, fecha, paciente_ci, profesional_ci, caballo_nombre, observaciones)
        return redirect(url_for('sesiones'))
    sesiones = gestion_sesiones.obtener_sesiones()
    sesion = next((s for s in sesiones if s[0] == id), None)
    return render_template('editar_sesion.html', sesion=sesion)

@app.route('/sesiones/eliminar/<int:id>')
def eliminar_sesion(id):
    gestion_sesiones.eliminar_sesion(id)
    return redirect(url_for('sesiones'))# Profesionales
@app.route('/profesionales/editar/<int:id>', methods=['GET', 'POST'])
def editar_profesional(id):
    if request.method == 'POST':
        ci = request.form['ci']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        especialidad = request.form['especialidad']
        gestion_profesionales.editar_profesional(id, ci, nombre, apellidos, especialidad)
        return redirect(url_for('profesionales'))
    profesionales = gestion_profesionales.obtener_profesionales()
    profesional = next((p for p in profesionales if p[0] == id), None)
    return render_template('editar_profesional.html', profesional=profesional)

@app.route('/profesionales/eliminar/<int:id>')
def eliminar_profesional(id):
    gestion_profesionales.eliminar_profesional(id)
    return redirect(url_for('profesionales'))

# Caballos
@app.route('/caballos/editar/<int:id>', methods=['GET', 'POST'])
def editar_caballo(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        gestion_caballos.editar_caballo(id, nombre, raza, edad)
        return redirect(url_for('caballos'))
    caballos = gestion_caballos.obtener_caballos()
    caballo = next((c for c in caballos if c[0] == id), None)
    return render_template('editar_caballo.html', caballo=caballo)

@app.route('/caballos/eliminar/<int:id>')
def eliminar_caballo(id):
    gestion_caballos.eliminar_caballo(id)
    return redirect(url_for('caballos'))

# Sesiones
@app.route('/sesiones/editar/<int:id>', methods=['GET', 'POST'])
def editar_sesion(id):
    if request.method == 'POST':
        fecha = request.form['fecha']
        paciente_ci = request.form['paciente_ci']
        profesional_ci = request.form['profesional_ci']
        caballo_nombre = request.form['caballo_nombre']
        observaciones = request.form['observaciones']
        gestion_sesiones.editar_sesion(id, fecha, paciente_ci, profesional_ci, caballo_nombre, observaciones)
        return redirect(url_for('sesiones'))
    sesiones = gestion_sesiones.obtener_sesiones()
    sesion = next((s for s in sesiones if s[0] == id), None)
    return render_template('editar_sesion.html', sesion=sesion)

@app.route('/sesiones/eliminar/<int:id>')
def eliminar_sesion(id):
    gestion_sesiones.eliminar_sesion(id)
    return redirect(url_for('sesiones'))