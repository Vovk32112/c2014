import random

class Im:
    def __init__(self, name="Im", bike=None, hobby=None, home=None):
        self.name = name
        self.money = 50
        self.happiness = 70
        self.hunger = 50
        self.home = home
        self.bike = bike
        self.hobby = hobby

    def get_home(self):
        self.home = House()

    def get_bike(self):
        self.bike = Bike()

    def play_video_games(self):
        print("Пограю у плейстейшн")
        self.happiness += 15

    def eat_snack(self):
        print("Буду їсти чіпси")
        self.hunger += 5
        self.money -= 3

    def do_homework(self):
        print("Знову робити домашню роботу...")
        self.happiness -= 5
        self.hunger -= 5

    def go_outside(self):
        print("Піду погуляю")
        self.happiness += 15
        self.hunger -= 3

    def buy_video_game(self):
        print("Кплю собі нову відеогру")
        self.home.video_games += 1
        self.money -= 15
        self.happiness += 10





    def days_indexes(self, day):
        dice = random.randint(1, 5)
        if dice == 1:
            self.play_video_games()
        elif dice == 2:
            self.eat_snack()
        elif dice == 3:
            self.do_homework()
        elif dice == 4:
            self.go_outside()
        elif dice == 5:
            self.buy_video_game()
        day_info = f"Today is the {day}th day of {self.name}'s life"
        print(f"{day_info:=^50}\n")
        kid_indexes = f"{self.name}'s indexes"
        print(f"{kid_indexes:^50}\n")
        print(f"Money - {self.money}")
        print(f"Happiness - {self.happiness}")
        print(f"Hunger - {self.hunger}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}\n")
        print(f"Video Games - {self.home.video_games}")
        print(f"Room Mess - {self.home.mess}")


    def is_alive(self):
        if self.happiness <= 0:
            print("Depressed")
            return False
        if self.hunger <= 0:
            print("Starved")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            print("Moved into a new house")
            self.get_home()
        if self.bike is None:
            print("Got a new bike!")
            self.get_bike()

        self.days_indexes(day)
        action = random.choice(["грати_у_відеоігри", "істи_чіпси", "робити_домашню_роботу", "іти_гуляти", "гупувати_відеоігри"])
        if hasattr(self, action):
            getattr(self, action)()

        return True


class Bike:
    def __init__(self):
        self.condition = 100


class House:
    def __init__(self):
        self.video_games = 0
        self.mess = 0


if __name__ == "__main__":
    Artur = Im(name="Артур")

    for day in range(1, 8):
        if not Artur.live(day):
            break
