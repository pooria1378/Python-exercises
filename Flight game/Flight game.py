import mysql.connector
import random
import math
from time import sleep
from geopy import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='pooria',
    password='hashemi1378',
    autocommit=True
)

def score_board(name, day, cost):
    # INSERT GAME SCORE TO SCORE BOARD
    sql = "insert into score_board(name, days_travelled, flight_ticket_cost)\n"
    sql += 'values("' + name + '", ' + str(day) + ", " + str(cost) + ")"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    # SHOW TOP 10 IN SCORE BOARD
    sql = 'select * from score_board '
    sql += 'order by days_travelled asc, flight_ticket_cost asc limit 10'
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"\n====== SCORE BOARD TOP 10 ======")
    for row in result:
        sleep(0.5)
        print(f"{row[0]}  |  {row[1]} days  |  {row[2]} EUR")
    return

def city_random_generator(continent_iso, radius, current_loc):
    sql = "select ident, airport.name, municipality, country.name, latitude_deg, longitude_deg from airport, country "
    sql += "where airport.iso_country=country.iso_country and type='large_airport' "
    sql += "and airport.continent='" + continent_iso + "' and country.name !='" + current_loc[3] + "'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #for row in result:
    #    print(row)
    #print(len(result))
    while True:
        city1 = random.choice(result)
        city23_list = []
        for row in result:
            if distance.distance(city1[4:6], row[4:6]).km <= radius and row[2] != city1[2]:
                city23_list.append(row)
        if len(city23_list) >= 2:
            #for row in city23_list:
            #    print(row[:-2])
            city2, city3 = random.sample(city23_list, 2)
            if city2[2] != city3[2]:
                break
    #print(len(city23_list))
    #print(f"{city1[:4]}\n{city2[:4]}\n{city3[:4]}")
    cities = [city1, city2, city3]
    return cities

def distance_sort(cities, current_loc):
    for city in cities:
        city_update = city + (distance.distance(city[4:6], current_loc[4:6]).km, )
        #print(city_update)
        cities[cities.index(city)] = city_update
    cities.sort(key=lambda x:x[-1])
    #print(cities)
    #for city in cities:
    #    print(city[:4] + (city[-1], ))
    return cities

def start_finish_location(icao):
    sql = "select ident, airport.name, municipality, country.name, latitude_deg, longitude_deg from airport, country\n"
    sql += "where airport.iso_country=country.iso_country and ident='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    #print(result[:4])
    return result

def ticket_option(cities, ticket, balance, earn_rate):
    while True:
        sleep(0.5)
        print(f"\nNext stops:")
        for n in range(3):
            print(f"{n + 1} - to {cities[n][2]}, {cities[n][3]}.\n"
                  f"    Ticket price: {ticket[n]} EUR. She can earn {int(ticket[n]*earn_rate)} EUR a day here.")
        sleep(0.5)
        print(f"\nAlisa's budget: {balance} EUR")
        i = input(f"Which ticket should she choose? ")
        if i == '1' or i == '2' or i == '3':
            break
    return i

def enough_money(i, balance, penalty, location, day_total, job):
    # NOT ENOUGH
    if balance < 0:
        day_penalty = math.ceil(abs(balance) / penalty)
        print(f"\nAlisa wants to buy ticket no.{i} but doesn't have enough money.")
        sleep(1)
        print("Unlucky for her, the locals are sick of Finnish language, it's just too hard!"
              f"\nShe has to stay in {location[2]} for {day_penalty} more days and works as a {random.choice(job)} for "
              f"{penalty} EUR per day to be able to buy this ticket.")
        balance = balance + day_penalty * penalty
        sleep(1)
        print(f"\n{day_penalty} days later, she's earned {day_penalty * penalty} EUR."
              f"\nAfter paying ticket, her balance: {balance} EUR")
        day_total = day_total + day_penalty
        print(f"Days spent on total trip: {day_total}")
        return balance, day_total
    # ENOUGH MONEY
    else:
        print(f"\nShe buys ticket no.{i} for {ticket[i - 1]} EUR. "
              f"\nHer balance: {balance} EUR.")
        return balance, day_total



#########       VARIABLES
day_total = 0
balance = 600
cost = 0
ticket = [150, 200, 300]
earn_rate = 0.2
job = ['waitress', 'cashier', 'barista', 'taxi driver']

#########        TITLE
title = '#         ALISA IN WONDERLAND         #'
print()
print("#" * len(title))
print(title)
print("#" * len(title))

#########     GAME ID
print("\n")
while True:
    game_id = input("Please enter your game ID: ")
    if game_id != "":
        break

###########        INTRO
sleep(2)
print(f'''\n    Alisa is just fresh out of high-school. She wants to spend some time before starting university
to explore the world. She doesn't have much money, but she is determined.''')
sleep(1)
print(f'''    "I can try to find some job at each destination to pay for the next trip." - Alisa thinks - " At least I 
can teach Finnish to the locals, eh?"''')
sleep(1)
print(f'''    As the enrollment for university approaching, she tries to go around the world with the shortest time, 
and maybe with the least money spent on flight tickets if possible. She wants to visit one city in each continent in order:
    Helsinki - EUROPE - AFRICA - ASIA - OCEANIA - NORTH AMERICA - SOUTH AMERICA - Helsinki''')

#########        SELECT START POINT
start = fin = start_finish_location("EFHK")
sleep(1)
print(f"\nAlisa is now at {start[1]}, checking flight tickets to Europe with {balance} EUR in her pocket.")

#########        RANDOM 3 CITIES IN EUROPE AND SORT DISTANCE FROM SHORT -> LONG
cities = city_random_generator("EU", 1000, start)
cities = distance_sort(cities, start)

#######     CHOOSE A CITY IN EUROPE 1/2/3
i = ticket_option(cities, ticket, balance, 0.2)

######### ASSIGN LOCATION, BALANCE, COST, SALARY BASE ON CHOICE
i = int(i)
location = cities[i-1]
#print(location)
balance = int(balance - ticket[i-1])
salary = int(ticket[i-1]/5)
cost = cost + ticket[i-1]

sleep(0.5)
print(f"\nShe buys ticket no.{i} for {ticket[i-1]} EUR. "
      f"\nHer balance: {balance} EUR.")

sleep(1)
print(f"\nThe flight takes her to {location[2]}, {location[3]}."
      f"\nWhile in there, she teaches Finnish at a language center for {salary} EUR a day.")

########## HOW MANY DAYS STAY
while True:
    sleep(1)
    day = input(f"\nHow many days would Alisa stay in {location[2]}? ")
    if day.isdigit() and int(day) >= 0:
        break

######## CALCULATE BALANCE AFTER N DAYS AND CALCULATE DAYS TRAVELLED TOTAL
day = int(day)
balance = balance + salary*day
day_total = day_total + day
sleep(0.5)
print(f"\n{day} days have passed, Alisa's earned {salary*day} EUR while staying there."
      f"\nHer balance: {balance} EUR"
      f"\nDays spent on the total trip: {day_total}")


########### CONTINENT: ISO, NAME, TICKET RATE COMPARE TO PREVIOUS
continent = [
    ('AF', 'Africa', 4),
    ('AS', 'Asia', 1.2),
    ('OC', 'Oceania', 1.2),
    ('NA', 'North America', 0.9),
    ('SA', 'South America', 0.8)
]

###################### CONTINENT LOOP
for cont in continent:
    penalty = math.ceil(salary/2)

    #########        RANDOM 3 CITIES IN CONT AND SORT DISTANCE FROM SHORT -> LONG
    cities = city_random_generator(cont[0], 1000, start)
    cities = distance_sort(cities, location)

    #########        MODIFY TICKETS BY RATIO
    for n in range(3):
        ticket[n] = int(ticket[n]*cont[2])

    ######### CHOOSE A TICKET 1 2 3 IN CONTINENT
    sleep(1)
    print(f"\nAlisa is now at {location[1]} checking flight ticket to {cont[1]} with {balance} EUR in her pocket.")
    i = ticket_option(cities, ticket, balance, 0.05)
    i = int(i)

    ######### CALCULATE BALANCE, COST AFTER BUY TICKET
    balance = balance - ticket[i-1]
    cost = cost + ticket[i-1]
    ########## NOT ENOUGH MONEY, 50% SALARY PENALTY, DAY PENALTY
    balance, day_total = enough_money(i, balance, penalty, location, day_total, job)

    ########### GO TO CHOSEN CITY, ASSIGN LOCATION, CALCULATE SALARY
    sleep(1)
    print(f"\nAlisa says goodbye to {location[2]}, {location[3]}.")
    location = cities[i - 1]
    salary = int(ticket[i-1]/20)
    penalty = math.ceil(salary/2)
    print(f"\nThe flight takes her to {location[2]}, {location[3]}."
          f"\nWhile in there, she teaches Finnish at a language center for {salary} EUR a day.")

    ########## HOW MANY DAYS STAY
    while True:
        sleep(1)
        day = input(f"\nHow many days would Alisa stay in {location[2]}? ")
        if day.isdigit() and int(day) >= 0:
            break

    ######## CALCULATE BALANCE AFTER N DAYS AND CALCULATE DAYS TRAVELLED TOTAL
    day = int(day)
    balance = balance + salary * day
    day_total = day_total + day
    sleep(0.5)
    print(f"\n{day} days have passed, Alisa's earned {salary * day} EUR while staying there."
          f"\nHer balance: {balance} EUR"
          f"\nDays spent on total trip: {day_total}")

######## OUT OF LOOP, FROM S.A. GOING BACK TO HELSINKI
sleep(2)
print(f"\nTime to go home, Alisa is looking for the ticket options from {location[2]} to {fin[2]}."
      f"\nHer balance: {balance} EUR")

##### RANDOM LAST TICKET TO HELSINKI
ticket_hel = round(random.uniform(ticket[0]*1.2, ticket[2]*1.2), -1)
sleep(1)
print(f"\nThe only ticket available costs {ticket_hel} EUR.")
balance = balance - ticket_hel
########## NOT ENOUGH MONEY, 50% SALARY PENALTY, DAY PENALTY
if balance < 0:
    day_penalty = math.ceil(abs(balance)/penalty)
    print(f"\nAlisa wants to buy ticket home but doesn't have enough money.")
    sleep(1)
    print("Unlucky for her, the locals are sick of Finnish language, it's just too hard!"
        f"\nShe has to stay in {location[2]} for {day_penalty} more days and works as a waitress for "
            f"{penalty} EUR per day to be able to buy this ticket.")
    balance = balance + day_penalty*penalty
    sleep(1)
    print(f"\n{day_penalty} days later, she's earned {day_penalty*penalty} EUR."
            f"\nAfter paying ticket, her balance: {balance} EUR")
    day_total = day_total + day_penalty
    print(f"Days spent on total trip: {day_total}")
   ########### ENOUGH MONEY
else:
    print(f"\nShe buys ticket home for {ticket_hel} EUR. "
            f"\nHer balance: {balance} EUR.")

########   OUTTRO
sleep(2)
print(f"\nFinally, Alisa's got home.")
sleep(2)
print(f"\nThe world tour is memorable but she doesn't forget how other people hate Finnish language!")
sleep(2)
print(f'''    "I'm wondering why?!" - she asks herself.''')

sleep(1)
print(f"\n#######################")
print(f"#         FIN         #")
print(f"#######################")


print(f"\n====== SUMMARY ======")
print(f"\nGame ID: {game_id}"
      f"\nDays spent on total trip: {day_total}"
      f"\nFlight ticket cost for total trip: {cost} EUR")

score_board(game_id, day_total, cost)