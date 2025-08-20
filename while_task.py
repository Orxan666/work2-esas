# num=1
# result=0

# while num<=100:
#     result+=num
#     num+=1
# print(result)
# =============

# num = 10000

# while num > 0:
#     if num % 9999 == 0:
#         print(num)
#     num -= 1
#     break

# print(num)
# ============
# text = 'Men her gun Python oyrenirem'
# saitler = 'aıoueəiöü'
# result = ''
# counter = len(text) - 1

# while counter >= 0:
#     result += str(saitler.find(text[counter]))
#     counter -= 1

# print(result)

# ===================
# FOR TASK

# i=0

# for number in range(101):
#     i+=number

# print(i)
# ----------


# for i in range(100000,0,-1):
#     if(i%9999==0):
#         break
# print(i)
# ---------------
# sentence="Men her gun Python oyrenirem"
# vowels='aıoeuüəiöü'
# result=''

# for char in sentence:
#     if char not in vowels:
#         result+=char
# print(result)
# # ====================
vowels = "aıoeuüəiöü"
sentence = input("Cümlə daxil edin: ").lower()

syllable_count = 0

for i in range(1, len(sentence)):
    if sentence[i] in vowels and sentence[i-1] not in vowels and sentence[i-1].isalpha():
        syllable_count += 1

# Əgər cümlənin ilk hərfi saitdirsə, onu sayma:
# Amma "samitdən sonra gələn sait" sayıldığı üçün ilk heca onsuz da sayılmır

print("Heca sayı:", syllable_count)



sentence='Men her gun Python oyrenirem'
vowels='aıoeuüəiöü'
result=''

for i in sentence:
    if i not in vowels:
        result+=i

print(result[::-1])   





# if True:
#     a=5

# print(a)