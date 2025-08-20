# number=15
# result=1

# for i in range(1,number+1):
#     result*=i

# print(result)


# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# factorial(5)
# def combination(n, r):
#     return(factorial(n)/(factorial(r)*factorial(n-r)))

# print(combination(5,3))
# print(combination(10,3))
# print(combination(15,2))


# def get_site_name(site,sireli="www.",rufet=".com"):
#     return site.removesuffix(sireli).removeprefix(rufet).capitalize()
# print(get_site_name("compar"+" saytina xos gelmisiniz."))


# print(get_site_name('google','www.',".com"))
# print(get_site_name(site='www.google.com',pref='www.',suf=".com"))


# def getManat(*dollars):
#     result=0
#     for d in dollars:
#         result+=d
#     result=result*1.7
#     return round(result,2)
# # print(getManat(10,10))
# print(getManat(13,45,12,54,32))


# def factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*factorial(n-1)
# print(factorial(6))
# def get_sum(numbers):
#     result=0
#     for i in numbers:
#         result+=i
#     return result

# def get_curreny(*args, **kwargs):
#     print(args,kwargs)
#     for key,value in kwargs.items():
#         print(f'{key.upper()}umumi qiymeti: {get_sum(args)*value}')

# get_curreny(12,53,12,54,azn=1.7,tl=20)


# print(get_sum([12,53,12,54]))


# --------------------------

# number=5

# result=1

# for i in range(1,number+1):
#     result*=i

# print(result)
# # ---------

# number=6

# result=1

# for i in range(1,number+1):
#     result=result*i
# print(result)
# print(dir(55))


# def factorial(reqem):
#     result=1
#     for i in range(1,reqem+1):
#         result*=i
#     return result


# print(factorial(5))
# print(factorial(10))
# print(factorial(20))
# print(factorial(30))





# result=int(input("Reqem daxil edin")) 

# def test(reqem1):
#     if reqem1%2==0:
#         return reqem1
#     else:
#         return "reqem 2 ye bolunmur"


# print(test(result))


# def topla(*args):
#     return sum(args)

# print(topla(1,2,3))



# Home Work Function
# =========================
# 1)Girilen stringlərin ilk hərfini böyüdüb, birləşdirən bir funksiya hazırlayın.
# upunion('birlesmis', 'milletler', 'teskilati') => 'BMT'

# cls

# upuion('Birlesmis', 'milletler','teskilati')
# upuion("avropa","surasi")
# upuion("birlesmis","milletler","teskilati")
# ----
# govs=[
#    [ 'birlesmis','milletler','teskilati'],
#    ['Azerbaycan','respublikasi'],
#    ['Demir','Yol','vagzali']

# ]

# result=[upuion(*gov)for gov in govs]
# print(result)

# -----2ci sual
# Girilen stringi qeyd edilen sekilde deyisen bir funksiya hazirlayin
# chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren') =>
# 'Kitabi sehife-sehife oxumalisan ki, oyrenesen'

# def chstr(text,**kwargs):
#     for key,value in kwargs.items():
#         text=text.replace(key,value)
#     return text

# print(chstr('Kitabi sehve-sehve oxumalisiz ki, orgenesen', sehve='sehife', orgen='oyren',oxumalisiz="oxumalisan"))


# 3-cu sual
# def find_percent(first,second):
#     diff=first -second
#     percent=(abs(diff)/first)*100
#     if first > second:
#         print(f'qiymet{percent}% azalmisdir')
#     elif first < second:
#         print(f'qiymet {percent}% artmisdir')
#     else:
#         print('qiymet deyismeyib')

# find_percent(50,50)
# find_percent(100,150)

# 4-cu sual

# def big_dif_sml(list):
#     result=max(list)-min(list)
#     return result

# print(big_dif_sml([1,2,3,4,5,6,9]))



# 5-ci sual
# üç rəqəmli ədədləri sözə çevirən bir funksiya hazırlayın. Örnək output:
# eded_cevir(658) => altı yüz əlli səkkiz

# eded_ad = {
#     0: {'1': 'bir', '2': 'iki', '3': 'uc', '4': 'dort', '5': 'bes', '6': 'alti', '7': 'yeddi', '8': 'sekkiz', '9': 'doqquz'},
#     1: {'1': 'on', '2': 'iyirmi', '3': 'otuz', '4': 'qirx', '5': 'elli', '6': 'altmis', '7': 'yedmis', '8': 'seksen', '9': 'doxsan'},
#     2: {'1': 'yuz', '2': 'ikiyuz', '3': 'ucyuz', '4': 'dortyuz', '5': 'besyuz', '6': 'altiyuz', '7': 'yeddiyuz', '8': 'sekkizyuz', '9': 'doqquzyuz'},
#     3: {'1': 'min', '2': 'ikimin', '3': 'ucmin', '4': 'dortmin', '5': 'besmin', '6': 'altimin', '7': 'yeddimin', '8': 'sekkizmin', '9': 'doqquzmin'}
# }
# def get_number_name(eded):
#     revnum = str(eded)[::-1]
#     result = ' '
#     for index, digit in enumerate(revnum):
#         if digit=='0':
#             continue
#         word = eded_ad.get(index).get(digit)
#         result = word + ' ' + result
#     return result
# print(get_number_name(2400))



# 6)Verilmiş ədədləri tərsinə çevirib toplayan bir funksiya hazırlayın
# print(getReversedSum(123, 567, 562, ...))
# result: 1351

# def get_reversed(num):
#     num=str(num)[::-1]
#     num=int(num)
#     return num

# def get_reversed_sum(*args):
#     result=0
#     for i in args:
#         result+=get_reversed(i)
#     return result

# print(get_reversed_sum(10,100))

# LAMBDA
# -------------------------

# get_reversed=lambda num:int(str(num)[::-1])
# print(get_reversed(2345))

# numbers=[1234,3456,7890]
# # numbers2=[1234,23343456,7890]

# def deyis(l,callback):
#     return [callback(i) for i in l]


# print(deyis(numbers,get_reversed))


# mehemmed=lambda num:int(str(num)[::-1])

# print(mehemmed(123))

# numbers=[123,456,789]

# def ters_cevir(mylist,callback):
#     return [callback(i) for i in mylist]


# print(ters_cevir(numbers,mehemmed))


# myList=[123,456,789]
# get_reversed=lambda num:int(str(num)[::-1])

# def get_reversed(number):
#     number=str(number)[::-1]
#     number=int(number)
#     return number

# def change(l,rufet):
#     return [rufet(i) for i in l]

# print(change(myList,get_reversed))

# ============

# numbers=[123,234,456]
# def get_100_times(num):
#     return num*100


# def deyis(l,callback):
#     return [callback(i) for i in l]

# print(deyis(numbers,get_100_times))
# print(deyis(numbers,lambda num : num**2))




# def factorial(x):
#     if  x==1:
#         return x
#     else:
#         return (x*factorial(x-1))
    
# print(factorial(999))

# nummbers=[12,24,33,45]

# def vurma(number):
#     return number**2


# def seyyar(l,sireli):
#     return [sireli(i) for i in l]

# print(seyyar(nummbers,vurma))
# animals = ['dog', 'cat', 'parrot', 'rabbit']
 
# uppered_animals = list(map(lambda animal: animal.upper(), animals))
 
# print(uppered_animals)


# number1=2
# number2=4
# result=number1+number2
# print(result)

# def topla():
#     print("Hello world")
# topla()

# def topla(number1,number2=4):
#     return (number1 + number2)

# print(topla(5))
# def personal(firstName,lastName):
#     return  f"Salam {firstName}\n sizin soyadiniz {lastName}"

# print(personal("Taleh","Qurbanov"))

# def kvadrataYukselt(number):
#     result=number**number
#     return result

# print(kvadrataYukselt(9))

# def test():
#     pass

# print("salam")

# result=pow(2,4)
# print(result)


# def topla(x):
#     def komekci(y):
#         return x+y
#     return komekci

# add_num=topla(5) 
# result=add_num(4)





# print(result)