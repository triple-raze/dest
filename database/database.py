import psycopg2
from os import getenv
from dotenv import load_dotenv

load_dotenv()       # инициализация .env

conn = psycopg2.connect(
    dbname = getenv('ENV_POSTGRES_DB'),
    user = getenv('ENV_POSTGRES_USER'),
    password = getenv('ENV_POSTGRES_PASSWORD'),
    host = 'db',
)


def execsql(query, params=None, firstfield=False):
    result = None
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            
            try:
                if firstfield:
                    result = cur.fetchone()[0]      # [0] чтоб возвращало строку, а не кортеж с одним значением
                else:
                    result = [var[0] for var in cur.fetchall()]       # row[0] т. к. cur.fetchall возвращает список кортежей, а нужен просто список
            except:
                result = None

        conn.commit()
    
    except Exception:
        print(f"error at query: {query}")
    
    return result

