from mysql.connector import Error
import mysql.connector
from plotly import data


#
# def get_employees() :
#
#     try:
#         conn = mysql.connector.connect(
#             host="localhost", #adres serwera gdzie jest baza danych (podajemy localhost lub 127.0.0.1
#             user="root",
#             password="zanetAka8621@",
#             database="cwiczenia_db"
#         )
#
#         if conn.is_connected():
#             print("Nawiązano połączenie")
#         else:
#             raise Error("Nie połączono")
#
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM employees")
#         results = cursor.fetchall()
#         return results
#
#
#     except Error as e:
#         print(e)
#
#
# data = get_employees()
#
# print(data)
#
# for x in data:
#     print(f"{x.get("first_name")} {x.get("last_name")}")

def create_record(data):
    try:
        conn = mysql.connector.connect(
            host="localhost",  # lub "127.0.0.1",
            user="root",
            password="zanetAka8621@",
            database="weather_db"
        )
        if not conn.is_connected():
            raise Error("Nie połączono")

        cursor = conn.cursor(dictionary=True)

        sql = """
            INSERT INTO records 
            (temp,temp_feels_like,pressure,weather_desc,clouds,place,wind,created) 
            VALUES 
            (%s,%s,%s,%s,%s,%s,%s,NOW());
        """

        variables = (
            data["temp"],
            data["temp_feels_like"],
            data["pressure"],
            data["description"],
            data["clouds"],
            data["place"],
            data["wind"],
        )

        cursor.execute(sql, variables)
        conn.commit()
        print("Zapisano do MySQL")

    except Error as e:
        print(e)
    finally:
        conn.close()
        cursor.close()

