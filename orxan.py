# import math as  m

# print(m.pi)


# from math import pi

# print(pi)

# print(dir(list))



class Weapon:
    metal="iron"
    def __init__(self,bullet_count):
        self.bullet_count=bullet_count

class MachineGun(Weapon):
    power=50

    

class Sniper(Weapon):
    power=70


class Soldier(Weapon):
    health=100

    def __init__(self,name:str,weapon):
        self.name=name
        self.weapon=weapon

    def fire(self,enemy):
        enemy.health-=self.weapon.power
        self.weapon.bullet_count-=1

    def __len__ (self):
        return self.weapon.bullet_count

avm=Sniper(5)
m416=MachineGun(30)


behram=Soldier("Behram",m416)
cavid=Soldier("Cavid",avm)

behram.fire(cavid)
behram.fire(cavid)
behram.fire(cavid)
print(behram.weapon.bullet_count)

    

    







