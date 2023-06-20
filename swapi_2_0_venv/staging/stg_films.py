from scrapi import api_wan
from variables import database_name, database_user, database_host, database_port
from hidden import postgres_pwd
import psycopg2

films = api_wan("films")


# Create staging table in database
print(f"Creating database table.")
command = """
CREATE TABLE IF NOT EXISTS "stg_films" ( "title" CHAR(200), 
    "episode_id" CHAR(200), "opening_crawl"	CHAR(2000), "director"	CHAR(200), 
    "producer"	CHAR(200), "release_date" CHAR(200), "url" CHAR(200), 
    "created" CHAR(200), "edited" CHAR(200));
"""

with psycopg2.connect(database=database_name, 
                    user=database_user, 
                    password=postgres_pwd, 
                    host=database_host, 
                    port=database_port) as conn:
    cursor = conn.cursor()
    cursor.execute(command)
    conn.commit()


# Send data to table in database 
print("Sending data to database.")
command = """INSERT INTO stg_films VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""

with psycopg2.connect(database=database_name, 
                    user=database_user, 
                    password=postgres_pwd, 
                    host=database_host, 
                    port=database_port) as conn:
    cursor = conn.cursor()
    for film in films:
        cursor.execute(command, tuple([film["title"], film["episode_id"], film["opening_crawl"], 
                                       film["director"], film["producer"], film["release_date"], 
                                       film["url"], film["created"], film["edited"]]))
    conn.commit()

print("Data transfer complete.")