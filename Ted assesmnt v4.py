# Imports
from appJar import gui
# Variables
food_list = []
Order_list = []
price = 0
limit = 0

# Functions
class Menu:
    """
    Class to set up and display gui
    Also manages the button events
    """
    def __init__(self, name, price, food):
        """
                Initialise the gui class in 2 columns including:
                - The top bar
                - the data collection frame
                - the data display window
        """
        self._name = name
        self._price = price
        self._food_type = food

    def get_name(self):
            return (self._name)

    def get_price(self):
            return (self._price)

    def get_food(self):
            return (self._food)

food_list.append(Menu('Cheese Burger', 14, 'Burger'))
food_list.append(Menu('Chicken Burger', 14, 'Burger'))
food_list.append(Menu('Beef Burger', 12, 'Burger'))
food_list.append(Menu('Fish Burger', 11, 'Burger'))
food_list.append(Menu('Water', 1, 'Drink'))
food_list.append(Menu('Milk', 14, 'Drink'))
food_list.append(Menu('Coke', 12, 'Drink'))
food_list.append(Menu('Orange', 13, 'Drink'))
food_list.append(Menu('Chips', 14, 'Sides'))
food_list.append(Menu('Orange', 14, 'Sides'))
food_list.append(Menu('Salad', 9, 'Sides'))
food_list.append(Menu('Nugget', 14, 'Sides'))

class Gui:
    def __init__(self):
        app = gui("Gui fast food menu", "1750x920")
        self._app = app
        app.addLabel("title", colspan=2)
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")

        with app.frame("Back"):
            app.addButton("Back", self.press)

        with app.frameStack("stack"):
            """
            stacks the frames giving the ability to switch through
            the frames seamlessy without any errors
            """
            with app.frame("data_collection"):
                """
                This frame control the selection of catergories
                """
                app.setLabel("title", "Fast food")
                app.setLabelBg("title", "white")
                app.setLabelFg("title", "grey")
                app.setImageLocation("images")
                app.addImage("images", "image.jpeg")
                app.addButtons(["Food", "Drinks"], self.press)
            with app.frame("food display"):
                """
                This frame controls the food section
                """
                app.addButtons(["burger", "fries", "melon"], self.press)
                app.setBg("lightBlue")
                app.setFont(20)


            with app.frame("data_display"):
                """
                this frame controls the liquids sections
                """
                app.addButtons(["coke", "pepsi", "water"], self.press)
                app.setBg("lightBlue")
                app.setFont(20)
            with app.frame("burgers"):
                app.addButtons(["cheese burger", "XL cheese burger", "bacon sandwich"], self.press)
                app.setBg("lightBlue")
                app.setFont(20)



        app.firstFrame("stack")  # Sets the first frame added to stack to display first
        app.go()
        
    def start_app(self):
        self._app.go()
    def press(self, btn):
        if btn == "Food":
            self._app.nextFrame("stack")
        elif btn == "Back":
            self._app.firstFrame("stack")
        elif btn == "Drinks":
            self._app.selectFrame("stack", 2)
        elif btn == "burger":
            self._app.selectFrame("stack", 3)

    def ordering_system(self, btn):
        while True:
            if btn == menu_list(1):
                Order_list.append(self, 1)
                print(Order_list)




# main routine
window = Gui()
window.start_app