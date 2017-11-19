#!/usr/bin/env python
# _*_ coding: utf-8 _*_


class Vehicle(object):
    def __init__(self, brand, model, st_km, service_date):
        self.brand = brand
        self.model = model
        self.st_km = st_km
        self.service_date = service_date  # string in format "DD.MM.YYYY"

    def add_km(self, new_km):
        self.st_km += new_km

    def update_service_date(self, new_date):
        self.service_date = new_date


def list_all_vehicles(vehicles):
    if vehicles == []:
        print "There is not any vehicle yet entered in the program. Please add your first vehicle."
    else:
        for index, vehicle in enumerate(vehicles):
            print "%s) %s %s with %s km driven so far. Last service date: %s" % (index+1, vehicle.brand, vehicle.model,
                                                                                 vehicle.st_km, vehicle.service_date)


def create_vehicle_object(brand, model, st_km_str, service_date, vehicles):
    try:
        st_km_str = st_km_str.replace(",", ".")
        st_km = float(st_km_str)

        new_vehicle = Vehicle(brand=brand, model=model, st_km=st_km, service_date=service_date)

        vehicles.append(new_vehicle)

        return True
    except ValueError:
        return False


def add_new_vehicle(vehicles):
    brand = raw_input("Please enter the vehicle brand: ")
    model = raw_input("Please enter the model of the vehicle: ")
    st_km_str = raw_input("Please enter the number of driven kilometres: ")
    service_date = raw_input("Please enter the date of the last vehicle service (DD.MM.YYYY): ")

    result = create_vehicle_object(brand, model, st_km_str, service_date, vehicles)

    if result:
        print "You have successfully added a new vehicle %s %s!" % (brand, model)
    else:
        print "Please enter just a number for the kilometers done so far."


def choose_vehicle(vehicles):
    print "Select the number of the vehicle you'd like to edit: "
    print ""
    list_all_vehicles(vehicles)
    print ""
    selection = raw_input("What vehicle number would you like to choose?: ")
    return vehicles[int(selection) - 1]


def add_new_kilometers(vehicles):
    sel_vehicle = choose_vehicle(vehicles)

    print "Vehicle selected: %s %s is now %s." % (sel_vehicle.brand, sel_vehicle.model, sel_vehicle.st_km)
    print ""
    new_km_str = raw_input("How many kilometers would you like to add to the existing ones? (enter only a number): ")
    print ""

    try:
        new_km_str = new_km_str.replace(",", ".")
        new_km = float(new_km_str)

        sel_vehicle.add_km(new_km)
        print "New number of kilometers for %s %s is now: %s." % (sel_vehicle.brand, sel_vehicle.model,
                                                                  sel_vehicle.st_km)
    except ValueError:
        print "Please enter just a number for the kilometers you´d like to add."


def change_service_date(vehicles):
    sel_vehicle = choose_vehicle(vehicles)

    print "Vehicle selected: %s %s with service date: %s." % (sel_vehicle.brand, sel_vehicle.model,
                                                              sel_vehicle.service_date)
    print ""
    new_service_date = raw_input("What is the new general service date for this vehicle? (DD.MM.YYYY): ")
    print ""
    sel_vehicle.update_service_date(new_date=new_service_date)
    print "Service date updated!"


def delete_vehicle(vehicles):
    print "Select the number of the vehicle you'd like to delete: "
    print ""
    list_all_vehicles(vehicles)
    print ""
    selection = raw_input("What vehicle number would you like to choose?: ")
    selected_vehicle = vehicles[int(selection) - 1]

    vehicles.remove(selected_vehicle)
    print ""  # empty line
    print "The vehicle was successfully removed from your list."


def save_to_disc(vehicles):
    with open("vehicles.txt", "w+") as veh_file:
        for vehicle in vehicles:
            veh_file.write("%s,%s,%s,%s\n" % (vehicle.brand, vehicle.model, vehicle.st_km,
                                              vehicle.service_date))


def main():
    print "Welcome to the Vehicle Manager program."

    vehicles = []

    with open("vehicles.txt", "r") as v_file:
        for line in v_file:
            try:
                brand, model, st_km_str, service_date = line.split(",")
                create_vehicle_object(brand, model, st_km_str, service_date, vehicles)
            except ValueError:
                continue

    while True:
        print ""  # empty line
        print "Please choose one of these options: "
        print "a) See a list of all company vehicles."
        print "b) Add a new company vehicle."
        print "c) Edit the kilometers done for the chosen vehicle."
        print "d) Edit the last service date for the chosen vehicle."
        print "e) Delete a vehicle from company vehicles list."
        print "f) Quit the program."
        print ""  # empty line

        selection = raw_input("Eneter your selection (a, b, c, d, e or f): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_vehicles(vehicles)
        elif selection.lower() == "b":
            add_new_vehicle(vehicles)
        elif selection.lower() == "c":
            add_new_kilometers(vehicles)
        elif selection.lower() == "d":
            change_service_date(vehicles)
        elif selection.lower() == "e":
            delete_vehicle(vehicles)
        elif selection.lower() == "f":
            print "Thank you for using company vehicles list. Have a nice day."
            save_to_disc(vehicles)
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue


if __name__ == '__main__':
    main()
