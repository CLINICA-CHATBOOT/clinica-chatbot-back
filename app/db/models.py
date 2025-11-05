from database import get_conexion

def tabla_specialties():
    conexion = get_conexion()
    conexion.execute("""
    CREATE TABLE IF NOT EXISTS specialties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)
    conexion.commit()
    conexion.close()

def tabla_professionals():
    conexion = get_conexion()
    conexion.execute("""
    CREATE TABLE IF NOT EXISTS professionals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialty_id INTEGER,
        FOREIGN KEY (specialty_id) REFERENCES specialties(id)
    )
    """)
    conexion.commit()
    conexion.close()

def tabla_appointments():
    conexion = get_conexion()
    conexion.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        professional_id INTEGER,
        patient_name TEXT NOT NULL,
        appointment_date DATETIME NOT NULL,
        FOREIGN KEY (professional_id) REFERENCES professionals(id)
    )
    """)
    conexion.commit()
    conexion.close()