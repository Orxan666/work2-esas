# REGULAR EXPRESSIONS


# value=re.match('[Pp]+',text)
# print(value)

# value=re.match('[Pp]y*',text)
# print(value)

# import re

# text='pZython oyrenirem'

# value=re.match('[PpZz]{1,2}y?thon+',text)
# value=re.match('^n',text)

# print(value)

# [] boyuk balaca herfleri qeyd edirik qarsiliq gelen deyeri daxil edirik 
# ? ola da biler olmayada biler 
#  + qoyanda en az bir dene olmalidir
# * hec olmuyada biler istenilen qeder ola da biler 

# ^ bundan xaric hamisini ver

# text='aazsvddkeAKGITHBJCdvDVDVsdvsDV121873456789!#$%^\t    \n&*_+=(@'

# value=re.search('[a-z]+',text) #match basdan basliyaraq yoxluyur
# print(value)
# value =re.search('[A-Z]+',text)
# value =re.search('[A-z]+',text)
# print(value)
# value =re.search('[a-zA-z]+',text)
# value =re.search('[A-Z]+[a-z]+',text)
# value=re.search('[1-3]+',text)
# value=re.search('[^A-z]+',text)
# value=re.search('[0-9]+',text)
# print(value)
# ---------
# value=re.search('\d+',text)#[0-9]
# value=re.search('\s+',text)#[\t \n]
# print(value)
# value=re.search('\w+',text)#[A-Za-z0-9_]
# value=re.search('\D+',text)#[^0-9]
# value=re.search('\S+',text)#[^\t\n]
# value=re.search('\W+',text)#[^A-Za-z0-9_]
# print(value)
# print(value)


# Ev tapsirigi

# 1)
# names=['Aygun Kazimova', 'fermer Həsən', 'Namiq Qaracuxurlu', 'Rehim Rehimli', 'roya Ayxan', 'Eynulla']
# pattern='^[A-Z][a-z]+ [A-Z][a-z]'
# import re
# for name in names:
#     value=re.search(pattern,name)
#     if value:
#         print(value)
# ----------------------------
# 2-ci sual sehvdir 
# ==========================
# 3)
# import re
# text="""Dünyada bir çox saytlar mövcuddur. Bunların bir çoxu fərqli məqsədlərə xidmət edirlər. Müsal üçün http://www.google.com saytı axtarış üçün istifadə olunur. Digər yandan https://facebook.com və http://www.instagram.com saytları sosial şəbəkə kimi fəaliyyət göstərirlər"""
# pattern=r'https?://[\w.]+'
# result=re.findall(pattern,text)
# print(result)


# 5)
# numbers_text="""051-235-642-12, 055-236-642-23, 077-623-234-26, 51-125-646-32, 50-125-542-12, 70-253-644-12, 050-135-346-64"""


# pattern=r'0?5[01]-\d{3}-\d{3}-\d{2}'
# azercell_number=re.findall(pattern,numbers_text)
# print(azercell_number)

# -----------Compile

# names=['Aygun Kazimova', 'fermer Həsən', 'Namiq Qaracuxurlu', 'Rehim Rehimli', 'roya Ayxan', 'Eynulla']
# pattern='^[A-Z][a-z]+ [A-Z][a-z]+$'
# import re
# compiled=re.compile(pattern)
# for name in names:
#     value=compiled.search(name)
#     if value:
#         print(value)

# import re
# text="""Salam necesen Orxan hardasan Bakidasanmi Isde olan mehsullar bulardi



# 1.Metbex mebelleri 50%
# 2.Geyim desti 40%
# 3.Elektron aletler 20%;

# """
# result=re.findall('[A-z]+',text,re.I)

# print(result)

# text="""
# Cavid Rustemzade.
# Fuad Qasimov.
# Fettayeva Nermine.
# Behram Memmedov.

# """

# print(re.findall('.',text,re.DOTALL))



# result=re.findall('[a-z]+',text,re.I)
# print(result)

# import re

# url = 'https://www.compar.edu.az'

# re_match = re.search(r'^(https?)://(\w+)\.(\w+)\.(\w+)', url)

# print(re_match.groups())


