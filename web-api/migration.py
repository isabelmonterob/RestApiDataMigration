import psycopg2
import csv
from config import DB_CONFIG

def csv_to_postgres(path, table):
    try:
        with psycopg2.connect(**DB_CONFIG) as con:
            with con.cursor() as cur:
                with open(path, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    
                    for row in reader:
                        if "" in row:
                            continue

                        placeholders = ", ".join(["%s"] * len(row))  # Genera '%s, %s, %s' según la cantidad de columnas
                        
                        query = f"INSERT INTO {table} VALUES ({placeholders})"
                        #print (query, row)
                        cur.execute(query, row)  # Insertar fila en la base de datos

                con.commit()
                print(f"Datos insertados correctamente en '{table}'.")

    except Exception as e:
        print(f"Error al insertar datos en '{table}': {e}")

#Insersión de datos de los csv
csv_to_postgres("sources\jobs.csv", "jobs")
csv_to_postgres("sources\departments.csv", "departments")
csv_to_postgres("sources\hired_employees.csv", "hired_employees")
