import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv


load_dotenv()


def get_pg_connection():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.set_session(autocommit=True)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print('PG Database connected...',cur)
        return cur
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    get_pg_connection()