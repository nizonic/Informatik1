
def where_is_waldo(names):
    try:
        return names.index("Waldo")
    except ValueError:
        return None

assert(where_is_waldo(["Peter", "Waldo", "John"]) == 1)
assert(where_is_waldo(["Peter", "Willy", "John"]) == None)
assert(where_is_waldo([]) == None)