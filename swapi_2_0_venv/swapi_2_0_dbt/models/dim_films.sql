{{ config(materialized='table') }}


with films as (
    select title, episode_id, opening_crawl, director, producer, release_date, url, created, edited 
    from {{source('postgres', 'stg_films')}}
)

select *
from films
