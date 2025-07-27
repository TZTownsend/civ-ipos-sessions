NUMBER_OF_BOTTLES = 99


def main():
    bottle_or_bottles = "bottles"
    drink_or_store = "Take one down, and pass it around,"

    for bottles in range(NUMBER_OF_BOTTLES, 0, -1):
        print(f"{bottles} {bottle_or_bottles} of beer on the wall,\n"
              f"{bottles} {bottle_or_bottles} of beer,\n"
              f"{drink_or_store}")
        bottles -= 1
        if bottles == 1:
            bottle_or_bottles = "bottle"
        else:
            bottle_or_bottles = "bottles"
        if bottles == 0:
            drink_or_store = "Go to the store and buy some more,"
        else:
            drink_or_store = "Take one down, and pass it around,"
        print(f"{bottles} {bottle_or_bottles} of beer on the wall!\n")


if __name__ == "__main__":
    main()
