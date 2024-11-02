# Arithmetic Operators:
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b
# 2. Müqayisə Operatorları
# Dəyərləri müqayisə etmək üçün istifadə olunur, nəticə olaraq True və ya False qaytarır.

# ==: bərabərdirmi?
# !=: bərabər deyilmi?
# >: böyüktürmü?
# <: kiçikdir?
# >=: böyük və ya bərabər?
# <=: kiçik və ya bərabər?
print(5+7j)
print((4>2)or (4<2))



l=16
p=4
print(l//p)

print((5**2)+(30//10))

print(7 and 9)
t=('alma','nar','armud')
o=('alma','nar','armud','borani','qarpiz')
print(not len(t)<len(o) or 9==12)

# print(PI)

#  is is not in not in
arr=['car','grape','ball','pie']

print('carc' not in arr)


print(1 is 1)
print(4 is 2**2)
print(4 is not 3)

first_name='Ulvi'
age=24
print(f"Hello {first_name}")
print(f"{age} years old")

price=30
quantity=12
print(f"total:{price * quantity}$")
print(float(12))

is_Student=False

if is_Student:
    print("You are student")
else:
    print("You are not student")



name="ulvi"
age=23
PI=3.14
is_Student=False

print(type(name))
age=str(age)
print(type(age))
print(int(PI))
print(type(is_Student))
# print(int(name))

# name=input("What is your name: ")
# age=input("How old are you")
# age=int(age)
# age+=1
# print(f"Hello {name} ")
# print("Happy birthday")
# print(f"You are {int(age)} years old")


# length=float(input("length"))
# width=float(input("width"))
# area=length*width


# print(f"the area is: {area}")


item=input('alacagin mehsulu yaz')
price=float(input("qiymet: "))
quantity =int(input('sayini qeyd et'))
total=price*quantity

print(f"{quantity} x {item} aldin")
print(f"{total}")
