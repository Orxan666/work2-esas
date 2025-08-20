# MODULE HOMEWORK
# 1-ci sual
import math


# def get_coni_area(r,h):
#     result=(1/3)*math.pi*(r**2)*h
#     return result

# print(get_coni_area(2,5))
# --------
# def get_glob_value(r):
#     result=(4/3)*math.pi*(r**3)
#     return result
# print(get_glob_value(5))

# ------------------2-ci sual
# import math

# def get_combination(n,r):
#     if n<r:
#         raise ValueError('n>r sertine uygun olmalidir')
#     a=math.factorial(n)
#     diff =math.factorial(r)*math.factorial(n-r)
#     result=a/diff
#     return result
# print(get_combination(6,2))

# 3-cu sual

# from random import shuffle
# names = input('adlar; daxil edin: ').split(', ')
# # print(names)
# shuffle(names)
# for n in names:
#     input(n)

# 4-cu sual-----------------------

# import random
# start:int=int(input('baslangic deyeri daxil edin : '))
# end:int=int(input('sonuncu deyeri daxil edin : '))
# number:int=random.randint(start,end)

# print(number)

# attempt:int=0
# attempt+=1
# while True:
  
#     prediction:int=int(input('ededi deyin: '))
#     if prediction > number:
#         print('asagi eded teyin edin')
#     elif prediction < number:
#         print('yuxari eded yazin')
#     else:
#         if attempt>3:
#             print(f'uduzduz cunki siz {attempt} qeder bextinizi sinadiniz vallah mumkun deyil')
#             break

#         else:
#             print('qalib oldunuz')
#         break
# eded_araliq=random.randint(1,50)
# texmin_haqqi=10
# saygac=0
# while True:
#     eded=int(input('1-50 arasi eded daxil edin'))
#     texmin_haqqi-=1
#     saygac+=1
#     if 
# import random

# start = int(input("Baslangic ededi qeyd edin: "))
# finish = int(input("Hansi edede qeder olacagin qeyd edin: "))

# gizlireqem = random.randint(start, finish)
# print(gizlireqem)

# cehd = 0
# texmin = None

# while texmin!=gizlireqem:
#     if cehd > 9:
#         print("Meglub oldunuz!")
#         break 
#     else:
#         texmin = int(input("Verdiyiniz araliqdaki ededi texmin edin: "))

#         if texmin < gizlireqem:
#             print("Yuxari")
#             cehd += 1
#         elif texmin > gizlireqem:   
#             print("Asagi")
#             cehd += 1
#         else:
#             print("Tebrikler! Qalibsiniz!")
#             break


# v=s/t
# def myDef(s,t):
#     return s/t
# print(

# myDef(588,90)

# )


# ++++++++++++++++++++++++++++++++++++++++++++++
#==== TIMEIT LESSON====

# import timeit

# duration1 = timeit.timeit('[i**3 for i in (1,2,3,4,5,6,7,8)]', number=7, repeat=5)
# duration2 = timeit.timeit('list(map(lambda x: x**3, (1,2,3,4,5,6,7,8)))', number=7, repeat=5)

# print(duration1, duration2)

# import timeit

# mySet="5+5+5"

# print(timeit.timeit(mySet))

# import timeit

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# import timeit

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# print(timeit.timeit('factorial(5)', globals=globals()))


# import math
# import timeit

# print(timeit.timeit('math.factorial(5)', globals=globals()))


# import sys

# print(sys.version_info)



# a=(1,2,3,4,5,6,7,8)

# duration1=timeit('[i**3 for i in a]','from __main__ import a',number=100_000)
# duration2=timeit('map(lambda x: x**3,a)','from __main__ import a',number=100_000)

# print(duration1,duration2)






# import sys



# print(sys.version)
# print(sys.version_info)


# argv: list[str]=sys.argv

# filename:str =argv[1]
# count:int=int(argv[2])

# with open('rufet.txt','w') as file:
#     for i in range(1,1+1):
#         file.write(f'{i}. \n')
# print('COMPLETED!')


# import sys


# for line in sys.stdin:
#     if 'q'==line.rstrip():
#         break
#     print(f'Input {line}')

# print('Exit')

# from math import pi,comb,perm
# import random

# form=input('ad daxil edin').split(', ')
# adlar=len(form)
# while True:
#     input('yeniden daxil edin')
#     secilen_ad=random.choice(form)
#     form.remove(secilen_ad)
#     adlar-=1
#     print(secilen_ad)

#     if adlar==0:
#         print('adlar bitdi')
#         break

# from datetime import datetime,timedelta
# mesafe=588000000
# suret= 90
# vaxt=mesafe/suret
# zaman= datetime.now()+timedelta(hours=vaxt)
# a= zaman.strftime('%d.%m.%Y')
# print(f"niva ile {a} tarixde catacaqsiz ")
# # print(zaman)

# '“Saat 17:00, 04.06.2022 tarixində dərsə gəlin” cümləsindən istifadə edərək tarixi datetime formatına çevirin. '
# cumle='Saat 17:00, 04.06.2022 tarixində dərsə gəlin'
# cumle_format='Saat %H:%M , %d.%m.%Y tarixində dərsə gəlin'

# import math

# from math import pi
# import math as orxan

# print(orxan.pi)
# import math
# print(dir(math))



# from math import *

# print(factorial(5))

import random

# myList=('a',4,'b')

# result=random.choice(myList)

# print(result)

# print(random.seed(1))
# print(random.random())

# random.seed(3)

# print(random.random())

# sample_list = [1, 2, 3, 4, 5]

# random.shuffle(sample_list)
# print(sample_list)

# import datetime

# print("Arazin ad gunu: ",datetime.date(2008, 6, 15))

# today=datetime.date.today()
# result=datetime.date.isoformat(today)
# print(type(result))

# import datetime

# print(dir(datetime))


# oop

class Soldier:
    def __init__(self, uniform_color, health, name, power):
        self.uniform_color = uniform_color
        self.health = health
        self.name = name
        self.power = power

    def __str__(self):
        return f"Soldier(name={self.name}, uniform_color={self.uniform_color}, health={self.health}, power={self.power})"

# Creating an instance of Soldier
soldier1 = Soldier(uniform_color="Black", health=80, name="Selcuq", power=40)
soldier2 = Soldier(uniform_color="Blue", health=70, name="Elsad", power=20)

# Printing the instance
print(soldier1)
print(soldier2)
