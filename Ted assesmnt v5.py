# Imports
from appJar import gui
import list # imports the order menu
# Variables
Order_list = [] # stores the ordered items
order_total = 0 # stores order total
total = 0 # stores how many orders have been made


# Functions
class Menu:

    def __init__(self, name, price, food):
        """
                A object to hold information of a person
                :param name: food name
                :param price: price of order
                :param food: food type
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



class Gui:
    def __init__(self):
        """
        Class to set up and display gui
        Also manages the button events
        """
        """
        Initialise the gui class in 2 columns including:
        - The top bar
        - the data collection frame
        - the data display window
        """
        app = gui("Gui fast food menu", "1750x920")
        app.addLabel("title")
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")

        def press(btn):
            if btn == "Food":
                app.selectFrame("stack", 1)
            elif btn == "Back":
                app.firstFrame("stack")
            elif btn == "sides":
                sides(self)
            elif btn == "burgers":
                burgers(self)
            elif btn == "drinks":
                drinks(self)
            elif btn == "Finish":
                finalorder(self)

        def get(mainbtn):
            global order_total
            global total
            total += 1
            if total < 20: # checks order total and sets it to a maximum of 20 ordered items
                order_total = order_total + meal_array[mainbtn][1]
                Order_list.append(meal_array[mainbtn][0])
                app.setLabel("display", Order_list)
                app.setLabel("Price_display", 'Total cost: $%d' % order_total)
            else:
                app.addLabel("max order")
                finalorder(self)

        def sides(self):
            meal_array.clear()
            for x in list.menu_list:
                if x.get_food_meal() == "sides":
                    meal_array.append([x.get_name(), x.get_price(), x.get_food_meal()])
            app.replaceAllTableRows("Menu display", meal_array, )
            app.selectFrame("stack", 2)

        def drinks(self):
            meal_array.clear()
            for x in list.menu_list:
                if x.get_food_meal() == "drinks":
                    meal_array.append([x.get_name(), x.get_price(), x.get_food_meal()])
            app.replaceAllTableRows("Menu display", meal_array, )
            app.selectFrame("stack", 2)

        def burgers(self):
            meal_array.clear()
            for x in list.menu_list:
                if x.get_food_meal() == "burgers":
                    meal_array.append([x.get_name(), x.get_price(), x.get_food_meal()])
            app.replaceAllTableRows("Menu display", meal_array, )
            app.selectFrame("stack", 2)

        def finalorder(self):
            app.selectFrame("stack", 3)
            app.hideLabel("display")
            app.addLabel("completed", "The order has been finalised", row=0, column=0)
            app.setLabelBg("completed", "grey")
            Theorder = "The order you have is:"
            counter = 0
            for x in Order_list:
                if counter % 1 == 0:
                    Theorder += "\n " + "" + x
                else:
                    Theorder += "  " + x
                counter += 1
            app.addLabel("final_order", Theorder)
            app.setLabelBg("final_order", "pink")

        meal_array = [['Name', 'Price', 'Type', ]]

        with app.frameStack("stack"):
            """
            Sets up the entire frame system 
            stores all frames in a stack
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
                app.addButtons(["Food", "drinks", "Finish"], press)
            with app.frame("food_frame"):
                app.addButtons(["sides", "burgers"], press)

            with app.frame("List_frame"):
                app.addTable("Menu display", meal_array, action=get, mainbtn="Get")
                app.addButton("Back", press)

            with app.frame("Food_display", row=3):
                app.addLabel("display", "")
                app.setLabelBg("display", "grey")
                app.addLabel("Price_display", 'Total cost USD: %d' % order_total)
                app.setLabelBg("Price_display", "green")

        app.firstFrame("stack") # Sets the first frame added to stack to display first

        app.go()
        self._app = app # set the gui instance of _app to app
# main routine
window = Gui()