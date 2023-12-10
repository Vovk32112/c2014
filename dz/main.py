import random
class Cat:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.Progress=0
        self.alive=True

    def to_Studying_the_world(self):
        print("time to Studying the world")
        self.Progress+=0.12
        self.gladness-=3
    def to_sleep(self):
        print(" I will sleep ")
        self.Progress+=3
    def to_play(self):
        print("Rest time")
        self.Progress-=0.1
        self.gladness+=5
    def is_alive(self):
        if self.Progress<-0.5:
            print("Cast out")
            self.alive=False
        elif self.gladness<=0:
            print("Depresion..")
            self.alive=False
        elif self.Progress>5:
            print("Passed externaly")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.Progress,2)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_Studying_the_world()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_play()
        self.end_of_day()
        self.is_alive()
nick=Cat(name="Murzik")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
