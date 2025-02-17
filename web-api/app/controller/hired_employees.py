from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas
from app.service import crud
from app.db.database import SessionLocal
from app.db.schemas import HiredEmployees, HiredEmployeesCreate
from sqlalchemy import func


router = APIRouter(prefix="/hired_employees", tags=["HiredEmployees"])

# Get DB local session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.HiredEmployees])
def read_hired_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_hired_employees(db, skip=skip, limit=limit)
    return [
        {
            "employee_id": emp.employee_id,
            "employee_name": emp.employee_name,
            "date_hired": emp.date_hired.isoformat() if emp.date_hired else None,  # Convert to string
            "department_id": emp.department_id,
            "job_id": emp.job_id
        }
        for emp in employees
    ]

@router.get("/{employee_id}", response_model=schemas.HiredEmployees)
def read_department(employee_id: int, db: Session = Depends(get_db)):
    data = crud.get_hired_employee(db, employee_id=employee_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return data

@router.delete("/", response_model=list[schemas.HiredEmployees])
def delete_hired_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.delete_hired_employees(db, skip=skip)

@router.post("/")
def create_hired_employee(employee: HiredEmployeesCreate, db: Session = Depends(get_db)):
    max_id = db.query(func.max(HiredEmployees.employee_id)).scalar()
    new_employee_id = (max_id + 1) if max_id is not None else 1  # Si la tabla está vacía, empieza en 1

    new_employee = HiredEmployees(
        employee_id=new_employee_id,
        employee_name=employee.employee_name,
        date_hired=employee.date_hired,  
        department_id=employee.department_id,
        job_id=employee.job_id
    )
    
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)  # Para obtener los datos después de la inserción
    
    return {"message": "Empleado contratado registrado", "employee": new_employee}