# sual 1 prezentasiya
# ------------------------------------------


# class Weapon:
#     metal="cobalt"
#     def __init__(self,bullet_count):
#         self.bullet_count=bullet_count



# class MachineGun(Weapon):
#     power=80
    

# class Sniper(Weapon):
#     power=90



# class Soldier(Weapon):
#     health=100

#     def __init__(self,name:str,weapon):
#         self.name=name
#         self.weapon=weapon

#     def fire(self,enemy):
#         enemy.health-= self.weapon.power
#         self.weapon.bullet_count-=1

#     def __len__ (self):
#         return self.weapon.bullet_count



# avm=Sniper(5)
# m4=MachineGun(15)

# behram=Soldier("Behram",m4)
# cavid=Soldier("Cavid",avm)

# behram.fire(cavid)
# # behram.fire(cavid)
# # behram.fire(cavid)
# print(cavid.health)
# print(behram.weapon.bullet_count)

# print(len(behram))
# # -------------------------------------------

# # 1-ci sual Notion

from typing import Literal

ServiceTypes=Literal['call','sms','mb']


class Credit:
    service_prices:dict[ServiceTypes,int] ={
        'call':10,
        'sms':3,
        'mb':5
    }
    
    def __init__(self,balance:int):
        self.balance=balance

    def decrease(self,service:ServiceTypes):
        price=self.service_prices[service]
        if price>self.balance:
            raise Exception("Kifayet qeder balans yoxdur !")
        
        self.balance-=price

    def increase(self,amount:int):
        self.balance+=amount

class Phone:
    
    def __init__(self, balance: int):
        self.credit = Credit(balance)
        self.received_message = []
        self.sent_message = []

    def send_message(self, message: str, target: 'Phone'):
        self.sent_message.append(message)  # Fixed the attribute name here
        target.received_message.append(message)
        self.credit.decrease('sms')


bphone=Phone((8))

cphone=Phone((10))

bphone.send_message('salam muellim',cphone)
cphone.send_message('Salam behram necesen?',bphone)


print(bphone.received_message)    

print(cphone.received_message,cphone.sent_message)



# --------------------------OOP2 DERSIMIZ

# multi inheritance-bir nece classdan inherit alma


# class Player:
#     health=100
#     def __init__(self,name):
#         self.name=name
       

# class Soldier(Player):
#     power=40

#     def fire(self,enemy:Player):
#         enemy.health -= self.power

# class Doctor(Player):
#     threatment=10

#     def thearet(self,opponent:Player):
#         opponent.health+=self.threatment



# class Rambo(Soldier,Doctor):
#     pass    


# orxan=Rambo("Orxan")
# behram=Soldier("Behram")
# cavid=Doctor('Cavid')


# behram.fire(cavid)
# print(cavid.health)

# orxan.fire(behram)
# print(behram.health)
# orxan.thearet(behram)
# orxan.thearet(behram)
# orxan.thearet(behram)
# print(behram.health)
# # print(cavid.health)
# cavid.thearet(behram)
# print(behram.health)


# ---------------------------

# Polimorfizm - bir prosesi bir nece class uzerinde heyata kecire bilirikse bu polimorfizm adlanir
    
# len('asadvdvv')
# len([1,2,3,4,5])
# len({1,2,3,4})

# def is_dead(player):
#     return player.health>0

    
# print(is_dead(behram))
# print(is_dead(cavid))
# print(is_dead(orxan))




# def is_dead(player):
#     return player.health >0

# print(is_dead(behram))
# print(is_dead(cavid))
# print(is_dead(orxan))


    # ------------------------------

# Encapsulation- 

# class Flash:
#     max_limit=30
#     def __init__(self):
#         self.volt=0

#     def get_volt_value(self):
#         return self.__volt

# class Phone:

#     def __init__(self):
#         self.flash=Flash()
    
# phone=Phone()
# phone.flash.__volt=120
# print(phone.flash.get_volt_value())




# class Flash:
#     max_limit=20

#     def __init__(self):
#         self.__volt=0

#     def get_volt_value(self):
#         return self.__volt
    
# class Phone:
#     def __init__(self):
#         self.flash=Flash()


# phone=Phone()

# phone.flash.__volt=100

# print(phone.flash.get_volt_value())


# import os
# # files = os.mkdir(r"D:\programming\PYTHON")
# files = os.rmdir(r"D:\programming\PYTHON\mehemmed")
# print(files)



# class Soldier():
#     def __init__(self, uniform_color, health, name, power):
#         self.uniform_color = uniform_color
#         self.health = health
#         self.name = name
#         self.power = power

# class Doctor(Soldier):
#     pass



# doctor1=Doctor()





# class Employee:
#     def __init__(self, name, salary):
#         self.name = name          # public
#         self._position = "Staff"  # protected
#         self.__salary = salary    # private

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self, new_salary):
#         if new_salary > 0:
#             self.__salary = new_salary
#         else:
#             print("Maaş sıfırdan böyük olmalıdır!")


# emp = Employee("Orxan", 2000)

# print(emp.name)
# print(emp._position)
# print(emp.__salary)
# print(emp.get_salary())