import psycopg2
import csv
from io import StringIO

# Datos de conexión
DB_CONFIG = {
    "host": "localhost",
    "database": "globant_db",
    "user": "postgres",
    "password": "imontero"
}

# Cargar CSV a PostgreSQL
def csv_to_postgres(path, table):
    try:
        with psycopg2.connect(**DB_CONFIG) as con:
            with con.cursor() as cur:
                with open(path, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    #headers = next(reader)  # Leer encabezados
                    
                    # Convertir CSV a formato compatible con `copy_from`
                    csv_data = StringIO()
                    for row in reader:
                        csv_data.write(",".join(row) + "\n")
                    
                    csv_data.seek(0)  # Volver al inicio del buffer

                    # Ejecutar inserción en la tabla
                    cur.copy_from(csv_data, table, sep=",")

                con.commit()
                print(f"Datos insertados correctamente en '{table}'.")

    except Exception as e:
        print(f"Error al insertar datos en '{table}': {e}")

# Uso de la función
csv_to_postgres("sources\jobs.csv", "jobs")
csv_to_postgres("sources\departments.csv", "departments")
csv_to_postgres("sources\hired_employees.csv", "hired_employees")
