import random
import time

class LiveObject:
    all_live_objects = []
    
    def __init__(self):
        LiveObject.all_live_objects.append(self)
        self.ticks = 0
    
    def tick(self):
        self.ticks += 1
        
class Animal(LiveObject):
    period = None
    
    def __init__(self, nickname):
        super().__init__()
        self.nickname = nickname
        
    def tick(self):
        super().tick()
        if not self.period:
            raise Exception("Друг! Все наследники должны иметь аттрибут period")
        if self.ticks % self.period == 0:
            self.say()
        
    def say(self):
        print(self.get_phase())
        
    def get_phase(self):
        v = ['Покорми , прошууууу ',"Кинь покушать ","Мне бы поесть ( "]
        
        return f"[{self.nickname}]" + random.choice(v)
        
class Cat(Animal):
    period = 15
            
    def get_phase(self):
        return super().get_phase() + " Meow!"

class Dog(Animal):
    period = 30
    def get_phase(self):
        return super().get_phase() + "Gav!"

class Cow(Animal):
    period = 40
    def get_phase(self):
        return super().get_phase() + "Muuuu!"

    
cat1 = Cat("Murzik")
dog1 = Dog("Bobik")
cow1 = Cow("Burenka")

while True:
    for l_obj in LiveObject.all_live_objects:
        l_obj.tick()
    time.sleep(0.1)



        
