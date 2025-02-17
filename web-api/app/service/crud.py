from sqlalchemy.orm import Session
from app.db.models import Departments, Jobs, HiredEmployees

#Departments
def get_department(db: Session, department_id: int):
    return db.query(Departments).filter(Departments.department_id == department_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Departments).offset(skip).limit(limit).all()

def delete_departments(db: Session, skip: int = 0):
    return db.query(Departments).delete()

#Jobs
def get_job(db: Session, job_id: int):
    return db.query(Jobs).filter(Jobs.job_id == job_id).first()

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Jobs).offset(skip).limit(limit).all()

def delete_jobs(db: Session, skip: int = 0):
    return db.query(Jobs).delete()

#Employees
def get_hired_employee(db: Session, employee_id: int):
    return db.query(HiredEmployees).filter(HiredEmployees.employee_id == employee_id).first()

def get_hired_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(HiredEmployees).offset(skip).limit(limit).all()

def delete_hired_employees(db: Session, skip: int = 0):
    res= db.query(HiredEmployees).delete()
    db.commit()
    return res