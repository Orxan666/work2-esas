# TIMEIT HOMEWORK

# from timeit import timeit

# import random 
# from math import inf as infinity

# randomlist_float=[]
# for i in range(0,1001):
#     floatnumber=round(random.uniform(1,100),3)
#     randomlist_float.append(floatnumber)

# # print(randomlist_float)

# def bignumbersort(a):
#     a.sort(reverse=True)
#     return a[0]


# def find_biggest_number(numbers):
#     max_value = -infinity
#     for n in numbers:
#         if n > max_value:
#             max_value = n
#     return max_value



# duration=timeit('bignumbersort(randomlist_float)','from __main__ import bignumbersort,randomlist_float')
# duration2=timeit('find_biggest_number(randomlist_float)','from __main__ import find_biggest_number,randomlist_float')



# print(duration,duration2)
# =============
from timeit import timeit
def f1():
    text = 'I live in New York'
    textreverse = text[::-1]
    vowels = 'aeiuo'
    result = ''
    for char in textreverse:
        if char not in vowels:
            result += char
    return result


def f2():
    text = list('I live in New York')
    text.reverse()
    vowels = 'aeiuo'
    for char in text:
        if char not in text:
                text.remove(char)
    return(''.join(text))

print(timeit('f1()','from __main__ import f1',number=100))
print(timeit('f2()','from __main__ import f2',number=100))



# import os


# print(os.listdir(r'C:\Users\Orxan\Videos\Captures'))
# os.mkdir("../humay.txt")

# os.rmdir("humay.txt")

# print(os.name)

# movcud_yer=os.getcwd()

# print(os.listdir(movcud_yer))

# print(os.listdir(os.pardir))


# os.mkdir("mehriban")

# os.rename('mehriban','ibooo')

# import clipboard
# print(clipboard.paste())




# import json 


# person_dict={"name":"Sireli",
# "languages":["aze","eng","rus"],
# "married":True,
# "hobby":"football"

# }

# with open ("elmar.txt",'w') as json_file:
#     json.dump(person_dict,json_file)



# import secrets

# print(secrets.token_urlsafe(10))

# from uuid import uuid1

# print(uuid1())


# +++++++++++++++++++++OS HOMEWORK+++++++++++++++++++++++

# 2-ci sual
# --------------------------------
# import os,shutil
# os.mkdir( 'Dersler')
# with open('Dersler/ders1.txt', 'w') as file:
#     pass
# with open('Dersler/ders2.txt', 'w') as file:
#     pass
# os.remove('Dersler/ders1.txt')
# os.rename('Dersler/ders2.txt', 'Dersler/phyton_notlar.txt')
# os.makedirs('Dersler/Python/General Python')
# shutil.move('Dersler/phyton_notlar.txt', 'Dersler/Python/General Python')
# shutil.copy('Dersler/Python/General Python/phyton_notlar.txt', r'D:\Users\Ujer\Desktop' )
# shutil.rmtree('Dersler')
 

# 3-cu sual 


# import json

# users_data="""[
#     {"device": "iphone", "price": 3000, "count": null}, 
#     {"device": "samsung", "price": 2500, "count": 3},
#     {"device": "xiaomi", "price": 2100, "count": null},
#     {"device": "nokia", "price": 1800, "count": 4}
# ]
# """

# users=json.loads(users_data)
# result=0

# for user in users:
#     if user['count']:
#         result+=(user['price']*user['count'])
# print(result)

# 1-ci sual 

# import time
# x=int(input("Deyer daxil edin: "))
# def geri_sayim(x):
#     while x>=0:
#         print(x)
#         time.sleep(1) 
#         x-=1
#     return "bitti"
# print(geri_sayim(x))




