import database

def obtener_pacientes():
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes')
    pacientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return pacientes

def agregar_paciente(ci, nombre, apellidos, historial_medico):
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pacientes (ci, nombre, apellidos, historial_medico) VALUES (%s, %s, %s, %s)', (ci, nombre, apellidos, historial_medico))
    conn.commit()
    cursor.close()
    conn.close()