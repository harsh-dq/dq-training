from dotenv import load_dotenv
load_dotenv()
from db_conn import get_pg_connection



# mongodb connection object
pg = get_pg_connection()

pg.execute("""
    CREATE TABLE formdata(
    id serial,
    firstname varchar,
    lastname varchar,
    email varchar,
    comments text,
    createdon timestamp with time zone DEFAULT now()
);
""")