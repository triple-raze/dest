import psycopg2

conn = psycopg2.connect(
    dbname="shorturl",
    user="postgres",
    password="123321",
    host="localhost",
    port="5432"
)

def execsql(query, params=None, firstfield=False):
    result = None
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            
            try:
                if firstfield:
                    result = cur.fetchone()[0]      # [0] чтоб возвращало строку, а не кортеж
                else:
                    result = [var[0] for var in cur.fetchall()]       # row[0] т. к. cur.fetchall возвращает список кортежей, а нужен просто список
            except:
                result = None

        conn.commit()
    
    except Exception:
        print(f"error at query: {query}")
    
    return result

