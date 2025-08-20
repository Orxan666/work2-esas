# a={1,14,16,4,5,15,6}
# b={6,5,15,7,11,10,9,8}
# c={5,7,11,4,4,16,3,13,12,2}
# d={2,11,12}


# a={1,2,3,4,"saaa","s"}
# print(type(a))

# personal=("Ehmed","Ehmed","Alsu","Keramet")
# print(personal.index("Alsu"))

# result=(1,2,3,4)

# print(type(result))

# mySet={1,2,3,4,(2,3,4)}
# print(mySet)

# meyveler ={'alma','armud','heyva'}
# personal=(1,2,3)
# print(personal[1])
# print(meyveler)
# for i in meyveler:
#     print(i)
# 
# print(meyveler,type(meyveler))

# print(len(meyveler))

# for meyve in meyveler:
#     print(meyve)

# setlerde sira anlayisi yoxdur
# print(meyveler[0])
# print(meyveler[0::3])

# setlerde bir datadan iki defe saxlanila bilmir
# meyveler={'alma','alma','armud','heyva','nar'}
# print(meyveler)


# setlere deyisen tipli datalar vere bilmerik
# meyveler={'alma','armud',['heyva','nar']} olmaz
# meyveler={'alma','armud',('alma','heyva','nar')}
# print(meyveler)

# ---------------------------
# tuple list set -lerin ferqi nedir
# ---------------------------
# a1=set()
# print(type(a1))

# PYTHON SET METHOD
# print(dir(set))
a = {1, 9, 16, 15, 22, 10, 11}
b = {15, 22, 45, 27}
c = {10, 11, 74, 86, 90, 77, 100}
d = {100, 44, 55, 94}

# d.add(10)
# d.remove(10)
# print(d)
# d2=d.copy()
# d2.add(10)
# print(d2)
# d.clear()
# print(d)
# d3=set()

# print(a.intersection(b))
# print(a)
# print(a.union(b))
# b.intersection_update(a)
# print(b)
print(a.difference(b))
# print(a.isdisjoint(b))
# a={1,2,3,4,5,6}
# # b={2,1}

# for i in a:
#     print(i)

# amount = 10000
# if(amount > 2999)
# print("You are eligible to purchase Dsa Self Paced")

# marks = 100

# a = marks/0
# print(a)

# x=6
# y=" "

# try:
#     print(x/y)

# except TypeError:
#     print("Reqemle herfi toplamaq olmaz")
# except ZeroDivisionError:
#     print("Hec bir reqem 0-a bolune bilmez")
    
# name="Orxan"

# # print(firstName)

# try :
#     print(firstName)
# except NameError:
#     print("bele bir deyisken movcud deyil")




# try :
#     import pandas
# except ModuleNotFoundError:
#     print("Import etdiyiniz deyer install olunmalidir ve ya sehv import etmisiz")
