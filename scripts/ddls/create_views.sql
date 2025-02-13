create or replace view vw_hiring_quartiles_2021 as
WITH tmp_quartiles AS (
    SELECT 
        he.employee_id, 
        d.department, 
        j.job,
        NTILE(4) OVER (ORDER BY he.date_hired ) AS Quartile
    FROM jobs j
    INNER JOIN hired_employees he ON j.job_id = he.job_id 
    INNER JOIN departments d ON he.department_id = d.department_id 
    WHERE he.date_hired BETWEEN '2021-01-01' AND '2021-12-31'
)
SELECT 
    department, 
    job,
    SUM(CASE WHEN Quartile = 1 THEN 1 ELSE 0 END) AS Q1,
    SUM(CASE WHEN Quartile = 2 THEN 1 ELSE 0 END) AS Q2,
    SUM(CASE WHEN Quartile = 3 THEN 1 ELSE 0 END) AS Q3,
    SUM(CASE WHEN Quartile = 4 THEN 1 ELSE 0 END) AS Q4
FROM tmp_quartiles
GROUP BY department, job
ORDER by department, job;
alter table vw_hiring_quartiles_2021 OWNER TO postgres;


create or replace view vw_department_counts_2021 as
WITH tmp_hired AS (
    SELECT 
        d.department_id, 
        d.department, 
        COUNT(he.employee_id) AS hired_count
    FROM hired_employees he 
    INNER JOIN departments d ON he.department_id = d.department_id 
    WHERE he.date_hired BETWEEN '2021-01-01' AND '2021-12-31'
    GROUP BY d.department_id, d.department
)
SELECT 
    department_id, 
    department, 
    hired_count
FROM tmp_hired
WHERE hired_count > (SELECT AVG(hired_count) FROM tmp_hired)
ORDER BY hired_count DESC;
alter table vw_department_counts_2021 OWNER TO postgres;