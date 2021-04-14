# Imports
from appJar import gui
# Variables

# Functions
class Gui:
    """
    Class to set up and display gui
    Also manages the button events
    """
    def __init__(self):
        app = gui("Gui fast food menu", "1920x1080")
        self._app = app
        app.addLabel("title", colspan=2)
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")

        with app.frameStack("stack"):
            with app.frame("data_collection"):
                app.setLabel("title", "Fast food")
                app.setLabelBg("title", "white")
                app.setLabelFg("title", "grey")
                app.setImageLocation("images")
                app.addImage("images", "image.jpeg")
                app.addButtons(["burger", "fries", "melon", "drinks"], self.press)

            with app.frame("data_display"):
                app.addButtons(["coke", "pepsi", "water"], self.press)
        app.firstFrame("stack")  # Sets the first frame added to stack to display first
        app.go()
    def start_app(self):
        self._app.go()
    def press(self, btn):
        if btn == "burger":
            pass
        if btn == "fries":
            pass
        if btn == "melon":
            pass
        if btn == "coke":
            pass
        if btn == "pepsi":
            pass
        if btn == "water":
            pass
        if btn == "drinks":
            self._app.showTabbedFrameTab(self, "data_display")

window = Gui()
window.start_app
