### Initial Setup 

1. Go to github and create repository for project
1. Clone github repo to local machine:
    1. `cd` to host directory on local machine
    1. `git clone <https://github.com/<git_username>/<repo_name>.git>` 
    1. `git branch -b <branch_name>` to branch the from main
1. Create and open readme.md:
    1. `cd` to github directory (directory cloned in previous step)
    1. `cp NUL readme.md`
    1. `code readme.md`
1. Inititate and activate Python virtual environment:
    1. `python -m venv <env_name>`
    1. `cd <env_name>/scripts`
    1. `activate`
    1. `cd ..`
    - Repeat last three steps whenever activating the environment
1. Install DBT and initiate DBT project:
    - In the active virtual environment
    1. `pip install dbt-core dbt-postgres`
    1. `dbt init <dbt_project_name>`
    1. Select postgres
1. Edit profiles.yml:
    1. Go to C://Users//<computer_user>//.dbt in file explorer and open profiles.yml
    1. Edit the <dbt_project_name> dev section to:
        - threads: 4
        - host: localhost
        - port: 5432
        - user: <postgres_username>
        - pass: <postgres_password>
        - dbname: <database_name>
        - schema: postgres
1. Initiate Postgres database
    - In DBT project directory
    1. `psql -U <postgres_username>`
    1. `CREATE DATABASE <database_name> WITH ENCODING 'UTF8' LC_COLLATE='English_United Kingdom' LC_CTYPE='English_United Kingdom';`
    1. `\c <database_name>`
    1. `GRANT TEMP ON DATABASE <database_name> TO <postgres_username>;`
    1. `GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO <postgres_username>` 
    1. `GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO <postgres_username>;` 
    1. `GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO <postgres_username>;`
    1. Open Control Panel > System & Security > Administrative Tools > ODBC Data Sources > Add
    1. Set database to <database_name> and port to *5432*, server to *localhost*, username to <postgres_username> amd password to <postgres_password>
    1. In advanced options check *Use Declare/Fetch* and *bytea as LO* 
    1. Click Apply > OK > Save > Test
    1. Click Test
    1. `\q` to quit psql
1. Test DBT
    - In command prompt, dbt project directory with venv active
    1. `dbt debug`
    1. `dbt run`
    1. Open PGAdmin4
    1. Open PostgreSQL <Version> Server > Databases > <database_name> > Schemas > Postgres > Tables: This should contain my_first_dbt_model table



### Adding data and tables to DBT project

- Add python script to scrape and stage data
- Add <model>.sql for dim/fct tables in models (note: `{{source(<postgres_username>, <source_name>)}}`)
- Add <model>.yml for each model in models
- Add sources.yml (name: <postgres_username>, database: <database_name>)


### TODO:

- ISSUE: outputting data somewhere, just not arriving in the swapi_2_0_dbase database in PGAdmin4. Will figure this out later - likely a config issue.
- Add dim_* and fct_* SQL and YAML files

### Variables:

- `branch_name`: development
- `computer_user`: Griff-Kauff
- `database_name`: swapi_2_0_dbase
- `dbt_project_name`: swapi_2_0_dbt
- `env_name`: swapi_2_0_venv
- `git_username`: griffindatasci
- `postgres_username`: postgres  
- `repo_name`: swapi_2_0


