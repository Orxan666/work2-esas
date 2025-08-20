# n1=int(input("Reqem 1-i daxil edin :"))
# n2=int(input("Reqem 2-i daxil edin :"))
# total=n1*n2
# print('Sizin netice: '+str(total))
# ---------------------------------------------------------------------
# =================HOMEWORK 2 =========================
# 1-ci sual
# val = "5382-1739-9201-9017"[9:].rjust(17,'*')
# print(val)
# ------
# 2-ci sual
# print((15%4)**3)
# print(17%4)
# 3-cu sual
# print(round(256.91872,2))
# print(round(256.91872,-2))
# 4-cu sual
val=str(34)
# print(val.rjust(5,"0"))
# result=input('Zehmet olmasa adinizi daxil edin: ')
# print('Xos geldin',result)
# 5-ci sual
# eded=float(input('Bir eded girin: '))
# eded=int(eded)
# eded=str(eded)
# print(len(eded))
# ----------6ci sual
# site = input('Sayti daxil edin : ')
# val = site.removeprefix('https://www.').removesuffix('.com').upper().replace('K','C')
# print(val)
# # --------------------
# # 7-ci sual

# eded = input("Reqem daxil edin: ")
# eded = int(eded)
# if (eded % 7 == 0) and (eded % 3 == 0) and (eded % 8 == 0):
#     print('eded 3 7 8- e qaliqsiz bolunur')
# else:
#     print('eded 3 7 8- e qaliqsiz bolunmur')

# ---------------

# 8-ci sual

# vesiqe = input("Daxil edin: ")
# result = ""  # Define result outside of the if block

# if len(vesiqe) == 10:
#     result = vesiqe[:3].upper()
#     if result[3::10].isdigit():  # Check if the characters are all numeric
#         print(result)
#     else:
#         print("son 7 say reqem olmalidir")
# else:
#     print("10 xarakterden ibaret olmalidir !!")

# vesiqe=input("Sexsiyyeti daxil edin")

# if len(vesiqe)!=10:
#     print("10 xarakter olmalidir")
# else:
#     olke_qisaltmasi=vesiqe[:3]
#     if not olke_qisaltmasi.isalpha() or olke_qisaltmasi != olke_qisaltmasi.upper():
#         print ("Olke adini duzgun qeyd edin ")
#     else:
#         reqem=vesiqe[3:]
#         if not reqem.isdigit():
#             print("Son 7 say reqem olmalidir")
#         else:
#             print("Duzgundur")


# --------------------

# 9cu sual

# amount = int(input('Ne qeder mebleg daxil etmek isteyirsiniz? :'))

# if amount < 2000:
#     print('2000-den asagi kredit verilmir')
# elif amount < 10_000:
#     print("Yekun borc", amount*1.05, 'olacaq!')
# elif amount < 50_000:
#     print("Yekun borc", amount*1.04, 'olacaq!')

# elif amount < 200_000:
#     print("Yekun borc", amount*1.03, 'olacaq!')
# elif amount < 500_000:
#     print("Yekun borc", amount*1.02, 'olacaq!')

# else:
#     print("500,000-den artiq kredit verilmir")
 
