# Imports
from appJar import gui
# Variables
order = []
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

        app = gui("Gui fast food menu", "1920x1080")
        self._app = app
        app.addLabel("title", colspan=2)
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")

        with app.frameStack("stack"):
            """
            stacks the frames and giving the ability to switch through
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
                app.addButtons(["burger", "fries", "melon", "Back"], self.press)
                app.setBg("lightBlue")
                app.setFont(20)
                app.startToggleFrame("Toppings")
                app.addProperties("Toppings", toppings)
                app.setPropertiesChangeFunction("Toppings", changed)
                app.stopToggleFrame()
            with app.frame("data_display"):
                """
                this frame controls the drinks sections
                """
                app.addButtons(["coke", "pepsi", "water"], self.press)

        app.firstFrame("stack")  # Sets the first frame added to stack to display first
        app.go()
    def start_app(self):
        self._app.go()
    def press(self, btn):
        if btn == "Food":
            self._app.nextFrame("stack")
            if btn != "Food":
                order.append("")
                pass
        if btn == "Back":
            self._app.prevFrame("stack")
        if btn == "drinks":
            self._app.nextFrame("stack")

# main routine
window = Gui()
window.start_app