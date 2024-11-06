my_tuple=()
myTuple=1,2,3,4
print(my_tuple)
print(myTuple)

odd_Tuple=(1,)

print(type(odd_Tuple))

names=('Ulvi','Zulfiqar','Kamran','Rasim')
print(names)
print(names[3])
print(names[-3])

for name in names:
    print(name)


obj=(
    {'name':'Ulvi',
      "age":24,
      "city":'Baku'},
      {'name':'Zaman',
      "age":54,
      "city":'London'},
      {'name':'Akif',
      "age":56,
      "city":'Limassol'},
)
print(obj)

for item in obj:
    print(item)


num=(10,20,30,40,50,60)
print(num[1:4])
print(num[::-1])
# num[2]=34
# print(num)
print(20 in num)
change_List=list(num)

print(change_List)
change_List[2]=34
print(change_List)


item1=(1,2,3,4)
item2=(5,6,7,8)
print(item1+item2)
