# Ted assesment
# Michael Polianski
""""
Fast food gui ordering system
"""
# Imports
from appJar import gui
import list  # imports the order menu

# Variables
Order_list = []  # stores the ordered items
order_total = 0  # stores order total


# Functions
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
        app = gui("Gui fast food menu", "750x750") # sets up gui window
        app.addLabel("title")
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")
        app.setImageLocation("images") # sets image file location
        app.addImage("images", "image.jpeg")
        """
        Button system defined giving buttons
        specified roles within the program
        """
        def press(btn):
            if btn == "Food":
                app.setImage("images", "side_burger.jpeg")
                app.selectFrame("stack", 1)
            elif btn == "Back":
                app.setImage("images", "image.jpeg")
                app.firstFrame("stack")
            elif btn == "Sides":
                app.setImage("images", "sides.jpeg")
                Sides(self)
            elif btn == "Burgers":
                app.setImage("images", "burger.jpeg")
                Burgers(self)
            elif btn == "Drinks":
                app.setImage("images", "drinks.jpeg")
                Drinks(self)
            elif btn == "Finish":
                app.setImage("images", "order.jpeg")
                finalorder(self)
            elif btn == "Quit":
                app.stop()
            elif btn == "Reorder":
                app.setImage("images", "image.jpeg")
                app.firstFrame("stack")

        # the button system that collects the button pressed and sets the correct table
        def get(mainbtn):
            global order_total
            order_total = order_total + meal_array[mainbtn][1] # collects costs and adds them together
            Order_list.append(meal_array[mainbtn][0]) # adds ordered items to the list
            app.setLabel("Price_display", 'Total cost: $%d' % order_total)
            app.setLabel("display", Order_list)

        """
        system defines buttons types and sets specific data types to them
        allowing for different tables to be viewed and swapped.
        defines the order types and set the tables when the button is pushed
        """
        def Sides(self):
            meal_array.clear()
            for x in list.menu_list: # collects data from list
                if x.get_food_meal() == "Sides": # if specific button is pressed, collect that data type
                    meal_array.append([x.get_name(), x.get_price(), x.get_food_meal()]) # add specific data type to a list
            app.replaceAllTableRows("Menu_display", meal_array, deleteHeader=False) # replace table rows with specific data type
            app.selectFrame("stack", 2)

        def Drinks(self):
            meal_array.clear()
            for x in list.menu_list:
                if x.get_food_meal() == "Drinks":
                    meal_array.append([x.get_name(), x.get_price(), x.get_food_meal()])
            app.replaceAllTableRows("Menu_display", meal_array, deleteHeader=False)
            app.selectFrame("stack", 2)

        def Burgers(self):
            meal_array.clear()
            for x in list.menu_list:
                if x.get_food_meal() == "Burgers":
                    meal_array.append([x.get_name(), x.get_price(), x.get_food_meal()])
            app.replaceAllTableRows("Menu_display", meal_array, deleteHeader=False)
            app.selectFrame("stack", 2)

        # defines the final screen and displays the total price and ordered items
        def finalorder(self):
            app.selectFrame("stack", 3)
            app.hideLabel("display")
            if order_total <1: # checks if anything has been ordered
                app.setImage("images", "Reorder.jpeg")
                app.selectFrame("stack", 4)
            else:
                duplicate = {i: Order_list.count(i) for i in Order_list} # checks for duplicate orders and counts them
                amount = []
                for food, number in duplicate.items(): # sets values for duplicate items
                    amount.append([food, number])
                app.addTable('final_order',
                             [["Order", "Quantity"]
                              ], row=4)

                app.addTableRows('final_order', amount)
                app.setLabel('title', "your order has been sent")
                app.addButton('Quit', press, row=7)

        meal_array = [
            ['Name', 'Price', 'Type', ]
        ]

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
                app.addButtons(["Food", "Drinks", "Finish"], press)

            with app.frame("food_frame"):
                app.addButtons(["Sides", "Burgers"], press)

            with app.frame("List_frame"):
                app.addTable("Menu_display", meal_array, action=get)
                app.addButton("Back", press)


            with app.frame("Food_display", row=3):
                app.addLabel("display", "")
                app.addLabel("Price_display", 'Total cost USD: %d' % order_total)
                app.setLabelBg("Price_display", "green")
                app.setLabelBg("display", "grey")

            with app.frame("Order_false"):
                app.addLabel("order_false_prompt", "You have not ordered anything")
                app.setLabelBg("order_false_prompt", "red")
                app.addButton("Reorder", press, row=5)

        app.firstFrame("stack")  # Sets the first frame added to stack to display first

        app.go()
        self._app = app  # set the gui instance of _app to app


# main routine
window = Gui()