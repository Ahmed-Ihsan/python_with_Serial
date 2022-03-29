import pandas as pd
import sqlite3


    
def create_SQL(name , vote):
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')
    conn.commit()
    
    data = {'name': name,
            'vote': vote
            }

    df = pd.DataFrame(data, columns= ['name','vote'])
    df.to_sql('products', conn, if_exists='replace', index = False)


def read_sql():
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')
    conn.commit()
    c.execute('''  
    SELECT * FROM products
            ''')

    return c.fetchall()

