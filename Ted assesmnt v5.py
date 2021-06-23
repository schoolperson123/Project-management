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
        app = gui("Gui fast food menu", "750x750")
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
            elif btn == "Quit":
                app.stop()

        # the button system that collects the button pressed and sets the correct table
        def get(mainbtn):
            global order_total
            order_total = order_total + meal_array[mainbtn][1]
            Order_list.append(meal_array[mainbtn][0])
            app.setLabel("Price_display", 'Total cost: $%d' % order_total)
            app.setLabel("display", Order_list)

        # defines the order types and set the tables when the button is pushed
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

        # defines the final screen and displays the total price and ordered items
        def finalorder(self):
            app.selectFrame("stack", 3)
            app.hideLabel("display")
            dup = {i: Order_list.count(i) for i in Order_list}
            amount = []
            for food, number in dup.items():
                amount.append([food, number])
            app.addTable('final_order',
                         [['the final order', 'amount']
                          ], row=4)
            app.replaceAllTableRows('final_order', amount)
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
                app.addLabel("Price_display", 'Total cost USD: %d' % order_total)
                app.setLabelBg("Price_display", "green")
                app.setLabelBg("display", "grey")


        app.firstFrame("stack")  # Sets the first frame added to stack to display first

        app.go()
        self._app = app  # set the gui instance of _app to app


# main routine
window = Gui()