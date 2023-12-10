import random
class Cat:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.famine=0
        self.alive=True

    def to_study(self):
        print("game")
        self.famine+=0.12
        self.gladness-=3
    def to_sleep(self):
        print(" I will sleep ")
        self.famine+=3
    def to_chill(self):
        print("Rest time")
        self.famine-=0.1
        self.gladness+=5
    def is_alive(self):
        if self.famine<-0.5:
            print("Cast out")
            self.alive=False
        elif self.gladness<=0:
            print("Depresion..")
            self.alive=False
        elif self.famine>5:
            print("Passed externaly")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"famine - {round(self.famine,2)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()
nick=Cat(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)