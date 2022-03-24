"""module for db operations"""
import psycopg2


def connect_to_db(db_name, db_user, db_password="TehP@rTVEL", host="127.0.0.1", port="5432"):
    """returns connection to db"""
    connection = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=host,
        port=port
    )
    print("Database opened successfully")
    return connection


def insert_record_to_crypto_table(connection, key, vector):
    """inserts record to Crypto table"""
    cur = connection.cursor()
    cur.execute(
        f'INSERT INTO "CryptoTestSchema"."Crypto" ("CryptoKey","InitVector") VALUES (\'{key}\', \'{vector}\')'
    )

    connection.commit()
    print("Record inserted successfully")

    connection.close()


def get_vector_key_pair(connection):
    cur = connection.cursor()
    cur.execute('SELECT "InitVector","CryptoKey" FROM "CryptoTestSchema"."Crypto" WHERE id IN (SELECT MAX(id) FROM "CryptoTestSchema"."Crypto")')

    data = {}
    rows = cur.fetchall()
    for row in rows:
        data['InitVector'] = row[0]
        data['CryptoKey'] = row[1]

    print("Operation done successfully")
    connection.close()
    return data
