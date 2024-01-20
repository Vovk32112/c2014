import random

class Artur:
    def __init__(self, name="Артур", hobby=None, home=None, pet=None):
        self.name = name
        self.money = 60
        self.happiness = 70
        self.hunger = 50
        self.home = home
        self.hobby = hobby
        self.progress = 15
        self.energy = 50
        self.pet = pet

    def get_cat(self):
        self.pet = Cat()


    def get_home(self):
        self.home = House()

    def play_video_games(self):
        print("Пограю у плейстейшн")
        self.happiness += 15
        self.home.mess += 5

    def go_to_sleep(self):
        print("Піду посплю")
        self.happiness += 10
        self.hunger += 15
        self.energy += 30

    def eat_snack(self):
        print("Буду їсти чіпси")
        self.hunger -= 5
        self.money -= 3

    def do_homework(self):
        print("Знову робити домашню роботу...")
        self.happiness -= 5
        self.hunger += 5
        self.energy -= 10

    def go_outside(self):
        print("Піду погуляю")
        self.happiness += 15
        self.hunger += 5
        self.energy -= 10

    def buy_video_game(self):
        if self.money >= 40:
            print("Куплю собі нову відеогру")
            self.money -= 10
            self.happiness += 10
            self.home.video_games += 1
        else:
            print("Я хотів купити нову відео гру але мені не вистачає")
            self.happiness -= 5


    def friend_to_home(self):
        print("Покличу друзів до себе додому")
        self.home.mess += 16
        self.hunger += 12
        self.energy -= 5

    def Clean_up(self):
        print("Я поприбирав")
        self.home.mess -= 10
        self.happiness -= 10
        self.energy -= 15

    def eat(self):
        print("Я поїв")
        self.hunger -= 20

    def get_progress(self):
        print("Піду позаймаюсь")
        self.progress += 15
        self.energy -= 5

    def progress_in_it_step(self):
        print("Піду позаймаюсь у IT STEP")
        self.progress += 30
        self.energy -= 10

    def cat_eat(self):
        print("Погодую Мурзика")
        self.happiness -= 2
        self.pet.cat_hunger -= 10
        self.pet.cat_happiness += 5

    def cat_play(self):
        print("Пограюсь з мурзиком")
        self.energy -= 10
        self.happiness += 10
        self.pet.cat_happiness +=10
        self.pet.cat_hunger += 5

    def cat_eat_chocolate(self):
        self.pet.cat_health -= 10
        self.pet.cat_hunger -= 5
        self.pet.cat_happiness += 10
        print("Кіт з'їв шоколад")

    def cat_treat(self):
        print("Мені треба відвезти кота до ветеринара")
        if self.money <= 20:
            print("Мені не вистачає на лікування кота. Продам свою відеогру")
            self.home.video_games -= 1
            self.money += 10
            self.happiness -= 20
            if self.money >= 20:
                self.money -= 20
                self.happiness -= 20
                self.pet.cat_happiness -= 20
                print("Я вилікував Мурзика")
            else:
                self.home.video_games -= 1
                self.money += 15
        if self.money >= 20:
            self.money -= 20
            self.happiness -= 20
            self.pet.cat_happiness -= 20
            print("Я вилікував Мурзика")
        print()
        if self.home.video_games <= -1:
            print(f"Video Games - {self.home.video_games}")
            print("Я взяв у кредит")

    def days_indexes(self, day):
        day_info = f"Today is the {day}th day of {self.name}'s life"
        print(f"{day_info:=^50}\n")
        kid_indexes = f"{self.name}'s indexes"
        print(f"{kid_indexes:^50}\n")
        print(f"Money - {self.money}")
        print(f"Progress - {self.progress}")
        dice = random.randint(1, 10)
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
        elif dice == 6:
            self.friend_to_home()
        elif dice == 7:
            if self.hunger >= 90:
                pass
            else:
                self.eat()
        elif dice == 8:
            if self.progress >= 50:
                pass
            else:
                self.get_progress()
        elif dice == 9:
            if self.progress >= 50:
                pass
            else:
                self.progress_in_it_step()
        elif dice == 10:
            if self.energy >= 90:
                pass
            else:
                self.go_to_sleep()
        if self.happiness <= 0:
            print("У мене дипресія")
        if self.progress >= 50:
            print("Я закінчив навчання у IT STEP")
        health_indexes = "health indexes"
        print(f"{health_indexes:^50}\n")
        print(f"Happiness - {self.happiness}")
        print(f"energy - {self.energy}")
        if self.energy <= 10:
            self.go_to_sleep()
        if self.hunger == -1:
            self.hunger += 1
        elif self.hunger == -2:
            self.hunger +=2
        elif self.hunger == -3:
            self.hunger +=3
        elif self.hunger == -4:
            self.hunger +=4
        elif self.hunger == -5:
            self.hunger +=5
        elif self.hunger == -6:
            self.hunger +=6
        elif self.hunger == -7:
            self.hunger +=7
        elif self.hunger == -8:
            self.hunger +=8
        elif self.hunger == -9:
            self.hunger +=9
        elif self.hunger == -10:
            self.hunger +=10
        elif self.hunger == -11:
            self.hunger +=11
        elif self.hunger == -12:
            self.hunger +=12
        elif self.hunger == -13:
            self.hunger +=13
        elif self.hunger == -14:
            self.hunger +=14
        elif self.hunger == -15:
            self.hunger +=15
        print(f"Hunger - {self.hunger}")
        if self.hunger >= 51:
            print("Треба поїсти")
            self.eat()
        if self.hunger <= 50:
            print("Я не голодний")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}\n")
        print(f"Video Games - {self.home.video_games}")
        print(f"Room Mess - {self.home.mess}")
        if self.home.mess == -1:
            self.home.mess += 1
        elif self.home.mess == -2:
            self.home.mess +=2
        elif self.home.mess == -3:
            self.home.mess +=3
        elif self.home.mess == -4:
            self.home.mess +=4
        elif self.home.mess == -5:
            self.home.mess +=5
        elif self.home.mess == -6:
            self.home.mess +=6
        elif self.home.mess == -7:
            self.home.mess +=7
        elif self.home.mess == -8:
            self.home.mess +=8
        elif self.home.mess == -9:
            self.home.mess +=9
        elif self.home.mess == -10:
            self.home.mess +=10
        elif self.home.mess == -11:
            self.home.mess +=11
        elif self.home.mess == -12:
            self.home.mess +=12
        elif self.home.mess == -13:
            self.home.mess +=13
        elif self.home.mess == -14:
            self.home.mess +=14
        elif self.home.mess == -15:
            self.home.mess +=15
        if self.home.mess >= 30:
            print("Треба поприбирати")
            self.Clean_up()
        if self.home.mess <= 15:
            print("У моїй кімнаті прибрано")
        if self.home.video_games <= -1:
            print("Я взяв у кредит")
        cat_indexes = "Cat indexes"
        print(f"{cat_indexes:^50}\n")
        cat_dice = random.randint(1, 3)
        print(f"cat_happiness - {self.pet.cat_happiness}")
        if self.pet.cat_hunger <= 0:
            self.pet.cat_hunger += 10
        print(f"cat_hunger - {self.pet.cat_hunger}")
        if cat_dice == 1:
            self.cat_eat()
        elif cat_dice == 2:
            self.cat_play()
        elif cat_dice == 3:
            self.cat_eat_chocolate()
        cat_health = "cat_health"
        print(f"{cat_health:^50}\n")
        print(f"cat_health - {self.pet.cat_health}")
        if self.pet.cat_health <= 11:
            self.cat_treat()


    def live(self, day):
        if self.home is None:
            self.get_home()
        if self.pet is None:
            self.get_cat()

        self.days_indexes(day)
        return True


class Cat:
    def __init__(self, name="Мурзик"):
        self.name = name
        self.cat_happiness = 50
        self.cat_hunger = 50
        self.cat_health = 30


class House:
    def __init__(self):
        self.video_games = 0
        self.mess = 0


if __name__ == "__main__":
    Artur = Artur(name="Артур")

    for day in range(1, 8):
        if not Artur.live(day):
            break
