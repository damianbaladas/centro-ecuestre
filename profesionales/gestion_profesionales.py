import database

def obtener_profesionales():
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM profesionales')
    profesionales = cursor.fetchall()
    cursor.close()
    conn.close()
    return profesionales

def agregar_profesional(ci, nombre, apellidos, especialidad):
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO profesionales (ci, nombre, apellidos, especialidad) VALUES (%s, %s, %s, %s)', (ci, nombre, apellidos, especialidad))
    conn.commit()
    cursor.close()
    conn.close()