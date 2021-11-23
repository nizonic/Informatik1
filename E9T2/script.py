#!/usr/bin/env python3

class Fridge:
    def __init__(self):
        self.__storage = []

    def store(self, tup):
        self.__storage.append(tup)
        self.__storage.sort()

    def take(self, item):
        if item not in self.__storage:
            raise Warning()
        self.__storage.remove(item)
        return item

    def find(self, name):
        for item in self.__storage:
            if name is item[1]:
                return item
        return None

    def take_before(self, date):
        going_bad = [items for items in self.__storage if items[0] < date]
        self.__storage = [items for items in self.__storage if items not in going_bad]
        return going_bad

    def __next__(self):
        pass

    def __iter__(self):
        return iter(self.__storage)

    def __len__(self):
        return len(self.__storage)

    def __str__(self):
        return f"Contents of fridge:\n{self.__storage}"


if __name__ == "__main__":
    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))
    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))

    print(f.find("Butter"))
    print(f.take_before(191200))
