from app.db.database import get_conexion
from app.db.models import tabla_specialties, tabla_professionals, tabla_appointments

def seed_database():
    tabla_specialties()
    tabla_professionals()
    tabla_appointments()

    conexion = get_conexion()
    cursor = conexion.execute("SELECT COUNT(*) as count FROM specialties")
    if cursor.fetchone()["count"] == 0:
        specialties = ["Cardiología", "Dermatología", "Neurología", "Pediatría"]
        for specialty in specialties:
            conexion.execute("INSERT INTO specialties (name) VALUES (?)", (specialty,))
        conexion.commit()
    
    cursor = conexion.execute("SELECT COUNT(*) as count FROM professionals")
    if cursor.fetchone()["count"] == 0:
        professionals = [
            ("Dr. Juan Rodríguez", 1),
            ("Dra. Marta Pérez", 1),
            ("Dr. Pedro Gómez", 2),
            ("Dra. Ana López", 2),
            ("Dr. Luis Fernández", 3),
            ("Dra. María Torres", 3),
            ("Dr. Pablo Díaz", 4),
            ("Dra. Laura Sánchez", 4),
        ]
        for name, specialty_id in professionals:
            conexion.execute(
                "INSERT INTO professionals (name, specialty_id) VALUES (?, ?)",
                (name, specialty_id),
            )
        conexion.commit()
    conexion.close()