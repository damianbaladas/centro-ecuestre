import database

def obtener_sesiones():
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT sesiones.id, sesiones.fecha, pacientes.ci, pacientes.nombre, pacientes.apellidos, profesionales.ci, profesionales.nombre, profesionales.apellidos, caballos.nombre, sesiones.observaciones
        FROM sesiones
        JOIN pacientes ON sesiones.paciente_id = pacientes.id
        JOIN profesionales ON sesiones.profesional_id = profesionales.id
        JOIN caballos ON sesiones.caballo_id = caballos.id
    ''')
    sesiones = cursor.fetchall()
    cursor.close()
    conn.close()
    return sesiones

def agregar_sesion(fecha, paciente_ci, profesional_ci, caballo_nombre, observaciones):
    conn = database.conectar_db()
    cursor = conn.cursor()

    # Obtener IDs de paciente, profesional y caballo
    cursor.execute('SELECT id FROM pacientes WHERE ci = %s', (paciente_ci,))
    paciente_id = cursor.fetchone()
    cursor.execute('SELECT id FROM profesionales WHERE ci = %s', (profesional_ci,))
    profesional_id = cursor.fetchone()
    cursor.execute('SELECT id FROM caballos WHERE nombre = %s', (caballo_nombre,))
    caballo_id = cursor.fetchone()

    if paciente_id and profesional_id and caballo_id:
        cursor.execute('INSERT INTO sesiones (fecha, paciente_id, profesional_id, caballo_id, observaciones) VALUES (%s, %s, %s, %s, %s)', (fecha, paciente_id[0], profesional_id[0], caballo_id[0], observaciones))
        conn.commit()
    else:
        print("Error: Paciente, profesional o caballo no encontrado.")

    cursor.close()
    conn.close()