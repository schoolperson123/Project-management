# Imports
from appJar import gui
# Variables

# Functions
class gui:
    """
    Class to set up and display gui
    Also manages the button events
    """
    def __init__(self):
        app = gui("Gui fast food menu", "1920x1080")
        self._app = app


    def press(button):
        if button == "start":
            app.hideFrame("main menu")
            app.showFrame("selection")
            pass


    app.setBg("white")
    app.setFont(17)

    with app.frame("main menu"):
        app.addLabel("title", "Fast food")
        app.setLabelBg("title", "white")
        app.setLabelFg("title", "grey")
        app.setImageLocation("images")
        app.addImage("images", "image.jpeg")
        app.addButtons(["start"], press)
    with app.frame("selection"):

        app.addButtons(["burger", "fries", "melon"], press)

    app.hideFrame()

    app.go()