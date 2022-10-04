airports = {"EGLL":"London Heathrow Airport", "RJTT":"Tokyo International Airport", "KLAX":"Los Angeles International Airport","EFHK":"Helsinki-Vantaa Airport"}
user_ask = True
while user_ask:
    user_option = input("Choose what do you want to do: New airport, Existing airport or quit. ").lower()
    if user_option == "new airport":
        icao = input("Enter the ICAO code: ").upper()
        airport_name = input("Enter the name of the airport: ").upper()
        airports[icao] = airport_name
    elif user_option == "existing airport":
        icao_exist = input("What is the ICAO of the airport? ").upper()
        print(airports[icao_exist])
    elif user_option == "quit":
        user_ask = False
    else:
        print("Wrong entry!")
print(airports)