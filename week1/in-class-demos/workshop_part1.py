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


try:
    print(f'"animals_list" second element is Giraffe: {animals_list[1] == "Giraffe"}')
except ValueError:
    print('No value found')


animals_list.append("Zebra")
try:
    print(animals_list.remove("Cheetah"))
except ValueError:
    print('No value found')


animals_tuple = tuple(animals_list)
# animals.append('Bear') cannot append to tuples

animals_dictionary = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}
print(animals_dictionary)
animals_dictionary['Lion'] = 'King'
animals_set = set(animals_dictionary)
animals_set.add("Lion")
print(animals_set)

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