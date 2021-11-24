from item import Item
from order import Order


class Restaurant:

    def __init__(self, restaurant_name, menu_list, revenue=0):
        self.__name = restaurant_name
        self.__menu = menu_list
        self.__revenue = revenue

    def get_restaurant_name(self):
        return self.__name

    def get_menu_list(self):
        return self.__menu

    def get_order_list(self):
        if not self.__order:
            return "No order yet"
        return self.__order

    def set_order(self, item_list):
        item_list = [item for item in item_list if item in self.__menu]
        self.__order = Order(item_list)
        self.__revenue += self.__order.get_bill_amount()

    def get_revenue(self):
        return self.__revenue




# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak, salad, fish]
    # Create order list
    order_list = [steak, steak, salad, pizza]
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    # Get the revenue of the restaurant object
    #print(restaurant.get_revenue())
    print(restaurant.get_order_list())
    order_list = [steak, steak, steak, steak]
    restaurant.set_order(order_list)
    print(restaurant.get_order_list())
    print(restaurant.get_revenue())