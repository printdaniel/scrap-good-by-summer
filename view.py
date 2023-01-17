from scrap import AccuWeather
from base import base
import psycopg2

#  Base de datos db 

class DataEntry:
    def __init__(self):
        self.scrap = AccuWeather()

    def variables(self):
        temp =  self.scrap.temperatura()
        salida = self.scrap.salida_sol()
        entrada = self.scrap.entrada_sol()


    def entrada_datos(self):
        try:
            connection = psycopg2.connect(
                host="tempbase",
                database="db",
                user="daniel",
                password="1234"
            )
            cursor = connection.cursor()
            insert_query = "INSERT INTO medidas (temperatura, salida, entrada) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (temperatura, salida, entrada))
            connection.commit()
            print("Data inserted successfully into medidas table")
        except (Exception, psycopg2.Error) as error:
            print("Error while inserting data into medidas table", error)
        finally:
            #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
            

if __name__ == '__main__':
    dt = DataEntry()
    dt.variables()
