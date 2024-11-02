# Pythonda olan daxili funksiyalar 
print("Hello variable")  # 1 print
y=[1,2,3,4,5]
print(len("ulvi"))  # 2 len uzunlugu qaytarir
print(len(y))           
print(len("ulvi"))  # 2 len uzunlugu qaytarir

print(type(5))
print(type(5.7))
print(type({12,34,2.3}))
print(type('Huseynov'))      #3 type  tipini qaytarir

print(abs(-9))    #4 abs mutleq qiymeti qaytarir  9
print(abs(-24))     # 24

print(min([32,12,11,9,5]))   #5  min en kiciyi qaytarir
print(max(23,56,12,57))      #6  max en kiciyi qaytarir

print(int(9.87))
print(float(9))
x=9.87
print(str(x))
print(type(str(x)))

number=[1,2,3,4,5,6,7,8,9,10]
result=sum(number)    # sum cemlemek ucun istifade olunur
print(result)

total=0         # el ile sum yazmaq usulu 
for item in number:
  total+=item
print(total)

# ad =input("adinizi yazin")
# print("adim" + ad)

sort=[4,0,-5,21,14,11,18,6]
print(sorted(sort))

print(round(9.7))
print(round(9.1))

names=['kamil','famil']
ages=[45,87]

for name,age in zip(names,ages):
  print(name,age)


for item in range(10):
  print(item)


first_name="Ulvi"
sur_Name='Huseynov'
city="Baku"
person_info={
  "name":"Ulvi",
  "surName":"Huseynov",
  "age":23
}
print(first_name,sur_Name,city,person_info)

print(len(person_info))

ad,soyad,yas='ulvi','huseynov',23
print(ad,soyad,yas)

d=30
l=20
m=d+l
print(m)