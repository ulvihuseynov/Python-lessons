name="Ulvi"
last_Name='Huseynov'
space=" "
full_Name=name+ space+ last_Name
print(full_Name)

info="""
Python \n bir backend \n dilidir.
Javascript ise front dilidir
"""

print(info)

name="Ulvi"
last_Name='Huseynov'
# f-string new
print(f"Menim adim {name}, soyadim {last_Name}dur.")
# % format old
old_Version="Menim adim %s, soyadim %sdur." %(name,last_Name)
print(old_Version)
#  .format metodu
old_Format='Menim adim {}, soyadim {}dur'.format(name,last_Name)
print(old_Format)

# template formati

from string import Template

temp=Template('Menim adim $ad, soyadim $soyad dur')
result=temp.substitute(ad=name,soyad=last_Name)

print(result)

lang='PyThon'
print(lang[0])
print(lang[1])
print(lang[2])
print(lang[3])
print(lang[4])
print(lang[5])
print('-------')
print("reverse",lang[::-1])

print(lang[1:4])
print(lang[0:3])

print(lang[0:3:2])

print(lang[-1])
print(lang[-2])
print(lang[-3])
print(lang[-4])
print(lang[-5])
print(lang[0])
print("String methods")
print(len(lang))
print(lang.capitalize())
print(lang.upper())
print(lang.lower())
print(lang.endswith("n"))
print(lang.startswith('P'))
print('Javascript'.count('a'))
print('Javascript'.find('a'))
print('Javascript'.find('b'))
print('Javascript'.rfind('a'))
test='Html\tCss\tJs'
print(test.expandtabs(20))
print('Javascript'.index('p'))
print('Javascript'.rindex('a'))
print('Javascript'.islower())
print('Javascript'.isupper())
print('ulvi1937'.isalnum())
print('1937.3'.isnumeric())
print('ulvi1937'.isalpha())
print('2.1'.isdigit())
print('2.1'.isdecimal())

front=['html','css','js']
print('#'.join(front))
country='Azerbaijan, Georgia, Turkey,Pakistan'
print(country.split(' '))
print(country.replace('Georgia','Misir'))

head='welcomE to azerbaijan'

print(head.title())

# swapcase , isIdentifier, strip








