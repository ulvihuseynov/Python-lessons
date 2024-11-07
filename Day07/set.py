new_Set=set()
print(type (new_Set))
new_Set.add('Ulvi')
new_Set.add('Huseynov')
new_Set.add(23)
new_Set.remove(23)
new_Set.update(['Baku','Bayil','Kurdamir'])
new_Set.clear()
print(new_Set)
new_Set.update(['Kamal','Ramal','Zaman','Ramin','Rahim'])
print(new_Set)
result=new_Set.pop()
print(result)
# del new_Set

name={'Famil','Samir','Amil','Tahir'}
arr=list(name)
print(arr)

surname={'Familov','Samirov','Amilov','Tahirov'}

union_Set=name.union(surname)
print(union_Set)

whole_Numbers={0,1,2,3,4,5,6,7,8,9,10}
other_Numbers={11,12,13,14}

even_Numbers={0,2,4,6,8,10}
print(whole_Numbers.intersection(even_Numbers))
print(whole_Numbers.difference(even_Numbers))
print(whole_Numbers.isdisjoint(even_Numbers))
print(whole_Numbers.isdisjoint(other_Numbers))

for item in whole_Numbers:
    print(item)

