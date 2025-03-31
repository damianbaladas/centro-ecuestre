import database

def obtener_caballos():
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM caballos')
    caballos = cursor.fetchall()
    cursor.close()
    conn.close()
    return caballos

def agregar_caballo(nombre, raza, edad):
    conn = database.conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO caballos (nombre, raza, edad) VALUES (%s, %s, %s)', (nombre, raza, edad))
    conn.commit()
    cursor.close()
    conn.close()