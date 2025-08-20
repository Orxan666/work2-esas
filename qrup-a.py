# result=10
# if result%3!=0:
#     print("not divisible by 3")
# else:
#     print("divisible by 3")

# result="Python"

# print( "P" in result)

# print((6//4))

# firstName=input("Adinizi daxil edin: ")
# lastName=input("Soyadinizi daxil edin: ")
# print("Salam",firstName,lastName)

# value1=int(input("1-ci ededi daxil edin: "))
# value2=int(input("2-ci ededi daxil edin: "))
# print(value1*value2)

# firstName="Orxan"
# print(firstName.center(11,"*"))

# message = 'python is Popular programming language'
# print(message.casefold().count("p"))

# message="Salam necesen Baki"
# print(message.endswith("necesen"))

# print(dir(str))

# result=("SAlam {} senin {} yasin var".format("Orxan","21"))
# result=("SAlam {name} senin {age} yasin var".format(age=27,name="Orxan"))
# print(result)
# print("Orxan!\n".isprintable())


# ===========================================
# Lesson3
# val="5382-1739-9201-9017"[9:].rjust(17,"*")
# print(val)
# -------------
# print((15%4)**3)
# ---------------
# print(round(256.91872,2))
# print(round(256.91872,-2))

# val=str(34)
# print(val.rjust(5,"0"))


# eded = float(input("Reqem daxil edin: "))
# print(type(val))
# print(val)

# tam_hisse=int(abs(eded))
# reqem_sayi = len(str(tam_hisse))


# print(reqem_sayi)


# site = input("Daxil et: ")

# val=site.removeprefix("https://").removesuffix(".az").upper()
# print(val)
# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Compar Academy")


# (num=1
# result=0
# while num<101:
#     result+=num
#     num+=1
# print(result)
# # --------------------------------------
# text='men her gun python oyrenirem'
# saitler="aiuoüöıəe"

# result=""
# index=0
# while index<len(text):
#     if text[index].lower() not in saitler:
#         result+=text[index]
#     index+=1)
# print(result)


# a=["Lamiye","Jale","Elton"]


# for index in a:
#     print(index)

# firstName="Orxan"

# for i in firstName:
#     print(i)

# for i in range(2, 101,2):
#     pass

# ascascac

#
# For home work


# 1-dən 100-ə kimi olan bütün ədədlərin toplamını tapın (1+2+3+...+99+100)
# i=0
# for eded in range(1,101):
#     i+=eded
# print(i)

# 100000-dən aşağı doğru gedərək 9999-a bölünən ilk ədədi konsolda göstərin.
# for i in range(100000,0,-1):
#     if i%9999==0:
#         print(i)
#         break


# ---------------------------------


# myList=[2,3,4,5,6]

# result =[i*i for i in myList]
# print(result)


# result ={index:index*index for index in range(1,101) if not index%2==0}
# print(result)
# myTup=["Orxan","Jale","Elton"]
# myTup[0]="Eli"
# print(myTup)

# myList = [2,3,4,5,6]
# for i in myList:
#     # print(i)
#     if i%2==0:
#         print(i)
# result=[i*i for i in myList if i%2==0]
# print(result)

# List compression ile V herfi ile baslayan adlari printde dinamik sekilde gossterin
# personal=["Vahab","Vidadi","veli","Orxan","Eli"]
# result = [item for item in personal if item.lower().startswith("v")]


# print(result)
# ---------------------------------------------------------------
# Asagidaki list icerisinden 5 herfli olan
# adlari ters cevirerek list compression ile yazaraq print edin

# items = ["Vahab", "Vidadi", "veli", "Orxan", "Eli", "Elton"]
# result = [item[::-1] for item in items if len(item) == 5]
# print(result)

# result = [item.upper() for item in items if len(item) == 6]
# print(result)


# items = ["Vahab", "Vidadi", "veli", "Orxan", "Eli","Terlan", "Elton"]
# netice=[ index for index in items if index[len(index)-1]=="n"]
# print(netice)

# firstname="Orxan"
# print(firstname[-1])
# print(firstname[len(firstname)-1])

# products={
#     "sud":1.70,
#     "soda":1.50,
#     "su":1.70,
#     "kofe":1.80,
#     "kola":1.50

# }
# faiz=0.25

# result={key:value*faiz+value for key,value in products.items()}
# print(result)


# sentence="Salam {} senin {} yasin var".format("Orxan",25)
# sentence = "Salam {name} senin {age} yasin var".format(age=input("Yasinizi daxil edin:"), name=input("Adinizi daxil edin:"))
# print(sentence)


# def myFunction():
#     return ("Hello from a function")

# print(myFunction())

# def toplama(reqem1,reqem2):
#     return reqem1+reqem2

# print(
#     toplama(1,2)
# )

# def myFunc(firstName):
#     return f'Hello {firstName}'


# print(myFunc("Orxan"))


# def test():
#     pass

# a=4
# print(a)

# student="Lamiye"

# def test(student):
#     return f'Hello {student}'


# print(test(student))

# def person(name,age=):
# return f"Hello {name} you are {age} years old"

# *args *kwargs

# def test(*args):
#     return sum(args)
# print(test(1,2,3,5,7,8))


# def test2(**kwargs):
#     return kwargs
# print(test2(name="Orxan",age=19))

# def myFunction(**kwargs):
#     for a,b in kwargs.items():
#         print(f"keyimiz: {a} value-miz: {b}")

# myFunction(Ad='Orxan')

# firstname="abdullah"

# result=lambda func:func.upper()
# print(result(firstname))

# age=int(input("Yasinizi daxil edin: "))


# result=lambda a: "Siqaret ala bilersiniz" if a>18 else "Siz siqaret ala bilmersiniz"
# print(result(age))


# result=lambda a, t : (a*(t*t)//2)


# print(result(5, 10))


result=lambda s,t : s
