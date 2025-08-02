# def update_immutable_1():
#     a1 = 42  # global a1 is immutable therefore a local a1 variable is created within the scope of the function
# immutable_a1 = 24  # immutable global variable
# update_immutable_1() # no changes to global immutable_a1 variable as it is immutable
# print(immutable_a1) # Output: 24


# def update_immutable_2():
#     print(immutable_2)
# immutable_2 = 24  # immutable global variable
# update_immutable_2() # Output: 24
# print(immutable_2) # Output: 24


# def update_immutable_3():
#     print(immutable_3)
# update_immutable_3()  # Output: NameError as variable immutable_3 not defined at this point
# immutable_3 = 24
# print(immutable_3)


# def update_immutable_4():
#     immutable_4 = 42  # global immutable_4 is immutable therefore a local  immutable_4 variable is created within the scope of the function
#     print(immutable_4)  # local immutable_4 variable is used
# immutable_4 = 24  # immutable global variable
# update_immutable_4()  # Output 42
# print(immutable_4)  # Output 24


# def update_immutable_5():
#     print(immutable_5)  # there is a local immutable_5 assigned within the scope of the function but it is called before it is assigned and an UnboundLocalError is raised
#     immutable_5 = 42
# immutable_5 = 24
# update_immutable_5()
# print(immutable_5)


# def update_immutable_6(immutable_6):
#     immutable_6 = 42  # local variable created as global immutable_6 is immutable
# immutable_6 = 24
# update_immutable_6(immutable_6)
# print(immutable_6)  # Output 24


# def update_mutable_1():
#     mutable_1[0] = 42  # global variable b1 is mutable and changed.
# mutable_1 = [24]  # mutable global variable
# update_mutable_1()
# print(mutable_1)  # Output: [42]


# def update_mutable_immutable(mutable, immutable):
#     mutable.append(42)  # global variable is mutable and changed.
#     immutable = 42  #global variable  global variable is immutable and new local variable created
# mutable = [24]  # mutable global variable
# immutable = 24  # mutable global variable
# update_mutable_immutable(mutable, immutable)
# print(mutable)  # Output: [24, 42]
# print(immutable)  # Output: 24

# a = 42
# b = 42
# c = 24
# d = [24]
# e = [24]
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d[0]))
# print(id(d))
# print(id(e))
# print(id(d[0]))
# print(id(e[0]))


# def modify(n, list_):
#     n = 2
#     list_.append(3)
# n = 1
# list_ = [1, 2]
# modify(n, list_)
# print(n)  # Output: 1
# print(list_)  # Output: [1, 2, 3]

# def modify_list(list_):
#     list_.append("new")
#     list_ = ["completely", "new"]  # this is a new list object therefore a different reference to that passed in to the function
# items = ["original"]
# modify_list(items)
# print(items)  # Output ["original", "new"]


# def update_c(c=[]):  # default argument is mutable (dangerous!!). See below for multiple calls to this function.
#     c.append(42)
#     return c
# c = update_c()
# print(c)  # Output: [42]
# c = update_c()  # object pointed to by a already exists and is mutable
# print(c)  # Output: [42, 42]
# c = update_c()  # object pointed to by a already exists and is mutable
# print(c)  # Output: [42, 42]

