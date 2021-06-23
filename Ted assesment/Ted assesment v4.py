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
        app.addLabel("title")
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

            with app.frame("Table_frame"):
                app.addTable("food table", meal_array, action=get, actionButton="Get")
                app.addButton("Back", self.press)

            with app.frame("Food_Label", row=3):
                app.addLabel("LABEL", "")
                app.setLabelBg("LABEL", "white")
                app.addLabel("Price_Label", 'Price: %d' % price)
                app.setLabelBg("Price_Label", "white")

            with app.frame("Button_frame"):
                app.addButtons(["Drink", "Sides", "Burger", "Finish", "Quit"], self.press)

        app.firstFrame("stack")  # Sets the first frame added to stack to display first

        def press(btn):
            if btn == "Food":
                app.nextFrame("stack")
            elif btn == "Back":
                app.firstFrame("stack")
            elif btn == "Drinks":
                app.selectFrame("stack", 2)
            elif btn == "burger":
                app.selectFrame("stack", 3)

        def get(mainbtn):
            global price
            global limit
            limit += 1
            if limit < 10:
                price = price + meal_array[mainbtn][1]
                orders.append(meal_array[mainbtn][0])
                app.setLabel("LABEL", orders)
                app.setLabel("Price_Label", 'Price: $%d' % price)

        def Sides(self):
            meal_array.clear()
            for x in food_list:
                if x.get_food() == "Sides":
                    meal_array.append([x.get_name(), x.get_price(), x.get_food()])
            app.replaceAllTableRows("food table", meal_array, )

        def Drink1(self):
            meal_array.clear()
            for x in food_list:
                if x.get_food() == "Drink":
                    meal_array.append([x.get_name(), x.get_price(), x.get_food()])
            app.replaceAllTableRows("food table", meal_array, )


        def Burger(self):
            meal_array.clear()
            for x in food_list:
                if x.get_food() == "Burger":
                    meal_array.append([x.get_name(), x.get_price(), x.get_food()])
            app.replaceAllTableRows("food table", meal_array, )

        def endScreen(self):
            app.removeFrame("Table_frame")
            app.removeFrame("Button_frame")
            app.hideLabel("LABEL")
            app.addLabel("end", "Your order has been sent", row=0, column=0)
            app.setLabelBg("end", "white")
            orderString = "Your Order is:"
            counter = 0
            for x in orders:
                if counter % 3 == 0:
                    orderString += "\n " + "" + x
                else:
                    orderString += "  " + x
                counter += 1
            app.addLabel("food_order", orderString)
            app.setLabelBg("food_order", "white")

        app.addButton('Start', start, row=4, column=0)

        meal_array = [['Name', 'Price', 'Type', ]]
        app.go()
        self._app = app


    # main routine
window = Gui()
window.start_app