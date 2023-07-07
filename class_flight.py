class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if self.open_seats() == 0:
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

peoples = ["Amar", "Harsh", "Swati", "Naman"]

for people in peoples:
    if flight.add_passenger(people) :
        print(f"{people} is added to the flight")
    else:
        print(f"{people} is not added to the flight, as it's full! ")


