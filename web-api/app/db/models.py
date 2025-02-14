from sqlalchemy import Column, Integer, String, DateTime
from app.db.database import Base

class Jobs(Base):
    __tablename__ = "jobs"
    job_id = Column("job_id",Integer,primary_key=True, nullable=False)
    job=Column("job",String(50))

class Departaments(Base):
    __tablename__ = "departments"
    department_id = Column("department_id",Integer,primary_key=True, nullable=False)
    department = Column("department",String(50))

class HiredEmployees(Base):
    __tablename__ = "hired_employees"
    employee_id = Column("employee_id",Integer,primary_key=True, nullable=False)
    employee_name = Column("employee_name",String(50))
    date_hired=Column("date_hired",DateTime)
    department_id=Column("department_id",Integer)
    job_id=Column("job_id",Integer)

class View_Quartiles(Base):
    __tablename__ = "vw_hiring_quartiles_2021"
    __table_args__ = {'extend_existing': True}
    department =Column(String(50))
    job=Column(String(50))
    q1 = Column(Integer, default=1, nullable=True)
    q2= Column(Integer, default=1, nullable=True)
    q3= Column(Integer, default=1, nullable=True)
    q4= Column(Integer, default=1, nullable=True)
    __mapper_args__ = {"primary_key": [department, job]}

