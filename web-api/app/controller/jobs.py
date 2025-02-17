from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas
from app.service import crud
from app.db.database import SessionLocal

router = APIRouter(prefix="/jobs", tags=["Jobs"])

# Get DB local session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Jobs])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_jobs(db, skip=skip, limit=limit)

@router.get("/{job_id}", response_model=schemas.Jobs)
def read_job(job_id: int, db: Session = Depends(get_db)):
    data = crud.get_job(db, job_id=job_id)
    if data is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return data

@router.delete("/", response_model=list[schemas.Jobs])
def delete_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.delete_jobs(db, skip=skip)