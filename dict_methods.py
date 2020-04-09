print("\n\033[7mget()\033[m")

person = {'name': 'Jack', 'age': 22}

print('Name: ', person.get('name'))

print('Salary: ', person.get('salary'))  # value is not provided... returns None

print('Salary: ', person.get('salary', 0.0))  # value is provided

print("\n\033[7mcopy()\033[m")

original = {1: 'one', 2: 'two'}
new = original.copy()  # a copia nao é ligada ao original

original[3] = 'three'  # adiciona um terceiro valor mas apenas na original
print(original)
print(new)

print("\n\033[7mfromkeys()\033[m")

keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'
number = [1]
vowels = dict.fromkeys(keys)
print(vowels)

vowels2 = dict.fromkeys(keys, value)
print(vowels2)

vowels3 = dict.fromkeys(keys, number)
print(vowels3)
number.append(2)  # Problem
print(vowels3)

print("\n\033[7mDictComprehension\033[m")

number = [1]
vowels4 = {key: list(number) for key in keys}
print(vowels4)
number.append(2)  # não ira alterar o vowels4
print(vowels4)

print("\n\033[7mitems()\033[m")
sales = {'apple': 5, 'orange': 4, 'lemon': 8}

items = sales.items()
print(items)

del [sales['apple']]
print(items)

print("\n\033[7mkeys()\033[m")

keys = sales.keys()
print(keys)

sales.update({'banana': 12})
print(keys)

print("\n\033[7mvalues()\033[m")
valores = sales.values()
print(valores)

print("\n\033[7mpopitem()\033[m")

animal = {'name': 'zebra', 'age': 10, 'color': 'black and white'}

result = animal.popitem()
print(animal)
print(result)

print("\n\033[7msetdefault()\033[m")

man = {'name': 'Jack'}

salary = man.setdefault('salary')
print(man)
print(salary)

age = man.setdefault('age', "22")
print(man)
print(age)

print("\n\033[7mpop()\033[m")

print(sales)
element = sales.pop('orange')
print(element)
print(sales)

element2 = sales.pop('grape', 'Key not found')
print(element2)
print(sales)

print("\n\033[7mupdate()\033[m")

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)

print()
dd = {'x': 2}
print(dd)
dd.update(y=3, z=0)
print(dd)
