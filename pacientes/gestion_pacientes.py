import database

def obtener_pacientes():
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pacientes ORDER BY id') # Ordena por ID
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

def editar_paciente(id, ci, nombre, apellidos, historial_medico):
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE pacientes SET ci = %s, nombre = %s, apellidos = %s, historial_medico = %s WHERE id = %s', (ci, nombre, apellidos, historial_medico, id))
    conn.commit()
    cursor.close()
    conn.close()

def eliminar_paciente(id):
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pacientes WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()