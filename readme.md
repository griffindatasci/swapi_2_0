
1. Go to github and create repository for project
1. Clone github repo to local machine:
    1. `cd` to host directory on local machine
    1. `git clone <https://github.com/<git_username>/<repo_name>.git>` 
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
    1. Edit the <dbt_project_name> section to:
    
```
swapi_2_0_dbt:
  outputs:

    dev:
      type: postgres
      threads: 4
      host: localhost
      port: 5432
      user: postgres
      pass: <postgres_password>
      dbname: <database_name>
      schema: postgres

  target: dev
```

### Variables:

- `git_username`: griffindatasci
- `repo_name`: swapi_2_0
- `env_name`: swapi_2_0_venv
- `dbt_project_name`: swapi_2_0_dbt
- `computer_user`: Griff-Kauff
- `database_name`: swapi_2_0_dbase
