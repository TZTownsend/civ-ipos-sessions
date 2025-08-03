# animals = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}
#
# # # animals names/characteristics using for loop
# # animal_names = []
# # for name in animals:
# #     animal_names.append(name)
# # print(f"{animal_names=}")
# # animal_characteristics = []
# # for characteristic in animals.keys():
# #     animal_characteristics.append(characteristic)
# # print(f"{animal_characteristics=}")
#
# # # animals names/characteristics using list comprehension
# # animal_names = [name for name in animals]
# # animals_characteristics = [characteristic for characteristic in animals.values()]
#
# # animals names/characteristics using list constructor
# animal_names = list(animals.keys())
# # print(f"{animal_names=}")
# animal_characteristics = list(animals.values())
# # print(f"{animal_characteristics=}")
#
# # # create dictionary using for loop
# # new_animal_dictionary = {}
# # for name, characteristic in zip(animal_names, animal_characteristics):
# #     new_animal_dictionary[name] = characteristic
# # print(f"{new_animal_dictionary=}")
#
# # create dictionary using dictionary comprehension
# new_animal_dictionary = {name: characteristic for name, characteristic in zip(animal_names, animal_characteristics)}
# print(f"{new_animal_dictionary=}")
#
# class Animal():
#     def __init__(self, name, characteristic):
#         self.name = name
#         self.characteristic = characteristic
#
#     def modify_characteristic(self, new_characteristic):
#         self.characteristic = new_characteristic
#
#
# lion = Animal("Lion", "Brave")
# lion.modify_characteristic("Coward")
#
# animal_instances = {}
# for key, value in new_animal_dictionary.items():
#     animal_instances[key] = Animal(key, value)
# print(f"{animal_instances=}")


user_names = ["John", "Jake", "Tiffany"]
user_campus = ["East Perth", "Perth", "Perth"]
user_id = ["1", "2", "3"]

users = {identifier: [name, campus] for name, campus, identifier in
         zip(user_names, user_campus, user_id)}


class User:
    def __init__(self, identifier, name, campus, ):
        self.name = name
        self.campus = campus
        self.identifier = identifier

    def modify_name(self, new_name):
        self.name = new_name

    def get_identifier(self):
        return self.identifier


# # create user instances using for loop
# user_instances = {}
# for key, value in users.items():
#     user_instances[key] = User(key, value[0], value[1])
# print(f"{user_instances=}")

# create user instances using dictionary comprehension
user_instances = {key: User(key, value[0], value[1]) for key, value in
                  users.items()}
print(f"{user_instances=}")
print(f"{user_instances["3"].name=}")

user_instances["3"].modify_name("TiffanyZoe")
print(f"{user_instances["3"].name=}")

# TODO: How can I improve this?
user_found = False
for user in user_instances.values():
    if user.name == "Jake":
        user_found = True
        print(f"{user.get_identifier()=}")
        break
if not user_found: print("User not found")
