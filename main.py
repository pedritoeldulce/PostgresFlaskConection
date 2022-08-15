import psycopg2
from config import config


def connect():

    conn = None

    try:
        params = config()  # lectura delos parametros de conexion

        print("Conectando a la Base de Datos  Postgrest ...")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()  # crea el cursor, sirve para hacer cualquir tipo de operacion sobre una bd

        print("PosrgreSQL database version: ")
        cur.execute("SELECT version()")  # sintaxis de la consulta

        db_version = cur.fetchone()
        print(db_version)

        cur.close()  # Cierre de comunicación con Postgres

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Database Conection close")


if __name__ == '__main__':
    connect()

