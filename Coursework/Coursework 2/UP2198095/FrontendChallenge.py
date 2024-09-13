##############################
# Alexander Bevan
# Programming Coursework 2 - Frontend Challenge
# UP2198095
# Due date: 11/03/24 16:00 GMT
##############################


# Imports
from backendChallenge import *
from tkinter import *
import tkinter.font
import tkinter.colorchooser as colorchooser
from datetime import datetime, timedelta

# Set up home function
def setUpHome():
    home = SmartHome()
    count = 0
    incorrect = 0
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
            incorrect += 1
            if incorrect >= 2:
                print(
                    'Hey, the lego prison is complete! You have now been locked up for your invalid inputs, you were warned!')
            else:
                print('\nHey! The user has given an invalid input in lego city!\n'
                      'Please enter either the word plug or doorbell for adding a SmartPlug or SmartDoorBell\n'
                      'and build the lego prison for when they do it again!')
    return home


# Smart home system class
class SmartHomeSystem:
    def __init__(self, smartHome):

        # Defining instance variables
        self.smartHome = smartHome
        self.widgetRows = []
        self.labelVars = []
        self.topWidgets = []
        self.totalRowCount = 0

        # These are the new instance vars for the accessibility themes
        self.lightMode = True
        self.darkMode = False
        self.customTheme = False
        self.customBgCol = '#000000'
        self.customFgCol = '#FFFFFF'

        # Making the window & basic layout frames
        self.win = Tk()
        self.win.title("Smart Control Hub")
        self.topFrame = Frame(self.win)
        self.bottomFrame = Frame(self.win)
        self.topFrame.grid(row=0, column=0, padx=10, pady=10)
        self.bottomFrame.grid(row=1, column=0, padx=10, pady=10)

        # Making window properties for the accessibility of the window
        self.fontSize = tkinter.font.Font(size=10)
        self.win.option_add("*Font", self.fontSize)

        # Defining the photo image tkinter variables for the custom visualisation challenge
        self.turnOnAllIcon = PhotoImage(file='turnonall.png').subsample(15)
        self.turnOffAllIcon = PhotoImage(file='turnoffall.png').subsample(15)
        self.addIcon = PhotoImage(file='add.png').subsample(15)
        self.accessibilityIcon = PhotoImage(file='accessibility.png').subsample(15)
        self.toggleIcon = PhotoImage(file='toggle.png').subsample(15)
        self.editIcon = PhotoImage(file='edit.png').subsample(15)
        self.deleteIcon = PhotoImage(file='eradicateFromExistance.png').subsample(15)
        self.plugIcon = PhotoImage(file='plug.png').subsample(15)
        self.doorbellIcon = PhotoImage(file='doorbell.png').subsample(15)
        self.customColourIcon = PhotoImage(file='color-picker.png').subsample(15)
        self.lightModeIcon = PhotoImage(file='lightmode.png').subsample(15)
        self.darkModeIcon = PhotoImage(file='darkmode.png').subsample(15)
        self.confirmIcon = PhotoImage(file='confirm.png').subsample(15)
        self.sleepOnIcon = PhotoImage(file='sleepon.png').subsample(15)
        self.sleepOffIcon = PhotoImage(file='sleepoff.png').subsample(15)
        self.scheduleIcon = PhotoImage(file='schedule.png').subsample(15)

        # Defining clock specific attributes for the device scheduler
        self.clockTime = datetime.now().replace(minute=0, second=0, microsecond=0)
        self.timeLabel = Label(self.win, text=self.clockTime.strftime("%H:%M"), font=('Arial', 20))

    # Method that builds the initial GUI
    def createWidgets(self):

        # Create the widgets for the top frame
        onAllBtn = Button(self.topFrame, text='Turn on all', image=self.turnOnAllIcon, compound='bottom',
                          command=lambda: [self.smartHome.turnOnAll(), self.updateLabels()])

        offAllBtn = Button(self.topFrame, text='Turn off all', image=self.turnOffAllIcon, compound='bottom',
                           command=lambda: [self.smartHome.turnOffAll(), self.updateLabels()])
        addDeviceBtn = Button(self.topFrame, text='Add a Device', command=self.addGUI,
                              image=self.addIcon, compound='bottom')

        accessibilityBtn = Button(self.topFrame, text='Accessibility', command=self.accessGUI,
                                  image=self.accessibilityIcon, compound='bottom')

        scheduleBtn = Button(self.win, text='Schedule Devices', image=self.scheduleIcon, compound='bottom',
                             command=self.scheduleGUI)

        # Append the widgets into the widget row
        self.topWidgets.append(onAllBtn)
        self.topWidgets.append(offAllBtn)
        self.topWidgets.append(addDeviceBtn)
        self.topWidgets.append(accessibilityBtn)
        self.topWidgets.append(self.timeLabel)
        self.topWidgets.append(scheduleBtn)

        # Draw widgets inside the topWidgets list - enumerate gets the list index and value
        for i, widget in enumerate(self.topWidgets):
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
        self.labelVars.append(labelText)  # appended here so the label doesn't error 'index out of range'

        # Make the widgets
        if isinstance(deviceType, SmartPlug):
            deviceLabel = Label(self.bottomFrame, textvariable=self.labelVars[deviceNo], image=self.plugIcon, compound='bottom')
        elif isinstance(deviceType, SmartDoorBell):
            deviceLabel = Label(self.bottomFrame, textvariable=self.labelVars[deviceNo], image=self.doorbellIcon, compound='bottom')
        else:
            deviceLabel = Label(self.bottomFrame, textvariable=self.labelVars[deviceNo])

        toggleDeviceBtn = Button(self.bottomFrame, text="Toggle Device", image=self.toggleIcon, compound='bottom',
                                 command=lambda: [self.smartHome.toggleSwitch(deviceNo), self.updateLabels()])

        editDeviceBtn = Button(self.bottomFrame, text="Edit Device", image=self.editIcon, compound='bottom',
                               command=lambda: [self.editGUI(deviceNo), self.updateLabels()])

        removeDeviceBtn = Button(self.bottomFrame, text="Remove Device", image=self.deleteIcon, compound='bottom',
                                 command=lambda: self.deleteCommand(deviceNo))

        # Append the label text and widgets to appropriate lists
        widgetRow.append(deviceLabel)
        widgetRow.append(toggleDeviceBtn)
        widgetRow.append(editDeviceBtn)
        widgetRow.append(removeDeviceBtn)

        # Draw each widget inside the widget row
        for i, widget in enumerate(widgetRow):
            widget.grid(row=self.totalRowCount, column=i, padx=5, pady=5)

        # Append the widget row to self.widgetRows list to keep track of rows and allow for label text update
        self.widgetRows.append(widgetRow)

        # Update totalRowCount to ensure that next function call, the widgets draw on the next line
        self.totalRowCount += 1

    # Method for the add device button - when clicked brings up a separate GUI to add either a plug or doorbell
    def addGUI(self):

        # Make the toplevel
        addWindow = Toplevel(self.win)
        addWindow.title('Device Attributes Edit Window')

        # Define tkinter variables - before checkboxes are made so all works correctly
        plugBoxValue = BooleanVar()  # Checkboxes can only be checked or not checked
        doorbellBoxValue = BooleanVar()
        scaleValue = IntVar()

        # Create widgets
        addBtn = Button(addWindow, text='Add Device', image=self.addIcon, compound='bottom',
                        command=lambda: [self.addCommand(plugBoxValue.get(), doorbellBoxValue.get(), scaleValue.get()),
                                         addWindow.destroy()])
        plugBox = Checkbutton(addWindow, text="Smart Plug", variable=plugBoxValue, )
        doorbellBox = Checkbutton(addWindow, text="Smart DoorBell", variable=doorbellBoxValue, )
        instruction = Label(addWindow, text='Please select either plug or doorbell.\n '
                                            'If plug is selected set the consumption rate using the below scale then press add')
        crScale = Scale(addWindow, from_=0, to=150, orient=HORIZONTAL, variable=scaleValue)

        # Append to a widget list
        widgetList = [addBtn, plugBox, doorbellBox, instruction]

        # Draw widgets
        addBtn.grid(row=0, column=0, padx=10, pady=10, )
        plugBox.grid(row=0, column=1, padx=10, pady=10, )
        doorbellBox.grid(row=0, column=2, padx=10, pady=10, )
        instruction.grid(row=1, column=1, )
        crScale.grid(row=2, column=1, pady=10,)

        # Logic for checking the accessibility theme - don't need to check if light mode because will be light as default
        if self.darkMode:
            addWindow.configure(bg="#333333")
            for widget in widgetList:
                if isinstance(widget, Checkbutton):
                    widget.configure(foreground="#000000", background="#555555")
                else:
                    widget.configure(foreground="#FFFFFF", background="#555555")
        elif self.customTheme:
            addWindow.configure(bg=self.customBgCol)
            for widget in widgetList:
                widget.configure(foreground=self.customFgCol, background=self.customBgCol)

    # Method for the add button inside the addGUI method
    def addCommand(self, plugChecked, bellChecked, scale):

        # Checkbox logic to check what device to add - only creates a device if a single box is selected
        if plugChecked and not bellChecked:
            self.smartHome.addDevice(SmartPlug(scale))
            self.createWidgetRow(len(self.smartHome.devices) - 1,
                                 self.smartHome.devices[len(self.smartHome.devices) - 1])

        elif bellChecked and not plugChecked:
            self.smartHome.addDevice(SmartDoorBell())
            self.createWidgetRow(len(self.smartHome.devices) - 1,
                                 self.smartHome.devices[len(self.smartHome.devices) - 1])

        # Putting the create widget row outside  the commands means that even if no device is created (both or neither
        # boxes are selected) means a widget row is made regardless which then causes identical last device widgets
        # to draw over the top of each other on the bottom row causing errors. This is why there is 'repetitive' code

        # Theme logic for if the accessibility options have been used - Re sets window theme after widgets are made
        if self.darkMode:
            self.setWindowDarkTheme()
        elif self.lightMode:
            self.setWindowLightTheme()
        elif self.customTheme:
            self.setWindowCustomTheme()

    # Method for the edit device button - when clicked allows for editing of all device attributes
    def editGUI(self, index):
        # Create the edit window using toplevel
        editWindow = Toplevel(self.win)
        editWindow.title('Device Attributes Edit Window')

        # Create all required widgets
        confirmBtn = Button(editWindow, text='Finish Editing', image=self.confirmIcon, compound='bottom',
                            command=editWindow.destroy)

        toggleDeviceBtn = Button(editWindow, text='Toggle Device', image=self.toggleIcon, compound='bottom',
                                 command=lambda: [self.smartHome.toggleSwitch(index), self.updateLabels()])

        conRateScale = Scale(editWindow, from_=0, to=150, orient=HORIZONTAL, command=lambda scaleValue=Scale.get: [
            self.smartHome.devices[index].setConsumptionRate(scaleValue), self.updateLabels()])

        sleepOnBtn = Button(editWindow, text='Sleep mode on', image=self.sleepOnIcon, compound='bottom',
                            command=lambda: [self.smartHome.devices[index].setSleepMode('on'), self.updateLabels()])

        sleepOffBtn = Button(editWindow, text='Sleep mode off', image=self.sleepOffIcon, compound='bottom',
                             command=lambda: [self.smartHome.devices[index].setSleepMode('off'), self.updateLabels()])

        # Append all to a widget list
        widgetList = [confirmBtn, toggleDeviceBtn, conRateScale, sleepOnBtn, sleepOffBtn]

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

            # Logic for checking the accessibility theme
            if self.darkMode:
                editWindow.configure(bg="#333333")
                for widget in widgetList:
                    widget.configure(foreground="#FFFFFF", background="#555555")
            elif self.customTheme:
                editWindow.configure(bg=self.customBgCol)
                for widget in widgetList:
                    widget.configure(foreground=self.customFgCol, background=self.customBgCol)

    # Method for the remove device button - when clicked removes device from relevant lists
    def deleteCommand(self, index):
        # Delete from smart home
        self.smartHome.removeDeviceAt(index)

        # un-draw device widgets from window and delete the widget row associated with deleted device
        rowToRemove = self.widgetRows[index]
        for widget in rowToRemove:
            widget.grid_forget()
        # del rowToRemove   # This deletes from the list but stops un-drawing widgets from the 3rd device, unsure why?!
        del self.widgetRows[index]  # deleting this way works flawlessly every time

        # Remove associated text variable for the deleted label
        del self.labelVars[index]

        # Update all other device buttons with new indexes to prevent 'index out of range' errors
        count = 0  # Yeah, it took me way too long to realise this needs initializing here instead of 2 lines below...
        for widgetRow in self.widgetRows:
            toggleButton = widgetRow[1]
            editButton = widgetRow[2]
            removeButton = widgetRow[3]
            toggleButton.config(
                command=lambda deviceNo=count: [self.smartHome.toggleSwitch(deviceNo), self.updateLabels()])
            editButton.config(command=lambda deviceNo=count: [self.editGUI(deviceNo), self.updateLabels()])
            removeButton.config(command=lambda deviceNo=count: self.deleteCommand(deviceNo))
            count += 1

    # Method to update the device labels via the tkinter text variable
    def updateLabels(self):
        for i, deviceType in enumerate(self.smartHome.devices):
            self.labelVars[i].set(deviceType)

    # Method to update the label that contains the clock.
    def updateClock(self):

        self.clockTime += timedelta(hours=1)
        self.timeLabel.config(text=self.clockTime.strftime("%H:%M"))
        self.win.after(3000, self.updateClock)

    # Making a device scheduling GUI
    def scheduleGUI(self):

        # Make the toplevel and frames
        schedulingWindow = Toplevel(self.win)
        schedulingWindow.title('Scheduling Window')

        # Making properties for the optionMenu box
        properties = ['Power On Device', 'Power Off Device']
        selectedProperty = StringVar()
        selectedProperty.set(properties[0])

        # Make the widgets & attributes
        scheduleDeviceBtn = Button(schedulingWindow, text='Schedule Device')
        deviceNumber = Spinbox(schedulingWindow, from_=1, to=len(self.smartHome.devices))
        deviceNumberLabel = Label(schedulingWindow, text='Select device number:')
        schedulePropertyMenu = OptionMenu(schedulingWindow, selectedProperty, *properties)
        propertyLabel = Label(schedulingWindow, text='Select Action:')
        scheduleWhenBox = Entry(schedulingWindow)
        whenLabel = Label(schedulingWindow, text='Select Time To Schedule:\n(integer in range 0-24)')
        deScheduleDeviceBtn = Button(schedulingWindow, text='De-Schedule Device')
        confirmBtn = Button(schedulingWindow, text='Finish Scheduling', command=schedulingWindow.destroy)

        # Drawing all the widgets
        confirmBtn.grid(row=0, column=0, padx=10, pady=10)
        scheduleDeviceBtn.grid(row=0, column=1, padx=10, pady=10)
        deScheduleDeviceBtn.grid(row=0, column=2, padx=10, pady=10)
        deviceNumberLabel.grid(row=1, column=0, padx=10, pady=10)
        deviceNumber.grid(row=2, column=0, padx=10, pady=10)
        propertyLabel.grid(row=1, column=1, padx=10, pady=10)
        schedulePropertyMenu.grid(row=2, column=1, padx=10, pady=10)
        whenLabel.grid(row=1, column=2, padx=10, pady=10)
        scheduleWhenBox.grid(row=2, column=2, padx=10, pady=10)

    # Making an accessibility method
    def accessGUI(self):

        # Make the toplevel
        accessWindow = Toplevel(self.win)
        accessWindow.title('Accessibility Window')

        # Make the widgets
        changeSizeBtn = Button(accessWindow, text='Change Font Size', command=lambda: self.setTextSize(inputBox.get()))
        inputBox = Entry(accessWindow)
        confirmBtn = Button(accessWindow, text='Confirm changes', image=self.confirmIcon, compound='bottom',
                            command=lambda: accessWindow.destroy())
        lightModeBtn = Button(accessWindow, text='Light Mode', image=self.lightModeIcon, compound='bottom',
                              command=self.setWindowLightTheme)
        darkModeBtn = Button(accessWindow, text='Dark Mode', image=self.darkModeIcon, compound='bottom',
                             command=self.setWindowDarkTheme)
        themeBtn = Button(accessWindow, text='Customize Theme', image=self.customColourIcon, compound='bottom',
                          command=self.customizeGUI)

        # Make widget list
        widgetList = [changeSizeBtn, inputBox, confirmBtn, lightModeBtn, darkModeBtn, themeBtn]

        # Draw the widgets
        confirmBtn.grid(row=0, column=0, pady=10, padx=10)
        themeBtn.grid(row=0, column=1, pady=10, padx=10)
        changeSizeBtn.grid(row=1, column=0, pady=10, padx=10)
        inputBox.grid(row=1, column=1, pady=10, padx=10)
        lightModeBtn.grid(row=2, column=0, pady=10, padx=10)
        darkModeBtn.grid(row=2, column=1, pady=10, padx=10)

        # Logic for checking the accessibility theme
        if self.darkMode:
            accessWindow.configure(bg="#333333")
            for widget in widgetList:
                widget.configure(foreground="#FFFFFF", background="#555555")
        elif self.customTheme:
            accessWindow.configure(bg=self.customBgCol)
            for widget in widgetList:
                widget.configure(foreground=self.customFgCol, background=self.customBgCol)

    # Making a customization method
    def customizeGUI(self):
        # Draw window
        customizeWindow = Toplevel(self.win)
        customizeWindow.title('Customize Window')

        # Make Widgets & associated vars
        pickFrontColBtn = Button(customizeWindow, text="Pick custom\nforeground colour", command=lambda: [self.pickFgColour(), selected.set(f'foreground colour: {self.customFgCol}\nBackground colour: {self.customBgCol}')])
        pickBackColBtn = Button(customizeWindow, text="Pick custom\nbackground colour", command=lambda: [self.pickBgColour(), selected.set(f'foreground colour: {self.customFgCol}\nBackground colour: {self.customBgCol}')])
        confirmBtn = Button(customizeWindow, text='Confirm Changes', image=self.confirmIcon, compound='bottom',
                            command=lambda: [customizeWindow.destroy(), self.setWindowCustomTheme()])
        selected = StringVar()
        selected.set(f'foreground colour: {self.customFgCol}\nBackground colour: {self.customBgCol}')
        selectedLabel = Label(customizeWindow, textvariable=selected)

        # Make widget list
        widgetList = [pickFrontColBtn, pickBackColBtn, confirmBtn, selectedLabel]

        # Draw Widgets
        pickFrontColBtn.grid(row=0, column=0, pady=10, padx=10)
        pickBackColBtn.grid(row=0, column=1, pady=10, padx=10)
        confirmBtn.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        selectedLabel.grid(row=1, column=1, padx=10, pady=10)

        # Logic for checking the accessibility theme
        if self.darkMode:
            customizeWindow.configure(bg="#333333")
            for widget in widgetList:
                widget.configure(foreground="#FFFFFF", background="#555555")
        elif self.customTheme:
            customizeWindow.configure(bg=self.customBgCol)
            for widget in widgetList:
                widget.configure(foreground=self.customFgCol, background=self.customBgCol)

    # Method to configure the font size for the accessibility settings.
    def setTextSize(self, fontSize):
        if fontSize.isnumeric():  # Does nothing if the font size is anything but a positive integer
            fontSize = int(fontSize)
            self.fontSize.config(size=fontSize)

    # Method to set the main window to the dark theme
    def setWindowDarkTheme(self):

        # Toggle theme variables
        self.darkMode = True
        self.lightMode = False
        self.customTheme = False

        # Sets the background of the main window as well as the 2 frames
        self.win.configure(bg="#333333")
        self.topFrame.configure(bg="#333333")
        self.bottomFrame.configure(bg="#333333")

        # Sets the background and foreground of each widget in the top frame
        for widget in self.topWidgets:
            widget.configure(foreground="#FFFFFF", background="#555555")

        # Sets the background and foreground of each widget in each widget row depending on the type of widget
        for row, list in enumerate(self.widgetRows):
            for widget in self.widgetRows[row]:
                if isinstance(widget, Label):
                    widget.configure(foreground="#FFFFFF", background="#333333")
                elif isinstance(widget, Button):
                    widget.configure(foreground="#FFFFFF", background="#555555")

        # Updates the window with the current colour properties
        self.win.update()

    # Method to set the main window to the light theme
    def setWindowLightTheme(self):
        # Toggle theme variables
        self.darkMode = False
        self.lightMode = True
        self.customTheme = False

        # Sets the background of the main window as well as the 2 frames
        self.win.configure(bg="#EEEEEE")
        self.topFrame.configure(bg="#EEEEEE")
        self.bottomFrame.configure(bg="#EEEEEE")

        # Sets the background and foreground of each widget in the top frame
        for widget in self.topWidgets:
            widget.configure(foreground="#333333", background="#EEEEEE")

        # Sets the background and foreground of each widget in each widget row
        for row, list in enumerate(self.widgetRows):
            for widget in self.widgetRows[row]:
                widget.configure(foreground="#333333", background="#EEEEEE")

        self.win.update()

    # Method to set the main window to a custom theme using the foreground and background custom picked colours
    def setWindowCustomTheme(self):

        # Toggle theme variables
        self.darkMode = False
        self.lightMode = False
        self.customTheme = True

        # Sets the background of the main window as well as the 2 frames
        self.win.configure(bg=self.customBgCol)
        self.topFrame.configure(bg=self.customBgCol)
        self.bottomFrame.configure(bg=self.customBgCol)

        # Sets the background and foreground of each widget in the top frame
        for widget in self.topWidgets:
            widget.configure(foreground=self.customFgCol, background=self.customBgCol)

        # Sets the background and foreground of each widget in each widget row depending on the type of widget
        for row, list in enumerate(self.widgetRows):
            for widget in self.widgetRows[row]:
                widget.configure(foreground=self.customFgCol, background=self.customBgCol)

        # Updates the window with the current colour properties
        self.win.update()

    # Method to pick the custom foreground colour
    def pickFgColour(self):
        colour = colorchooser.askcolor(title="Select Color")
        colour = colour[1]
        self.customFgCol = colour

    # Method to pick the custom background colour
    def pickBgColour(self):
        colour = colorchooser.askcolor(title="Select Color")
        colour = colour[1]
        self.customBgCol = colour

    # Making the run method for main code body.
    def run(self):
        self.createWidgets()
        self.updateClock()
        self.win.mainloop()


# Defining the main function
def main():
    testHouse = setUpHome()
    gui = SmartHomeSystem(testHouse)
    gui.run()


# Calling main to run
main()

# Extra features added
# Dynamic invalid input for lego error message just for fun after 2 incorrect
# Backend inheritance inside the backendChallenge.py file
# Every button now has custom images associated excluding the change text size button in accessibility

# CHALLENGES
# 4 marks - inheritance in backend - using smart device superclass
# 4 marks - advanced tkinter widgets - used checkboxes and scale inside add device window as well as scale in edit window
# 3 marks - custom visualisation - icon used for every button excluding change text size in accessibility
# 4 marks - Interface & Accessibility settings - made button for menu allowing for light, dark, custom themes and text scaling
# 4 marks - Permanent data storage - Not Applicable
# 4 marks - Device Scheduler - Not Applicable
