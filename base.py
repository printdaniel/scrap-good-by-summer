import psycopg2

def base():
    """Creación y conección con la base de datos"""

    try:
        connection = psycopg2.connect(
            host="tempbase",
            database="db",
            user="daniel",
            password="1234"
        )
    
        cursor = connection.cursor()
    
        # Create table
        create_table_query = '''CREATE TABLE medidas (
                                    id SERIAL PRIMARY KEY,
                                    temperatura NUMERIC,
                                    salida NUMERIC,
                                    entrada NUMERIC
                                );'''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")
    
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

