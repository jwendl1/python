#Import the GUI module
from Tkinter import *
import tkMessageBox

#Create the class to hold our GUI
class App(object):
    def __init__(self):
        #Define the Tkinter window
        self.root = Tk()
        #Set window size
        self.root.minsize(width=300,height=50)
        self.root.maxsize(width=300,height=110)
        self.root.iconbitmap('myicon.ico')
        self.root.wm_title("Milliseconds Conversion")
        self.label = Label (self.root, text= "Enter value in Milliseconds.")
        self.label.pack()

        #Accept user input in the textbox
        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        #Set the button text to calculate seconds and pass it the command parameter
        self.buttontext = StringVar()
        self.buttontext.set("Calculate Seconds")
        Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()
        Button(self.root, text="Calculate Minutes", command=self.clicked2).pack()

        self.label = Label (self.root, text="")
        self.label.pack()

        self.root.mainloop()

        #Define the first button click function
    def clicked1(self):
        input = self.entrytext.get()
        #Set result to our mathematical equation for MS to Sec
        result = float(input)/1000
        self.label.configure(text="Seconds = " + str(result))
        #Return the result so we can pass it to the label
        return result

        #Define the second button click function
    def clicked2(self):
        #Set result to the mathematical equation for MS to Sec or Sec to Min.
        result = App.clicked1(self) / 60
        self.label.configure(text="Minutes = " + str(result))

    def button_click(self, e):
        pass

App()
