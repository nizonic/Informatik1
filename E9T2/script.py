#!/usr/bin/env python3

class Fridge:
    def __init__(self):
        self.storage = []

    def __next__(self):
        pass

    def __iter__(self):
        return iter(self.storage)

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return f"Contents of fridge:\n{self.storage}"

    def find(self, name):
        for item in self.storage:
            if name is item[1]:
                return f"You have {name} you should eat by {item[0]} with the index {self.storage.index(item)}"

    def take(self, item):
        yes = None
        for groceries in self.storage:
            if item is groceries[1]:
                self.storage.remove(groceries)
                yes = True
        if yes is None:
            return None

    def take_before(self, date):
        going_bad = [items for items in self.storage if items[0] < date]
        self.storage = [items for items in self.storage if items not in going_bad]
        return going_bad

    def store(self, tup):
        self.storage.append(tup)
        self.storage.sort()


if __name__ == "__main__":
    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))
    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))

    print(f.find("Butter"))
    print(f.take_before(191200))
