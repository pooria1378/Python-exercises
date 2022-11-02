import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='pooria',
    password='hashemi1378',
    autocommit=True
)
def getAirportsByCountry(country):
    sql = "SELECT ident, type, name, iso_country from airport"
    sql += " WHERE iso_country='" + country + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    result.sort(key=lambda x:x[1])
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[3]}, {row[1]}, {row[2]}, ICAO code: {row[0]}")
    return

country = input("Enter country code: ")
getAirportsByCountry(country)