# DataChallengeGlbnt

### Requeriments

- Python 3.10.4
- Postgres 13

### Create DB and objects
Excecute sql files in the next order:
1. `scripts/ddls/create_db.sql`
2. `scripts/ddls/create_table.sql`
3. `scripts/ddls/create_views.sql`

### Copy information to DB
1. Add csv files in `sources` folder
2. Configure DB credentials in `web-api/config.py`
3. Excecute `web-api/migration.py`