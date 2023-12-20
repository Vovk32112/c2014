import random

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class Person:
    def __init__(self, name="Person"):
        self.name = name
        self.money, self.happiness, self.satiety = 100, 50, 50
        self.home, self.vehicle, self.job = {"food": random.randint(0, 100), "mess": random.randint(1, 70)}, Auto(brand_of_car), None

    def acquire_home(self):
        self.home = {"food": random.randint(0, 100), "mess": random.randint(1, 70)}

    def find_job(self):
        if self.vehicle.drive():
            self.job = {"salary": random.randint(30, 70), "happiness_loss": random.randint(1, 25)}
        else:
            self.repair()

    def clean_home(self):
        self.happiness -= 5
        self.home["mess"] = 0

    def repair(self):
        self.vehicle.strength += 100
        self.money -= 50

    def show_indexes(self, day):
        day_info = f"Today is the {day} of {self.name}'s life"
        print(f"{day_info:=^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Happiness - {self.happiness}")
        print(f"Satiety - {self.satiety}")
        home_indexes = "Home_indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home['food']}")
        print(f"Mess - {self.home['mess']}")
        vehicle_indexes = f"{self.vehicle.brand} vehicle indexes"
        print(f"{vehicle_indexes:^50}", "\n")
        print(f"Fuel - {self.vehicle.fuel}")
        print(f"Strength - {self.vehicle.strength}")

    def is_alive(self):
        if any(value < 0 for value in [self.happiness, self.satiety, self.money]):
            print("Depression" if self.happiness < 0 else "Dead" if self.satiety < 0 else "Bankrupt")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home["food"] == 0:
            print("Settled in the house")
            self.acquire_home()
        if self.job is None:
            self.find_job()
            print(f"I don't have a job, I'm going to get a job with salary {self.job['salary']}")
        self.show_indexes(day)
        dice = random.randint(1, 4)


    def purchase(self, manage):
        if self.vehicle.drive():
            cost = 100 if manage == "fuel" else 50
            print(f"I bought {manage}")
            self.money -= cost
            self.home["food"] += random.randint(0, 100) if manage == "food" else 0
            self.vehicle.fuel += 100 if manage == "fuel" else 0

brand_of_car = {
    "Honda": {"fuel": 90, "strength": 80, "consumption": 11},
    "Ford": {"fuel": 60, "strength": 70, "consumption": 9},
    "Chevrolet": {"fuel": 75, "strength": 100, "consumption": 10},
    "Tesla": {"fuel": 0, "strength": 120, "consumption": 5}
}

person = Person(name="John")
for day in range(1, 8):
    if not person.live(day):
        break
