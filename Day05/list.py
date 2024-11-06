arr=list()
print(arr)
array=[]
print(array)

names=['Ulvi','Kamal','Ramal','Zaman','Azad','Manaf','Roman','Ayxan']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(len(names))
print(names[-3])
print(names[3:6])
print(names[1:4])
print(names[-4:-1])

print(names.index('Zaman'))
# method_Pop=names.pop()
# print(method_Pop)
# print(names.pop(0))
names.sort(reverse=True)

print(names)
names.sort()
print(names)
names.reverse()
print(names)
num=[4,52,-1,7,3,11,-4]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

fruits=['apple','lemon','grape','pie']

fruits.append('mango')

print(fruits)

fruits.remove('apple')
print(fruits)

fruits.clear()
print(fruits)


country=['Aze','Tur','Geo','Cro']
country.insert(2,'Bel')

print(country)

say=country.count('Aze')
print(say)
# names=country

# print(names)

names.extend(country)

print(names)


for item in names:
    print(item)


print('Qalib' in names)

list1=[1,2,3,4]
list2=[5,6,7,8]
list3=list1+list2
print(list3)



first,second,three,*rest=names
print(*rest)
