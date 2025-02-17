from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas
from app.service import crud
from app.db.database import SessionLocal

router = APIRouter(prefix="/departments", tags=["Departments"])

# Get DB local session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Departaments])
def read_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_departments(db, skip=skip, limit=limit)

@router.get("/{department_id}", response_model=schemas.Departaments)
def read_department(department_id: int, db: Session = Depends(get_db)):
    data = crud.get_department(db, department_id=department_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return data

@router.delete("/", response_model=list[schemas.Departaments])
def delete_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.delete_departments(db, skip=skip)