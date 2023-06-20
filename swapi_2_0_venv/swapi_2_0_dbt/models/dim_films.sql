{{ config(materialized='table') }}

with films as (

    select * from {{source('swapi_2_0_dbase', 'stg_films')}}

)

select *
from films
