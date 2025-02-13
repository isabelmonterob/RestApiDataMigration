--drop TABLE jobs cascade;
CREATE TABLE public.jobs (
    job_id int NOT NULL,
    job VARCHAR(50) NOT null,
    CONSTRAINT "jobs_pk" PRIMARY KEY ("job_id")
);
ALTER TABLE public.jobs OWNER TO postgres;

--drop TABLE departments cascade;
CREATE TABLE public.departments (
    department_id int NOT NULL,
    department VARCHAR(50) NOT null,
    CONSTRAINT "department_pk" PRIMARY KEY ("department_id")
);
ALTER TABLE public.departments OWNER TO postgres;

--drop TABLE hired_employees cascade;
CREATE TABLE public.hired_employees (
    employee_id int NOT NULL,
    employee_name VARCHAR(50) NOT NULL,
    date_hired timestamp NOT null,
    department_id int,
    job_id int,
    CONSTRAINT "hired_employees_pk" PRIMARY KEY ("employee_id"),
    CONSTRAINT "hired_employees_departments_fk" FOREIGN KEY ("department_id") REFERENCES public.departments ("department_id"),
    CONSTRAINT "hired_employees_jobs_fk" FOREIGN KEY ("job_id") REFERENCES public.jobs ("job_id")

);
ALTER TABLE public.hired_employees OWNER TO postgres;