import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='pooria',
    password='hashemi1378',
    autocommit=True
)
from geopy import distance

def distanceBetween2Airports(icao1, icao2):
    airports = []
    deg = []
    sql = "SELECT ident, name, iso_country, latitude_deg, longitude_deg from airport"
    sql1 = sql + " WHERE ident='" + icao1 + "'"
    print(sql1)
    sql2 = sql + " WHERE ident='" + icao2 + "'"
    print(sql2)
    cursor = connection.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    airports.extend(result)
    cursor.execute(sql2)
    result = cursor.fetchall()
    airports.extend(result)
    #print(airports)
    for i in airports:
        print(f"{i[0]}, {i[2]}, {i[1]}")
        n = (i[3], i[4])
        deg.append(n)
    #print(deg)
    return distance.distance(deg[0], deg[1]).km

icao1 = input("1st airport's ICAO code: ")
icao2 = input("2nd airport's ICAO code: ")
print(f"Distance between these 2 airports is {distanceBetween2Airports(icao1, icao2):.2f} km")
