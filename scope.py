# Scopes
# Globals
# Decorators
# Recursive Function


# number=5


# if number==5:
#     a=3

# print(a)

# while a<number:
#     b=5
#     a+=1

# print(b)
# print(a)

# c=None
# for i in range(3):
#     c=10

# print(c)
# c=11
# print(c)

# x=5

# def test():
#     global x
#     x=20

# test()

# print(x)


# z=10
# def test():
#     global z
#     z = 2


# test()
# print(z)


# z=10
# def f():
#     global simba
#     simba=30
#     global t
#     t=20
# print(globals())
# print(locals())
# f()
# print(simba)
# print(t)
# def f2():
#     e=25
#     print(e)
# f()
# print(simba)
# -------------
# a=5
# a=34

# def deyis():
#   a+=2
# deyis()
# print(a)


# def add(x,y):
#     return x+y

# def calculate(orxan,x,y):
#     return orxan(x,y)

# print(calculate(add,3,4))


# def make_pretty(func):
#     def inner():
#         print("salam")
#         func()
#     return inner


# @make_pretty
# def test():
#     print("Necesen")

# test()


# def my_decorator(func):
#     def wrapper():
#         print("Salam1")
#         func()
#         print("Salam2")
#     return wrapper


# @my_decorator
# def say_hello():
#     print("Roya")
# say_hello()


# ---------------Decorators
# def salam(ad):
#     return f'Salam hormetli {ad}'
# def necesen(ad):
#     return f'necesiniz bugun {ad}'
# def isler(vezife):
#     return f'{vezife} nece gedir?'

# print(salam('Orxan'))
# print(necesen('Orxan'))
# print(isler('Muellimlik'))


# def upper(function):
#     def wrapper(word):
#         result=function(word)
#         result=result.upper()
#         return result
#     return wrapper
# @upper
# def salam(ad):
#     return f'Salam hormetli {ad}'
# @upper

# def necesen(ad):
#     return f'necesiniz bugun {ad}'

# @upper
# def isler(vezife):
#     return f'{vezife} nece gedir?'


# necesen=upper(necesen)


# print(necesen("Eli"))
# print(isler("Muellimlik"))


# -----------

# logined=False


# def login_required(function):
#     def wrapper():
#         if logined:
#             result=function()
#         else:
#             result=print("Giris qadagandir")
#         return result
#     return wrapper


# @login_required
# def ana_sehife():
#     return ("ana sehifeye xos gelmissiniz")

# @login_required
# def login_sehifesi():
#     return ("login sehifesidir")


# @login_required
# def register():
#     return ("register sehifesi")


# @login_required
# def hesab():
#     return ("Hesab parametrleri sehifesi")


# print(ana_sehife())


# ----------------- Recursive Function


# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))

# print(dir(str))

# a=-5

# print(abs(a))


# 
# print(eval("5+5"))


# age=int(input("Yasinizi daxil edin: "))
# print(age)

# if isinstance(age,int):
#     print(age)
# else:
#     print("Zehmet olmasa reqem daxil edin")

# print(55/0)

try:
    age=int(input("Yasinizi daxil edin: "))
except ValueError:
    print("Zehmet olmasa reqem daxil edin")

