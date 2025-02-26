from pydantic import BaseModel
from datetime import datetime

##JOBS
class JobsBase(BaseModel):
    job: str

class JobsCreate(JobsBase):
    pass

class Jobs(JobsBase):
    job_id: int

    class Config:
        from_attributes = True

##DEPARTMENTS
class DepartamentsBase(BaseModel):
    department: str

class DepartamentsCreate(DepartamentsBase):
    pass

class Departaments(DepartamentsBase):
    department_id: int

    class Config:
        from_attributes = True

#EMPLOYEES
class HiredEmployeesBase(BaseModel):
    employee_name: str
    date_hired: datetime
    department_id: int
    job_id: int

class HiredEmployeesCreate(HiredEmployeesBase):
    pass

class HiredEmployees(HiredEmployeesBase):
    employee_id: int

    class Config:
        from_attributes = True