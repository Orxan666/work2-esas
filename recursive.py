# def factorial(number):
#     if number==0:
#         return 1
#     return number*factorial(number-1)


# print(factorial(1))

# ---------------

# a=[1,5,[2,1,[3,1],],5,[2,3],5,3,[1,[1,2,[9,10],3,7],3],1,6]
# def flat(li):
#     result=[]
#     for el in li:
#         if type(el) != list:
#             result.append(el)
#         else:
#             result.extend(flat(el))
#     return result

# print(flat(a))

# my_dict={
#     'ad':'Eli',
#     'soyad':'Eliyev'

# }

# print(dir(my_dict))

# def factorial(number):
#     if number==0:
#         return 1
#     return number*factorial(number-1)

# print(factorial(5))
# ----------------
# a=[1,5,[2,1,[3,1],],5,[2,3],5,3,[1,[1,2,[9,10],3,7],3],1,6]
# def flat(li):
#     result=[]
#     for el in li:
#         if type(el) != list:
#             result.append(el)
#         else:
#             result.extend(flat(el))
#     return result

# print(flat(a))

# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner

# def decor(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner

# @decor1
# @decor
# def num():
#     return 10

# @decor
# @decor1
# def num2():
#     return 10

# print(num())
# print(num2())

# boolean_list = ['True', 'True', '']

# result=all(boolean_list)

# print(result)


# Home-Work 17====================

# 1-ci sual
# factorial=lambda x : 1 if x==0 else x*factorial(x-1)
# print(factorial(5))
# -------------------------------------

# 2-ci sual

# letdict = {'a': 1, 'v': {'b': 2}, 'c': {'f': 3, 'c': 3, 'h': {'r': 5}, 'p': 3}, 'y': 9}
# # # output: {' ': 3, 'r': 5, 'p': 3, 'y': 9}

# def seperate(roya):
#     rest_dict={}
#     for key,value in roya.items():
#         if not isinstance(value,dict):
#             rest_dict[key]=value
#         else:
#             rest_dict.update(seperate(value))
#     return rest_dict

# print(seperate(letdict))


# -----------------
# 3-cu sual
# numbers = [85856, 73930, 95298, 57870, 1000000, 99688, 92907, 13075, 12905, 52948,
#            97687, 10832, 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400]


# def get_digits_sum(number):
#     digits = map(lambda x: int(x), str(number))
#     return sum(digits)




# max_value=max(numbers,key=get_digits_sum)
# print(max_value)
# print(get_digits_sum(max_value))

# # ---------------
# 4-cu sual

# children = ['Arif', 'Babek', 'Hesen', 'Rufet', 'Sahin', 'Eldeniz', 'Turan', 'Sahmar', 'Kamal', 'Ruslan']
# gifts = ['Ball', 'Iphone', 'Bicycle', 'Ball', 'Piano', 'Bicycle', 'Socks', 'Play Station', 'Ball', 'Socks']
# prices = {'Ball': 10, 'Iphone': 1100, 'Bicycle': 500, 'Piano': 1500, 'Socks': 10, 'Play Station': 1200}

# children_gifts=zip(children,gifts)
# print(children_gifts)
# sorted_children_gifts=sorted(children_gifts,key=lambda x:prices.get(x[1]),reverse=True)
# # print(sorted_children_gifts)
# for child,gift in sorted_children_gifts:
#     print('{} {} manat deyerinde {} goturub'.format(child,prices[gift],gift))

# ================================
# 5-ci sual

# types =[list,bool,dict,int ,float,str]

# data=[{'a': 1, 'b': 2}, 5, 7.8, 'asdf', 23, ['a', 'b'], True,  False]

# data_sorted=sorted(data,key=lambda el :types.index(type(el)))

# print(data_sorted)

# mySet={1,2,3,4,5,5}
# print(mySet)

myset=set()
print(type(myset))