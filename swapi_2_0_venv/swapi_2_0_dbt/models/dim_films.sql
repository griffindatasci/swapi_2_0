with films as (
    select title from {{source('postgres', 'stg_films')}}
)

select *
from films
