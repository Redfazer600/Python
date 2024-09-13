##############################
# Alexander Bevan
# Programming Coursework 2 - Frontend
# UP2198095
# Due date: 11/03/24 16:00 GMT
##############################

# Imports
from backend import *
from tkinter import *

# Set up home function
def setUpHome():
    home = SmartHome()
    count = 0

    while count < 5:
        choice = input('Would you like to add a plug or a doorbell?')
        if choice.lower() == 'plug':
            while True:  # Validation for the consumption input.
                consumptionRate = input('Please enter the consumption rate of the plug')
                if consumptionRate.isnumeric():  # Checks to see if there are only numbers
                    consumptionRate = int(consumptionRate)  # Converts to an int
                    if 0 <= consumptionRate <= 150:  # checks to see if in range
                        home.addDevice(SmartPlug(consumptionRate))
                        count += 1
                        break  # Adds and break validation loop after increasing count.
                    else:
                        print('ruh roh Shaggy, the user has entered a number out of range!\n'
                              'Yeah he has Scooby! He needs to enter a whole number between 0 and 150\n')
                else:
                    print('Ahoy there me-hearty, you be speaking foreign! '
                          'First mate should have told you to use integers!')

        elif choice.lower() == 'doorbell':
            home.addDevice(SmartDoorBell())
            count += 1
        else:
            print('Hey! The user has given an invalid input in lego city! '
                  'Please enter either the word plug or doorbell for adding a SmartPlug or SmartDoorBell '
                  'and build the lego prison for when they do it again!')
    return home

# Smart home system class
class SmartHomeSystem:
    def __init__(self, smartHome):

        # Defining instance variables
        self.smartHome = smartHome
        self.widgetRows = []
        self.labelVars = []

        # Making the window & basic layout frames
        self.win = Tk()
        self.win.title("Smart Control Hub")
        self.topFrame = Frame(self.win)
        self.bottomFrame = Frame(self.win)
        self.topFrame.grid(row=0, column=0, padx=10, pady=10)
        self.bottomFrame.grid(row=1, column=0, padx=10, pady=10)

    # Method that builds the initial GUI
    def createWidgets(self):

        # Create the widgets for the top frame
        topWidgets = []
        onAllBtn = Button(self.topFrame, text='Turn on all', command=lambda: [self.smartHome.turnOnAll(), self.updateLabels()])
        offAllBtn = Button(self.topFrame, text='Turn off all', command=lambda: [self.smartHome.turnOffAll(), self.updateLabels()])
        addDeviceBtn = Button(self.topFrame, text='Add a Device', command=self.addGUI)

        # Append the widgets into the widget row
        topWidgets.append(onAllBtn)
        topWidgets.append(offAllBtn)
        topWidgets.append(addDeviceBtn)

        # Draw widgets inside the topWidgets list - enumerate gets the list index and value
        for i, widget in enumerate(topWidgets):
            widget.grid(row=0, column=i, padx=10)

        # for each initial device, create widgets at row i with description of device type for each label text var
        for deviceNumber, deviceType in enumerate(self.smartHome.devices):
            self.createWidgetRow(deviceNumber, deviceType)

    # Method that creates a row of widgets, appends to widgetRows list and draws in the window
    def createWidgetRow(self, deviceNo, deviceType):

        # Make list for the widgets inside the row
        widgetRow = []

        # Make label string variables for dynamic update of text without redrawing widgets every time
        labelText = StringVar()
        labelText.set(deviceType)
        self.labelVars.append(labelText)    # appended here so the label doesn't error 'index out of range'

        # Make the widgets
        deviceLabel = Label(self.bottomFrame, textvariable=self.labelVars[deviceNo])
        toggleDeviceBtn = Button(self.bottomFrame, text="Toggle Device",
                                 command=lambda: [self.smartHome.toggleSwitch(deviceNo), self.updateLabels()])
        editDeviceBtn = Button(self.bottomFrame, text="Edit Device", command=lambda: [self.editCommand(deviceNo), self.updateLabels()])
        removeDeviceBtn = Button(self.bottomFrame, text="Remove Device", command=lambda: [self.deleteCommand(deviceNo), print(self.smartHome)])

        # Append the label text and widgets to appropriate lists
        widgetRow.append(deviceLabel)
        widgetRow.append(toggleDeviceBtn)
        widgetRow.append(editDeviceBtn)
        widgetRow.append(removeDeviceBtn)

        # Draw each widget inside the widget row
        for i, widget in enumerate(widgetRow):
            widget.grid(row=deviceNo, column=i, padx=5, pady=5)

        # Append the widget row to self.widgetRows list to keep track of rows and allow for label text update
        self.widgetRows.append(widgetRow)

    # Method for the add device button - when clicked brings up a separate GUI to add either a plug or doorbell
    def addGUI(self):

        # Make the toplevel
        addWindow = Toplevel(self.win)
        addWindow.title('Device Attributes Edit Window')

        # Define tkinter variables - before checkboxes are made so all works correctly
        plugBoxValue = BooleanVar()    # Checkboxes can only be checked or not checked
        doorbellBoxValue = BooleanVar()
        scaleValue = IntVar()

        # Create widgets
        addBtn = Button(addWindow, text='Add Device', command=lambda: [self.addCommand(plugBoxValue.get(), doorbellBoxValue.get(), scaleValue.get()), addWindow.destroy()])
        plugBox = Checkbutton(addWindow, text="Smart Plug", variable=plugBoxValue, )
        doorbellBox = Checkbutton(addWindow, text="Smart DoorBell", variable=doorbellBoxValue, )
        instruction = Label(addWindow, text='Please select either plug or doorbell.\n '
                                            'If plug is selected set the consumption rate using the below scale then press add')
        crScale = Scale(addWindow, from_=0, to=150, orient=HORIZONTAL, variable=scaleValue)

        # Draw widgets
        addBtn.grid(row=0, column=0, padx=10, pady=10,)
        plugBox.grid(row=0, column=1, padx=10, pady=10,)
        doorbellBox.grid(row=0, column=2, padx=10, pady=10,)
        instruction.grid(row=1, column=1,)
        crScale.grid(row=2, column=1, pady=10,)

    # Method for the add button inside the addGUI method
    def addCommand(self, plugChecked, bellChecked, scale):

        # Checkbox logic to check what device to add - only creates a device if a single box is selected
        if plugChecked and not bellChecked:
            self.smartHome.addDevice(SmartPlug(scale))

        elif bellChecked and not plugChecked:
            self.smartHome.addDevice(SmartDoorBell())

        self.createWidgetRow(len(self.smartHome.devices)-1, self.smartHome.devices[len(self.smartHome.devices)-1])

    # Method for the edit device button - when clicked allows for editing of all device attributes
    def editCommand(self, index):
        # Create the edit window using toplevel
        editWindow = Toplevel(self.win)
        editWindow.title('Device Attributes Edit Window')

        # Create all required widgets
        confirmBtn = Button(editWindow, text='Finish Editing', command=editWindow.destroy)
        toggleDeviceBtn = Button(editWindow, text='Toggle Device',
                                 command=lambda: [self.smartHome.toggleSwitch(index), self.updateLabels()])
        conRateScale = Scale(editWindow, from_=0, to=150, orient=HORIZONTAL, command=lambda scaleValue=Scale.get: [self.smartHome.devices[index].setConsumptionRate(scaleValue), self.updateLabels()])
        sleepOnBtn = Button(editWindow, text='Sleep mode on', command=lambda: [self.smartHome.devices[index].setSleepMode('on'), self.updateLabels()])
        sleepOffBtn = Button(editWindow, text='Sleep mode off', command=lambda: [self.smartHome.devices[index].setSleepMode('off'), self.updateLabels()])

        # Checks device type and draws window accordingly
        if isinstance(self.smartHome.devices[index], SmartPlug):
            confirmBtn.grid(row=0, column=0, padx=10, pady=10)
            toggleDeviceBtn.grid(row=0, column=1, padx=10, pady=10)
            conRateScale.grid(row=1, column=0, padx=10, pady=10)

        elif isinstance(self.smartHome.devices[index], SmartDoorBell):
            confirmBtn.grid(row=0, column=0, padx=10, pady=10)
            toggleDeviceBtn.grid(row=0, column=1, padx=10, pady=10)
            sleepOnBtn.grid(row=1, column=0, padx=10, pady=10)
            sleepOffBtn.grid(row=1, column=1, padx=10, pady=10)

    # Method for the remove device button - when clicked removes device from relevant lists
    def deleteCommand(self, index):
        # Delete from smart home
        self.smartHome.removeDeviceAt(index)

        # un-draw device widgets from window and delete the widget row associated with deleted device
        rowToRemove = self.widgetRows[index]
        for widget in rowToRemove:
            widget.grid_forget()
        # del rowToRemove   # This deletes from the list but stops un-drawing widgets from the 3rd device, unsure why?!
        del self.widgetRows[index]      # deleting this way works flawlessly every time

        # Remove associated text variable for the deleted label
        del self.labelVars[index]

        # Update all other device buttons with new indexes to prevent 'index out of range' errors
        count = 0   # Yeah, it took me way too long to realise this needs initializing here instead of 2 lines below...
        for widgetRow in self.widgetRows:
            toggleButton = widgetRow[1]
            editButton = widgetRow[2]
            removeButton = widgetRow[3]
            toggleButton.config(command=lambda deviceNo=count: [self.smartHome.toggleSwitch(deviceNo), self.updateLabels()])
            editButton.config(command=lambda deviceNo=count: [self.editCommand(deviceNo), self.updateLabels(), print(self.smartHome)])
            removeButton.config(command=lambda deviceNo=count: [self.deleteCommand(deviceNo), print(self.smartHome)])
            count += 1

    # Method to update the device labels via the tkinter text variable
    def updateLabels(self):
        for i, deviceType in enumerate(self.smartHome.devices):
            self.labelVars[i].set(deviceType)

    # Making the run method for main code body.
    def run(self):
        self.createWidgets()
        self.win.mainloop()


# Defining the main function
def main():
    testHouse = setUpHome()
    gui = SmartHomeSystem(testHouse)
    gui.run()


# Calling main to run
main()


# In the delete command could someone please tell me why I can't delete row to remove however the code works when just
# the value of the row to remove variable is deleted, I have extensively researched and can't find an answer!
