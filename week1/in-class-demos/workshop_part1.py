crazy_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(crazy_list[3][1][2][0])

animals_list = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']

has_zebra = False
for animal in animals_list:
    if animal != 'Zebra':
        continue
    else:
        has_zebra = True
        break
try:
    print(f'"animals_list" contains Zebra: {has_zebra}')
except ValueError:
    print('No value found')


try:
    print(f'"animals_list" contains Zebra: {"Zebra" in animals_list}')
except ValueError:
    print('No value found')

#  pythonic solution
print('"animals_list" contains Zebra:', "Zebra" in animals_list)


try:
    print(f'"animals_list" second element is Giraffe: {animals_list[1] == "Giraffe"}')
except ValueError:
    print('No value found')

#  more pythonic solution
print('"animals_list" second element is Giraffe:', animals_list[1] == "Giraffe")


animals_list.append("Zebra")
try:
    print(animals_list.remove("Cheetah"))
except ValueError:
    print('No value found')


animals_tuple = tuple(animals_list)
# animals.append('Bear') cannot append to tuples

animals_dictionary = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}
print(f"{animals_dictionary=}")
animals_dictionary['Lion'] = 'King'
animals_dictionary_names_1 = []
animals_dictionary_characteristics_1 = []
for name, characteristic in animals_dictionary.items():
    animals_dictionary_names_1.append(name)
    animals_dictionary_characteristics_1.append(characteristic)
print(f"{animals_dictionary_names_1=}")
print(f"{animals_dictionary_characteristics_1=}")
# more pythonic
animal_names_2 = [name for name in animals_dictionary]
animal_characteristics_2 = [value for value in animals_dictionary.values()]
print(f"{animal_names_2=}")
print(f"{animal_characteristics_2=}")

new_animal_dictionary_1 = {}
for name, characteristic in zip(animal_names_2, animal_characteristics_2):
    new_animal_dictionary_1[name] = characteristic
print(f"{new_animal_dictionary_1=}")

# more pythonic
new_animal_dictionary_2 = {name: characteristic for name, characteristic in zip(animals_dictionary_names_1, animals_dictionary_characteristics_1)}
print(f"{new_animal_dictionary_2=}")


animals_set = set(animals_dictionary)
animals_set.add("Lion")
print(f"{animals_set}")

animals_titles = ["Bee", "Ant", "Fox", "Owl"]
animals_characteristics = ["busy", "industrious", "sly", "wise"]
animals_dictionary_zipped = dict(zip(animals_titles, animals_characteristics))


class Animal:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def modify_characteristic(self, new_characteristic):
        self.characteristic = new_characteristic


lion = Animal('Lion', 'King')
lion.modify_characteristic('Brave')

class_animals = []
for name, characteristic in animals_dictionary_zipped.items():
    class_animals.append(Animal(name, characteristic))

for animal in class_animals:
    print(animal.characteristic, animal.name)

for i, char in enumerate('abcde'):
    print (i, char)

for i, char in enumerate('abcde', 4):
    print (i, char)

for a, b in zip(range(4, 10, 2), 'abc'):
    print(a, b)
