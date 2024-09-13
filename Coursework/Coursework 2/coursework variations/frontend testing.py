##############################
# Alexander Bevan
# Programming Coursework 2 - Frontend
# UP2198095
# Due date: 11/03/24 16:00 GMT
##############################
from backend import *
from tkinter import *


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


class SmartHomeSystem:
    def __init__(self, smartHome):
        # Initializing instance variables
        self.smartHome = smartHome
        self.widgetList = []
        self.labelVariables = []

        # Initializing window & window structure w/ frames
        self.win = Tk()
        self.win.title("Smart Control Hub")
        self.topFrame = Frame(self.win)
        self.topFrame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )
        self.bottomFrame = Frame(self.win)
        self.bottomFrame.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
        )
        # Initialize tkinter instance variables - done after window creation to avoid runtime error

    def createWidgets(self):
        # The button to turn on all devices
        onAllBtn = Button(
            self.topFrame,
            text='Turn on all',
            command=lambda: [self.smartHome.turnOnAll(), print(self.smartHome), self.textUpdate()]
        )
        onAllBtn.grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
        )
        # The button to turn off all devices
        offAllBtn = Button(
            self.topFrame,
            text='Turn off all',
            command=lambda: [self.smartHome.turnOffAll(), print(self.smartHome), self.textUpdate()]
        )
        offAllBtn.grid(
            row=0,
            column=1,
            padx=10,
            pady=0,
        )

        # The button to add a device - opens a new screen to ask for a device.
        addDeviceBtn = Button(
            self.topFrame,
            text='Add a Device',
            command=self.addButtonGui
        )
        addDeviceBtn.grid(
            row=0,
            column=2,
            padx=10,
            pady=0,
        )

        for deviceNumber in range(len(self.smartHome.devices)):
            widgetRow = []  # A list to store widget rows, this list will be added to another higher list
            deviceType = self.smartHome.getDevicesAt(deviceNumber)

            # The label text variable that will link to the label to dynamically update the text of it upon change.
            labelText = StringVar()
            labelText.set(deviceType)
            self.labelVariables.append(labelText)
            # The label of the text that displays the description of the object
            deviceLabel = Label(
                self.bottomFrame,
                text=deviceType,
                textvariable=self.labelVariables[deviceNumber]
            )
            deviceLabel.grid(
                row=deviceNumber + 1,
                column=0,
                padx=5,
                pady=5,
            )
            widgetRow.append(deviceLabel)
            # The toggle device button that toggles the state from on to off
            toggleDeviceBtn = Button(
                self.bottomFrame,
                text="Toggle Device",
                command=lambda index=deviceNumber: [self.smartHome.toggleSwitch(index), print(self.smartHome),
                                                    self.textUpdate()]
            )
            toggleDeviceBtn.grid(
                row=deviceNumber + 1,
                column=1,
                padx=5,
                pady=5,
            )
            widgetRow.append(toggleDeviceBtn)
            # The edit device button that opens a new window and allows for property modification
            editDeviceBtn = Button(
                self.bottomFrame,
                text="Edit Device",
                command=lambda index=deviceNumber: [self.editButtonCommand(index)]
            )
            editDeviceBtn.grid(
                row=deviceNumber + 1,
                column=2,
                padx=5,
                pady=5,
            )
            widgetRow.append(editDeviceBtn)
            # The remove device button that removes the device from the list
            removeDeviceBtn = Button(
                self.bottomFrame,
                text="Remove Device",
                command=lambda index=deviceNumber: [self.deleteButtonCommand(index)]
            )
            removeDeviceBtn.grid(
                row=deviceNumber + 1,
                column=3,
                padx=5,
                pady=5,
            )
            widgetRow.append(removeDeviceBtn)

            self.widgetList.append(widgetRow)

    def deleteButtonCommand(self, index):  # Command for the delete device button

        self.smartHome.removeDeviceAt(index)
        listToRemove = self.widgetList[index]
        # Finds widget list inside of list, for each widget, un-draw. Then delete list
        for widget in listToRemove:
            widget.grid_forget()
        del self.widgetList[index]
        # Deletes the textVariable with the associated label widget for the row inside of the labelVariables list
        del self.labelVariables[index]
        # update the command of each other remove button in each widget row sublist to stop out of range errors
        for widgetRow in self.widgetList:
            count = 0
            widgetRow[3].config(command=lambda index=count: [self.deleteButtonCommand(index)])
            count += 1

    def editButtonCommand(self, index):  # Command for the edit device button
        editButtonWindow = Toplevel(self.win)
        editButtonWindow.title('Device Attributes Edit Window')

        # Making the 2 frames
        topFrame = Frame(editButtonWindow)
        topFrame.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
        )
        bottomFrame = Frame(editButtonWindow)
        bottomFrame.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
        )
        # Making the 4 buttons - confirm, cancel, turn on, turn off.
        confirmBtn = Button(
            topFrame,
            text='Finish Editing',
            command=editButtonWindow.destroy
        )
        confirmBtn.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        deviceToggleBtn = Button(
            bottomFrame,
            text="Toggle Device",
            command=lambda: [self.smartHome.toggleSwitch(index), self.textUpdate()]
        )
        deviceToggleBtn.grid(
            row=0,
            column=3,
            padx=5,
            pady=5,
        )

        if isinstance(self.smartHome.devices[index], SmartPlug):

            instructions = Label(
                bottomFrame,
                text='Please select your consumption rate on the scale, the rate will change with the scale.'
            )
            instructions.grid(
                row=0,
                column=0,
                padx=5,
                pady=5,
            )
            consumptionRateScale = Scale(
                bottomFrame,
                from_=0, to=150,
                orient=HORIZONTAL,
                command=lambda scaleValue=Scale.get: [self.smartHome.devices[index].setConsumptionRate(scaleValue),
                                                      self.textUpdate()]
            )
            consumptionRateScale.grid(
                row=1,
                column=0,
                padx=10,
                pady=10,
            )

        elif isinstance(self.smartHome.devices[index], SmartDoorBell):

            sleepOnBtn = Button(
                bottomFrame,
                text="Toggle Sleep On",
                command=lambda: [self.smartHome.devices[index].setSleepMode('on'), self.textUpdate()]
            )
            sleepOnBtn.grid(
                row=0,
                column=0,
                padx=5,
                pady=5,
            )
            sleepOffBtn = Button(
                bottomFrame,
                text="Toggle Sleep Mode Off",
                command=lambda: [self.smartHome.devices[index].setSleepMode('off'), self.textUpdate()]
            )
            sleepOffBtn.grid(
                row=1,
                column=0,
                padx=5,
                pady=5,
            )

        # When the user clicks confirm edit, the value of the slider will be set to the consumption rate

    def addButtonCommand(self, window, plugChecked, bellChecked, scale):
        window.destroy()

        # create object & append to list
        if plugChecked and not bellChecked:
            self.smartHome.devices.append(SmartPlug(scale))
            print(self.smartHome)

        elif bellChecked and not plugChecked:
            self.smartHome.devices.append(SmartDoorBell())
            print(self.smartHome)

        # draw new widgets for device
        widgetRow = []
        # Text Label
        labelText = StringVar()
        labelText.set(self.smartHome.getDevicesAt((len(self.smartHome.devices) - 1)))
        self.labelVariables.append(labelText)
        deviceLabel = Label(
            self.bottomFrame,
            textvariable=labelText
        )
        deviceLabel.grid(
            row=len(self.smartHome.devices),
            column=0,
            padx=5,
            pady=5,
        )
        widgetRow.append(deviceLabel)

        toggleDeviceBtn = Button(
            self.bottomFrame,
            text="Toggle Device",
            command=lambda index=(len(self.smartHome.devices) - 1):
            [self.smartHome.toggleSwitch(index), print(self.smartHome), self.textUpdate()]
        )

        toggleDeviceBtn.grid(
            row=len(self.smartHome.devices),
            column=1,
            padx=5,
            pady=5,
        )
        widgetRow.append(toggleDeviceBtn)
        # Edit Button
        editDeviceBtn = Button(
            self.bottomFrame,
            text="Edit Device",
            command=lambda index=len(self.smartHome.devices): [self.editButtonCommand(index)]
        )
        editDeviceBtn.grid(
            row=len(self.smartHome.devices),
            column=2,
            padx=5,
            pady=5,
        )
        widgetRow.append(editDeviceBtn)
        # Remove Button
        removeDeviceBtn = Button(
            self.bottomFrame,
            text="Remove Device",
            command=lambda index=len(self.smartHome.devices): [self.deleteButtonCommand(index)]
        )
        removeDeviceBtn.grid(
            row=len(self.smartHome.devices),
            column=3,
            padx=5,
            pady=5,
        )
        widgetRow.append(removeDeviceBtn)

        self.widgetList.append(widgetRow)

        # Configuring the remove buttons so that they don't out of range error upon being added
        for widgetRow in self.widgetList:
            count = 0
            widgetRow[3].config(command=lambda index=count: [self.deleteButtonCommand(index)])
            count += 1

    def addButtonGui(self):
        # Make the toplevel
        addWin = Toplevel(self.win)
        addWin.title('Device Attributes Edit Window')

        # Add Button - adds device and closes previous window
        addBtn = Button(
            addWin,
            text='Add Device',
            command=lambda: self.addButtonCommand(addWin, cbx1value.get(), cbx2value.get(), scaleValue.get())
        )
        addBtn.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        # Checkboxes
        cbx1value = BooleanVar()  # define tkinter variables
        cbx2value = BooleanVar()
        cbx1 = Checkbutton(
            addWin,
            text="Smart Plug",
            variable=cbx1value,
        )
        cbx2 = Checkbutton(
            addWin,
            text="Smart DoorBell",
            variable=cbx2value,
        )
        cbx1.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
        )
        cbx2.grid(
            row=0,
            column=2,
            padx=10,
            pady=10,
        )
        # Instructions Label
        instruction = Label(addWin, text='Please select either plug or doorbell.\n '
                                         'If plug is selected set the consumption rate using the below scale then press add')
        instruction.grid(
            row=1,
            column=1,
        )
        # Consumption Rate slide
        scaleValue = IntVar()
        crScale = Scale(addWin, from_=0, to=150, orient=HORIZONTAL, variable=scaleValue)
        crScale.grid(
            row=2,
            column=1,
            pady=10,
        )

    def textUpdate(self):
        for i in range(len(self.smartHome.devices)):
            deviceType = self.smartHome.getDevicesAt(i)
            self.labelVariables[i].set(deviceType)

    def run(self):
        self.createWidgets()
        self.win.mainloop()


def main():
    testHouse = setUpHome()
    gui = SmartHomeSystem(testHouse)
    gui.run()


main()

# use inheritance from the start of the programming.
# use other widgets that we haven't been taught - frame
# STORE AS SETS OR ENUMS INSTEAD OF LISTS FOR THE WIDGETS TO REMOVE ISSUE OF LIST OUT OF INDEX RANGE
# when removing a device, the list is appended so that all the positions change without the command index numbers
# changing meaning that the final index is not removed due to the command trying to remove the object with the index
# that was previously correct but is now incorrect, giving the out of range error.
