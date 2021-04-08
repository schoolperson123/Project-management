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


    def press(button):
        if button == "start":
            pass

    app = gui("Gui fast food menu", "1920x1080")
    app.setBg("white")
    app.setFont(17)

    with app.frame("main menu"):
        app.addLabel("title", "Fast food")
        app.setLabelBg("title", "white")
        app.setLabelFg("title", "grey")
        app.setImageLocation("images")
        app.addImage("images", "image.jpeg")
        app.setBgImage(self, "iamge.jpeg")
        app.addButtons(["start"], press)


app.go()