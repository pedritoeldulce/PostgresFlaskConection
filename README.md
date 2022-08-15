1) Se almacena la configuración a la base de datos en un archivo .ini `database.ini` u otro tipo de archivo utilizado para almacenar configuraciones
- NOTA: Extensión .ini sirve para identificar los archivos de inicializacion/configuracion __(.ini)__ en Micfosoft y otros SO. No se incluyó el puerto ya que se tomará por defecto host=5432

ejemplo:
    
    [postgresql]
    host:localhost
    database:db_tienda
    user:postgres
    password:mypass

2) Creamos una función llamada __config()__ que lea los archivos de `database.ini` y devuelva los parametros de conexión.


    from configparser import ConfigParser
    
    def config(filename='database.ini', section='postgresql')
         
        # crea el parser y lee el archivo
        parser = ConfigParser()
        parser.read(filename)

        # obtiene la seccion de la conexion
        db={}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found un the {1} file'.format(section, filename))

        return db
            

- section: es la seccion para identificar a los parámetros.
- read(): lee el archivo __database.ini__, si existe el archivo devuelve una lista
- variable params: devuelve una lista de tuplas de la cual solo se guarda los primeros valores en la lsita db

* __configparser__: módulo qye provee la clase ConfigParser usado para gestionar archivos de configuración editables por 
el usuario.

3) creamos una función donde vamos a conectarnos con la BD.
3.1) importamos el paquete psycopg2: archivo que nos ayudará a conectar con la BD
3.2) importamos el archivo de configuracion (creadenciales)


    import psycopg2
    from config import config
    
    def conectar():

        conexion = None
        try:
            params = config()
            print("Conectando a la BD Postgres")
            conn = psycopg2.connect(**params)
            
            cur = conn.cursor()
            
            # ejecución de una consulta en SQL
            cur.cursor("SELECT version()") # obtiene la version de Postgres
    
            version = cur.fetchone() # tras la lectura, obtiene el primer registro o el único que exista
    
            cur.close()  # Cierre de comunicacion con Postgres
    
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
        finally:
            if conexion is not None:
                conn.close()
                print("Conexion finalizado")
    
    if __name__ == '__main__':
    conectar()