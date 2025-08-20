# Scopes,
# Globals,
# Decorator,
# Recursive Function,
# Callback Function,

# number=5

# if number==5:
#     a=3
# print(number)

# def test():
#     global a
#     a=4


# test()
# print(a)
# while number<10:
#     b=5
#     number+=1
# print(b)


def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(0))


# for i in range(8):
#     c=10

# print(c)

# z=10
# a=3
# c=6
# def f():
#     global z,a,c
#     z=z+1
#     a=a+1
#     c=c+1
# f()
# print(a,z,c)

# print(reqem1)

# print(locals())


# def f():
#     global z
#     z=10
#     def c():
#         global a
#         a=4
#     c()
#     print(a)
# f()

# print(z)

# a=5

# def test():
#     global a
#     a+=1

# # test()
# print(a)

# a=5
# def deyis():
#     global a
#     a+=2

# deyis()
# print(a)


# DECORATOR FUNCTION



# def salam_decorator(func):
#     def wrapper():
#         print("Salam xos geldin")
#         func()
#         print("Sagol")
#     return wrapper


# @salam_decorator
# def firstName():
#     print("Orxan")


# firstName()

# def upper(function):
#     def wrapper(word):
#         result = function(word)
#         result=result.upper()
#         return result
#     return wrapper


# @upper
# def firstName(ad):
#     return f'Salam hormetli {ad}'

# print(firstName('eli'))

# @upper
# def lastName(ad):
#     return f'Salam hormetli soyad {ad}'

# print(lastName('Eliyev'))


# @upper
# def ataAdi(ad):
#     return f'Salam hormetli ata adi {ad}'

# print(ataAdi('eli'))


# @upper
# def necesen(ad):
#     return f'Necesen hormetli {ad}'

# @upper
# def isler(vezife):
#     return f'{vezife} nece gedir?'


# print(salam("Eli"))
# print(necesen("Eli"))
# print(isler("Hekimlik"))


# salam=upper(salam)
# print(salam("Rufet"))

# -------------------------

# logined = False


# def login_required(function):
#     def wrapper():
#         if logined:
#             result = function()
#             return result
#         else:
#             print("Zehmet olmasa login daxil edin")
#     return wrapper


# @login_required
# def ana_sehife():
#     return "Home sehifesine xos gelmisiniz"

# print(ana_sehife())
# @login_required
# def login_sehife():
#     return "login  sehifesi"


# @login_required
# def hesab():
#     return "hesab cixarisi sehifesi"

# print(ana_sehife())
# print(login_sehife())
# print(hesab())

# Recursive function HomeWork 16


# eqs = {'ə':'e','ü':'u','ö':'o','ı':'i'}
# def replace_azeri_chars(func):
#     def wrapper(*args, **kwargs):
#         value = func(*args, **kwargs)
#         if isinstance(value, str):
#             result = ''
#             for i in value:
#                 result += eqs.get(i, i)
#             return result
#         return value
#     return wrapper

# @replace_azeri_chars
# def salam_ver(ad,soyad):
#     return 'Salam hörmətli {} {}, necəsiniz?'.format(ad, soyad)

# eqs = {'ə':'e','ü':'u','ö':'o','ı':'i'}


# def replace_azeri_chars(function):
#     def wrapper(*args, **kwargs):
#         value=function(*args, **kwargs)
#         if isinstance(value,str):
#             result=''
#             for i in value:
#                 result+=eqs.get(i,i)
#             return result
#         return value
#     return wrapper

# @replace_azeri_chars
# def salam_ver(ad, soyad,email):
# 	return 'Salam hörmətli {} {}, necəsiniz? sizin email adresiniz {}'.format(ad, soyad,email)

# print(salam_ver('Arif', 'Həsənov','ərif@mail.ru'))
# ---------------------------------------------------------------



# def az_cevir(func):
# 	def inner(*args,**kwargs):
# 		result=func(*args,*kwargs)
# 		for i in result:
# 			for key, value in eqs.items():
# 				if i==key:
# 					result=result.replace(key,value)
# 		return result			
#     return inner



# eqs = {'ə':'e','ü':'u','ö':'o','ı':'i'}
# def az_cevir(func):
#     def wrapper(*args, **kwargs):
#         value = func(*args, **kwargs)
#         if isinstance(value, str):
#             result = ''
#             for i in value:
#                 result += eqs.get(i, i)
#             return result
#         else:
#              print("duzgun deyil")
#         return value
    
#     return wrapper


# @az_cevir
# def salam_ver(ad, soyad):
	# return 'Salam hörmətli {} {}, necəsiniz?'.format(ad, soyad)

# print(salam_ver('Arif', 'Həsənov'))
# output: Salam hormetli Arif Hesenov, necesiniz?




# def upperName(c):
#      return c.upper()
     

# def bigCall(name,call):
#      result=call(name)
#      return result

# result=bigCall("selcuq",upperName)
# print(result)





# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x * factorial(x-1))

# print(factorial(5))









