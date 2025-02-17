from sqlalchemy.orm import Session
from app.db.models import Departments, Jobs, HiredEmployees
from sqlalchemy import func
from app.db.schemas import HiredEmployeesCreate

#Departments
def get_department(db: Session, department_id: int):
    return db.query(Departments).filter(Departments.department_id == department_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Departments).offset(skip).limit(limit).all()

def delete_departments(db: Session):
    return db.query(Departments).delete()

#Jobs
def get_job(db: Session, job_id: int):
    return db.query(Jobs).filter(Jobs.job_id == job_id).first()

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Jobs).offset(skip).limit(limit).all()

def delete_jobs(db: Session):
    return db.query(Jobs).delete()

#Employees
def get_hired_employee(db: Session, employee_id: int):
    return db.query(HiredEmployees).filter(HiredEmployees.employee_id == employee_id).first()

def get_hired_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(HiredEmployees).offset(skip).limit(limit).all()

def delete_hired_employees(db: Session):
    res= db.query(HiredEmployees).delete()
    db.commit()
    return res

def create_hired_employees(db:Session, employee: HiredEmployeesCreate):
    max_id = db.query(func.max(HiredEmployees.employee_id)).scalar()
    new_employee_id = (max_id + 1) if max_id is not None else 1 
    new_employee = HiredEmployees(
        employee_id=new_employee_id,
        employee_name=employee.employee_name,
        date_hired=employee.date_hired,  
        department_id=employee.department_id,
        job_id=employee.job_id
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee) 
    return {"message": "Empleado contratado registrado", "employee": new_employee}