cities = {"Beirut", "Saida", "Tyre", "Jbeil", "Tripoli"}
drivers = {"Ali":["Beirut", "Saida", "Tyre"], "Moussa":["Jbeil", "Beirut"], "Ahmad":["Tripoli", "Jbeil", "Beirut"]}
print(cities)
print(drivers)
def displayMainMenu():
    print("Enter:\n1. To add a city\n2. To add a driver\n3. To add a city to the route of a driver\n4. Remove a city from a driver's route\n5. To check the deliverability of a package")

def addCity():
    user_city = input("Add a city: ").capitalize()
    if user_city not in cities:
        cities.add(user_city)
        print(f"{user_city} was added.")
        print(cities)
    else:
        print(f"{user_city} already exists.")

def addDriver():
    user_driver = input("Enter the name of the driver: ").capitalize()
    driver_cities = []
    if user_driver not in drivers:
        while True:
            user_city = input("Enter a city to add to the driver's route: ").capitalize()
            if user_city in cities:
                if user_city not in driver_cities:
                    driver_cities.append(user_city)
                    print(f"{user_city} was added.")
                else:
                    print(f"{user_city} is already on {user_driver}'s route.")
            else:
                print("City is not available.")
            continue_choice = int(input("Would you like to add more?\n1. Yes\n2. No\nChoice: "))
            if continue_choice == 1:
                continue
            elif continue_choice == 2:
                break
            else:
                print("Invalid input.")
        new_driver = {user_driver: driver_cities}
        drivers.update(new_driver)
        print(f"{user_driver} was added.")
        print(drivers)
    else:
        print(f"{user_driver} already exists.")
    
def addCityToRoute():
    user_driver = input("Enter the name of the driver: ").capitalize()
    if user_driver in drivers:
        user_city = input("Enter a city to add to the driver's route: ").capitalize()
        if user_city in cities:
            if user_city not in drivers[user_driver]:
                print("Input:\n0. To add to the beginning of the route\n-1. To add to the end of the route\n#. (any other number) to add that city to the given index")
                index = int(input("Choice: "))
                if index <= len(drivers[user_driver]):
                    drivers[user_driver].insert(index, user_city)
                    print(f"{user_city} was added to {user_driver}'s route.")
                    print(drivers)
                else:
                    print("Index out of range.")
            else:
                print(f"{user_city} is already on {user_driver}'s route.")
        else:
            print("City is not available.")
    else:
        print("Driver not found.") 

def removeCity():
    user_driver = input("Enter the name of the driver: ").capitalize()
    if user_driver in drivers:
        user_city = input("Enter a city to remove from the driver's route: ").capitalize()
        if user_city in cities:
            if user_city in drivers[user_driver]:
                drivers[user_driver].remove(user_city)
                print(f"{user_city} was removed from {user_driver}'s route.")
                print(drivers)
            else:
                print(f"{user_city} is not on {user_driver}'s route.")
        else:
            print("City is not available.")
    else:
        print("Driver not found.")

def checkDeliverability():
    user_city = input("Enter the city you'd like to dilever the package to: ").capitalize()
    if user_city in cities:
        print(f"Drivers that deliver to {user_city}: ")
        for driver, route in drivers.items():
            if user_city in route:
                print(driver)
    else:
        print("City is not available.")

def main():
    while True:
        displayMainMenu()
        choice = int(input("Choice: "))
        if choice == 1:
            addCity()
        elif choice == 2:
            addDriver()
        elif choice == 3:
            addCityToRoute()
        elif choice == 4:
            removeCity()
        elif choice == 5:
            checkDeliverability()
        else:
            print("Invalid input")

main()