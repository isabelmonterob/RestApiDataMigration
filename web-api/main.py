from fastapi import FastAPI
from app.utility.config import APP_PORT, APP_DEBUG
from app.controller import departments, jobs, hired_employees

app = FastAPI(debug=APP_DEBUG)

# Registrar los routers
app.include_router(departments.router)
app.include_router(jobs.router)
app.include_router(hired_employees.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=APP_PORT)
