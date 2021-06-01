# Imports
from appJar import gui
# Variables
menu_list = [
    {"id": 1, "name": "cheese burger", "price": 34, "$": "USD"},
    {"id": 2, "name": "XL cheese burger", "price": 23, "$": "USD"},
    {"id": 3, "name": "bacon sandwich", "price": 65, "$": "USD"},
    {"id": 4, "name": "Pepsi", "price": 66, "$": "USD"},
    {"id": 5, "name": "Coke", "price": 21, "$": "USD"}]
Order_list = []
def changed(props):
    print("Changed", props)
toppings={"Cheese":False, "Tomato":False, "Bacon":False,
            "Corn":False, "Mushroom":False}

# Functions
class Gui:
    """
    Class to set up and display gui
    Also manages the button events
    """
    def __init__(self):
        """
                Initialise the gui class in 2 columns including:
                - The top bar
                - the data collection frame
                - the data display window
        """
        app = gui("Gui fast food menu", "1750x920")
        self._app = app
        app.addLabel("title", colspan=2)
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")
        for menu in menu_list:
            app.addLabel("f1", menu.get('name'), menu.get('price'), menu.get('$'))
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
                app.startToggleFrame("Toppings")
                app.addProperties("Toppings", toppings)
                app.setPropertiesChangeFunction("Toppings", changed)
                app.stopToggleFrame()

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


# main routine
window = Gui()
window.start_app