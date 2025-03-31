import psycopg2

def conectar_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="centro_ecuestre_db",
            user="damian",
            password="2802"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tablas():
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id SERIAL PRIMARY KEY,
                ci TEXT,
                nombre TEXT,
                apellidos TEXT,
                historial_medico TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profesionales (
                id SERIAL PRIMARY KEY,
                ci TEXT,
                nombre TEXT,
                apellidos TEXT,
                especialidad TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS caballos (
                id SERIAL PRIMARY KEY,
                nombre TEXT,
                raza TEXT,
                edad INTEGER
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sesiones (
                id SERIAL PRIMARY KEY,
                fecha TEXT,
                paciente_id INTEGER,
                profesional_id INTEGER,
                caballo_id INTEGER,
                observaciones TEXT,
                FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
                FOREIGN KEY (profesional_id) REFERENCES profesionales(id),
                FOREIGN KEY (caballo_id) REFERENCES caballos(id)
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()

crear_tablas()

# Agregar funciones para interactuar con las tablas (INSERT, SELECT, UPDATE, DELETE)