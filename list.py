menu_list = []
class Menu:

    def __init__(self, name, price, food):
        """
                Initialise the gui class in 2 columns including:
                - The top bar
                - the data collection frame
                - the data display window
        """
        self._name = name
        self._price = price
        self._food_meal = food

    def get_name(self):
        return (self._name)

    def get_price(self):
        return (self._price)

    def get_food_meal(self):
        return (self._food_meal)

menu_list.append(Menu('Cheese Burger', 10, 'burgers'))
menu_list.append(Menu('Chicken Burger', 13.50, 'burgers'))
menu_list.append(Menu('Extra large burger', 17, 'burgers'))
menu_list.append(Menu('Pork burger', 11.50, 'burgers'))
menu_list.append(Menu('Water', 2, 'drinks'))
menu_list.append(Menu('Pepsi', 3, 'drinks'))
menu_list.append(Menu('Coke', 3, 'drinks'))
menu_list.append(Menu('Orange juice', 3, 'drinks'))
menu_list.append(Menu('Potato chips', 7, 'sides'))
menu_list.append(Menu('Onion rings', 8, 'sides'))
menu_list.append(Menu('Coleslaw', 5, 'sides'))
menu_list.append(Menu('Chicken nuggets', 8, 'sides'))