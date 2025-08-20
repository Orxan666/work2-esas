# vesiqe=input("şəxsiyyət vəsiqəni daxil edin: ")

# if len(vesiqe)!=10:
#     print("10 xarakterden ibaret olmalidir")
# else:
#     olke_qisaltmasi=vesiqe[:3]
#     if not olke_qisaltmasi.isalpha() or olke_qisaltmasi!=olke_qisaltmasi.upper():
#         print("Olke adini duzgun qeyd edin")
#     else:
#         reqem=vesiqe[3:]
#         if not reqem.isdigit():
#             print("son yeddi simvol reqem olmalidir")
#         else:
#             print(vesiqe + " necesen ? ")



# amount=int(input("Ne qeder mebleg goturmek isteyirsen?"))
# if amount<2000:
#     print("Ay kasib sene pul dusmur")
# elif amount < 10_000:
#     print("Size ayrilcaq kredit miqdari: ",amount*1.05)
# elif amount < 50_000:
#     print("Size ayrilcaq kredit miqdari: ",amount*1.04)
# elif amount < 200_000:
#     print("Size ayrilcaq kredit miqdari: ",amount*1.02)
# elif amount < 500_000:
#     print("Size ayrilcaq kredit miqdari: ",amount*1.02)
# else:
#     print("500_000 den yuxari kredit verilmir")

# name="Keramet"

# for herf in name:
#     print(herf)



# uppercase_input=False
# name_input = input("Adinizi daxil edin: ")

# uppercase_found = False

# for char in name_input:
#     if char.isupper():
#         uppercase_found = True
#         break

# if uppercase_found:
#     print("Xos geldiniz "+name_input)
# else:
#     print(name_input + " yaxsi yol balaca herf ile ad olmaz")




# ad="Eli"

# for herf in ad:
#     if  herf == 'e'.upper() or "e".lower():
#         print(True)


# personal=["Orxan","Ehmed","Alsu","araz"]
# # print(type(personal))

# for item in personal:
#     if item.upper() =="araz".upper():
#         print("ascascasc")


# result=["Araz,2","Orxan"]

# print(result[2])


# personal=["Alsu","Keramet","Orxan"]


# personal.append("Araz")

# personal.remove("Alsu")

# print(personal)

# print(len(personal))

# valyuta=[1,3,6,2]
# valyuta2=["tumen","zlot","lari","manat"]
# valyuta.extend(valyuta2)
# print(valyuta)
# valyuta.append("euro")
# valyuta.clear()
# valyuta.remove("dollar")
# exchange=valyuta.copy()
# print(exchange)
# print(valyuta.count("dollar".lower()))
# print(valyuta.index("azn"))
# valyuta.insert(1,"euro")
# print(valyuta)
# valyuta.reverse()

# print(valyuta)
# valyuta.sort()
# valyuta.reverse()
# print(valyuta)

# print(dir(list))

# ad="Orxan#yaxsi#muellimdir"

# print(ad.split('#',2))


# sentence=["Men","python","oyrenirem"]

# print(" ".join(sentence))

# personal={
#     "name":"Alsu",
#     "age":25,
#     "job":"teacher",
#     "city":"Baku",
# }

# personal["hobby"]="driver"

# print(personal)


# even_numbers=[index for index in range(1,10) if index%2==0]
# print(even_numbers)

# my_dict=dict()

# for index in range(1,11):
#     my_dict[index]=index*index

# print(my_dict)
# my_dict={index:index*index for index in range(1,11)}
# print(my_dict)




# result=("Salam {} xos geldin .Biz {}-yiq".format("Ehmed","Baku"))
# print(result)

# print(('Salam {1} biz {0} oturmusuq').format("Bakida","Eli"))

# name="Taleh"
# age=22

# result=f"Hello {name.upper()} You're {age} years old"
# print(result)

# person={
#     "name":"Alsu",
#     "age":18
    
# }

# print(f"Hello {person["name"].upper()} You're {person["age"]} years old")



# --------------------------------------------------------------------

# sentence="Men Javascript oyrenirem"

# result=''

# for char in sentence:
#     if char.isalpha():
#         order=ord(char)-96
#         result+=str(order)+','

# print(result)


# sentence = 'Men Javascript oyrenirem'
# # sentence=input("Cumle daxil edin : ")
# result = ''
# for char in sentence.lower():
#     if char.isalpha():
#         order = ord(char) - 96
#         result+=str(order)+','
# print(result)


# Global , Local

# a=5
# print(a)
# number1=4
# def test():
#     print(number1)

# test()


# def test():
#     global number1
#     number1=555
    
#     print("function local : "+str(number1))
# test()

# print("Qlobal deyer" + str(number1))

# CALL BACK FUNTION , BUILD IN FUNCTION RECURSIVE FUNCTION

# def topla(*arqs):
#     total=0
#     for i in arqs:
#         total+=i
#     return total

# print(topla(5,2,4,7))
# topla(2,4)



# a={1,9,16,15,22,10,11}
# b={15,22,45,27}
# c={10,11,74,86,90,77,100}
# d={100,44,55,94}


# numbers={1,2,3,4,5}
# print(numbers[0:2])
# Set-de sira anlayisi yoxdur

# personal={"Orxan","orxan","Eli","Aysel"}
# set-de deyisin tipli datalar saxlaya bilmirik 
# result={1,2,3,(4,5,6)}

# print(result)
# ------------------------
# result={}
# dictionary
# ---------------------
# result=set()

# print(type(result))
print(dir(set))