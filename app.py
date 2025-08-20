# print("Hello World")

# """
# str
# int
# float
# bool


# """

# name="25"
# print(type(int(name)))

# # name="555.555"
# # print(float(name))

# # print(int('2')/3)

# # print(int('36')+int("35"))

# # print((str(45)+str(22)))


# language = "Javascript"

# if "y" in language:
#     print(True)
# else:
#     print(False)


# speed=float(input("Sureti daxil edin: "))
# if speed>=0 and  speed<=40:
#     print("Zeif gedirsen")
# elif speed > 40 and speed < 60:
#     print("Orta gedirsen")
# elif  speed >= 60 and speed <=80:
#     print("nagarsan ucassan")
# else:
#     print("Bele bir suret yiga bilmez")


# val="o_rxan"

# if '_' or '.' in val:
#     print("true")
# else:
#     print("simvol yoxdur")

# # print(round(35.5545))
# # print(round(22.454,1))
# # print(round(36.666,2))
# # print(3**2)
# # print(pow(3,3))
# # print(abs(4))

# # print(divmod(17,3))

# # print(False==False)

# # sentence="Men Python oyrenirem"

# # print(len(sentence))
# # print(sentence[-1])
# # val=-4
# # print(sentence[(val)])

# # val="Sireli necesen?"
# # print(val[-1])
# # name="Rufet"
# # print(name.lower())
# # print(name.upper())
# # site="www.compar.edu.az"

# # print(site.removeprefix("www.").removesuffix(".az"))

# # sentence="seyfelerden en cox bu seyfeni seyfe olaraq sevirem"
# # print(sentence.replace('seyfe','sehife'))

# # val="445566"
# # print(val.rjust(7,"%"))

# sifre="4169-7388-6242-1878"

# print(sifre[4:14].center(16,"*"))

# name=input("Salam Adinizi daxil edin: ")
# print(type(name))


# value1=input("1-ci reqemi daxil edin: ")
# value2=input("2-ci reqemi daxil edin: ")
# print(float(value1)* float(value2))
# -------------------
value = "5382-1739-9201-9017"[:9].rjust(16,"*")

# print(value)

# print((15 % 4)**3)


# print(round(256.91372,2))
# print(round(256.91872,-2))

# val=str(34)

# print(val.rjust(5,"0"))

# val=float (input("bura reqem daxil edin: "))

# result=len(str(int(val)))
# print(result)


# print(len(
# site=input('sayti daxil edin:')
# print(site.removeprefix('https://').removesuffix('.com').upper().replace('K','C'))

val=int(input("Reqem daxil edin: "))

if (val%3==0) and (val%7==0) and (val%8==0):
    print('daxil etdiyiniz reqem 3 7 8 bolunur')
else:
    print("bolunmur") 

# a=input('sexsiyyet vesiqesinin nomresini daxil edin')
# b=str(a[:3].upper())

# if len(a)==10 and a[:3].isalpha() and a[:3].upper()==a[:3]:
#     print('xos gelmissiniz ')

#     if a[3:10].isdecimal():
#         True
#     else:
#         print('yanlis daxil edilib')
# else:
#     print("nomre herf ve reqemlerden ibaret olmalidir.")



# seria=input("Seriani daxil edin: ")


# if len(seria)==10:
#     if seria[::3].upper().isalpha():
#         if seria[3::].isdigit():
#             print("Sizin seria nomreniz: ",seria)
#     else:
#         print("Ilk 3 simvol boyukle yazilmalidir ve ingilis srifti olmalidir")
# else:
#     print("Seria 10 simvoldan ibaret olmalidir")



# credit =input("kreditinizi daxil edin:")
# credit =int(credit)
# if(credit<2000):
#   print("kredit verilmir")
# elif(credit<10_000):
#    print("yekun-borc",credit*1.05,"olacaq")
# elif(credit<50_000):
#    print("yekun-borc",credit*1.04,"oldu")
# elif(credit<200000):
#    print("yekun-borc",credit*1.02,"alindi")
# elif(credit<500000):
#    print("yekun-borc",credit*1.02,"verelecek")
# else:
#    print("bele kredit movcud deyil")


# password = input("Sifrenizi daxil edin: ")


# if  len(password) < 8 or len(password) > 40:
#     print("Parolunuz 8-den boyuk 40 dan kicik olmalidir")
# elif not password.isascii():
#     print("Zehmet olmasa ingilis  srifti ile qeyd etmelisiniz")
# elif not password.isalnum():
#     print("Hem herf hemde reqem olmalidir sizin sifrede")
# elif  password.islower() or password.isupper():
#     print("Sizin sifrede en azi bir boyuk bir balaca herf olmalidir")
# elif  password.isnumeric() or password.isalpha():
#     print("Daxil etdiyiniz parolda mutleq sekilde 1 herf bir reqem olmalidir")
# else:
#     print("Daxil oldunuz")






# number = input('Enter a phone number: ')

# if not isinstance(number, str):
#     print('Invalid input: phone number must be a string')
# else:
#     if len(number) == 14:
#         if number.startswith('+994'):
#             if number[1:].isnumeric():
#                 print('Phone number is valid')
#             else:
#                 print('Invalid input: phone number must contain only digits')
#         else:
#             print('Invalid input: phone number must start with +994')
#     else:
#         print('Invalid input: phone number must contain exactly 14 characters')

# print(len(number))
    


    # print(3.75)



# count=0


# while(count<3):
#     count=count+1
#     print("Araz")




# INIFINITE LOOP
# age=30


# while(age>18):
#     print("Siz suruculuk vesiqesi ala bilersiniz")
    


# num = 10000

# while num > 0:
#     if num % 999 == 0:
#         print(num)
#     num -= 1
#     break
    

# print(num)



# myList=['Mehemmed','Ferid','Rufet','IBO']
# firstName="Orxan"

# for item in firstName:
#     print(item)