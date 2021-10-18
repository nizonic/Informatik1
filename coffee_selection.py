def get_sane_user_input():
    selection = 0
    while not selection:
        user_input = input("Machine ready, select beverage...\n"
                           "1: Coffee\n"
                           "2: Espresso\n"
                           "3: Doppio\n"
                           "4: Ristretto\n")
        if not user_input.isdigit():
            print("not a number")
            continue
        selection = int(user_input)
        if not 0 < selection <= 4:
            print("invalid number")
            selection = 0
            continue
    return selection


def get_amount(selection):
    if selection == 1:
        return 15, 15
    elif selection == 2:
        return 60, 15
    elif selection == 3:
        return 60, 30
    elif selection == 4:
        return 30, 15


def basic_coffe_maker():
    selection = get_sane_user_input()
    water, coffee = get_amount(selection)

    print(f"Using {water}ml of water and  {coffee}g of coffee")


basic_coffe_maker()
