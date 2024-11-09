
person={
    "name":"Ulvi",
    "sur_Name":'Huseynov',
    "age":23,
    "city":"Baku",
    "skills":["HTML","CSS","JS","BOOTSTRAP"],
    "address":{
        "country":"Azerbaijan",
        "city":"Baku",


    }
}

print(person.keys())
print(person.values())
print(person.items())
# print(person.popitem())
# print(person.popitem())
# print(person.popitem())
# print(person.popitem())
# print(person.popitem())
# print(person.clear())
# print(person["sur_Name"])
# print(person.get('skills'))
print(len(person))
person["age"]=45
person["skills"].append('React JS')
person['isMarried']=False
print(person)
 

for item in person:
    print(item,person[item])


print(person["skills"][2])
print(person.pop('city'))

print('city' in person)
print('name' in person)
