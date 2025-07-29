NUMBER_OF_BOTTLES = 99


def main():
    bottle_or_bottles = "bottles"

    for bottles in range(NUMBER_OF_BOTTLES, 0, -1):
        print(f"{bottles} {bottle_or_bottles} of beer on the wall,\n"
              f"{bottles} {bottle_or_bottles} of beer,")
        bottles -= 1
        if bottles == 0:
            bottles = "No more"
        if bottles == 1:
            bottle_or_bottles = "bottle"
        else:
            bottle_or_bottles = "bottles"
        print("Take one down, and pass it around,\n"
              f"{bottles} {bottle_or_bottles} of beer on the wall!\n")
    else:
        print("No more bottles of beer on the wall,\n"
              "No more bottles of beer,\n"
              "Go to the store and buy some more,\n"
              f"{NUMBER_OF_BOTTLES} bottles of beer on the wall.\n")


if __name__ == "__main__":
    main()
