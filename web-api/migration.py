from migdb.mig_service import csv_to_postgres

#Insersión de datos de los csv
csv_to_postgres("../sources/jobs.csv", "jobs")
csv_to_postgres("../sources/departments.csv", "departments")
csv_to_postgres("../sources/hired_employees.csv", "hired_employees")