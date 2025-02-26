from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas
from app.service import crud_service
from app.db.database import SessionLocal
from app.db.schemas import HiredEmployeesCreate

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
    employees = crud_service.get_hired_employees(db, skip=skip, limit=limit)
    return [
        {
            "employee_id": emp.employee_id,
            "employee_name": emp.employee_name,
            "date_hired": emp.date_hired.isoformat() if emp.date_hired else None, 
            "department_id": emp.department_id,
            "job_id": emp.job_id
        }
        for emp in employees
    ]

@router.get("/{employee_id}", response_model=schemas.HiredEmployees)
def read_department(employee_id: int, db: Session = Depends(get_db)):
    data = crud_service.get_hired_employee(db, employee_id=employee_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return data

@router.delete("/", response_model=list[schemas.HiredEmployees])
def delete_hired_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_service.delete_hired_employees(db, skip=skip)

@router.post("/")
def create_hired_employee(employee: HiredEmployeesCreate, db: Session = Depends(get_db)):
    return crud_service.create_hired_employees(db, employee)