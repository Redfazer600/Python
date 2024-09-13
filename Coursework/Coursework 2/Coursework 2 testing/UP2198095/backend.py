##############################
# Alexander Bevan
# Programming Coursework 2 - Backend
# UP2198095
# Due date: 11/03/24 16:00 GMT
##############################

# Task 1 - Smart Plug class
class SmartPlug:
    def __init__(self, consumption):
        consumption = str(consumption)  # This is for input validation, converts to a string if not already
        while True:                     # Then checks if the string is numeric, if so converts to int and validates
            if consumption.isnumeric():
                consumption = int(consumption)
                if 150 >= consumption >= 0:
                    break               # Breaks validation loop if valid & continues initializing instance vars
            else:
                consumption = input(int('Please enter an integer between 0 and 150'))

        self.switchedOn = False
        self.consumptionRate = consumption

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getOperationalStatus(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def setConsumptionRate(self, consumption):
        consumption = str(consumption)  # Same validation technique as above used - check can convert, check in range.
        while True:
            if consumption.isnumeric():
                consumption = int(consumption)
                if 150 >= consumption >= 0:
                    self.consumptionRate = consumption
                    break
            else:
                consumption = input(int('Please enter an integer between 0 and 150'))

    def __str__(self):

        if self.switchedOn:
            switch = 'On'
        else:
            switch = 'Off'

        output = f'SmartPlug: {switch},\nConsumption: {self.consumptionRate}'
        return output


# Task 1 part 2 - TestSmartPlug function
def testSmartPlug():
    plug = SmartPlug(45)
    plug.toggleSwitch()
    print(plug.switchedOn)
    print(plug.consumptionRate)
    plug.setConsumptionRate(75)
    print(plug.consumptionRate)
    print(plug)


# testSmartPlug()                       # Calling the test function for debugging

# Task 2 - Custom Smart Device Class (from table - Smart Door Bell)
class SmartDoorBell:

    def __init__(self):
        self.switchedOn = False
        self.sleepMode = False

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getOperationalStatus(self):
        return self.switchedOn

    def getSleepMode(self):
        return self.sleepMode

    def setSleepMode(self, mode):

        if mode.lower() == 'on':
            self.sleepMode = True

        elif mode.lower() == 'off':
            self.sleepMode = False

    def __str__(self):
        if self.sleepMode:
            sleep = 'On'
        else:
            sleep = 'Off'
        if self.switchedOn:
            switch = 'On'
        else:
            switch = 'Off'
        output = f'SmartDoorBell: {switch},\nSleep mode: {sleep}'
        return output

# Task 2 part 2 - TestSmartDoorbell function
def testSmartDoorbell():
    doorbell = SmartDoorBell()
    doorbell.toggleSwitch()
    print(doorbell.getOperationalStatus())
    doorbell.sleepMode = False
    print(doorbell)


# testSmartDoorbell()                       # Calling the test function for debugging

# Task 3 - Smart Home Class
# Task 3 - Smart Home
class SmartHome:
    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices

    def getDevicesAt(self, index):
        return self.devices[index]

    def addDevice(self, device):
        self.devices.append(device)

    def removeDeviceAt(self, index):
        del self.devices[index]

    def toggleSwitch(self, index):
        self.devices[index].toggleSwitch()

    def turnOnAll(self):
        for device in self.devices:
            if not device.switchedOn:
                device.toggleSwitch()

    def turnOffAll(self):
        for device in self.devices:
            if device.switchedOn:
                device.toggleSwitch()

    def __str__(self):
        output = f'A smart home with the following devices:\n'
        for device in self.devices:
            output += f'\n{device}\n'       # Newline before and after each device added to string for formatting.
        return output


def testSmartHome():
    home = SmartHome()
    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    doorbell1 = SmartDoorBell()
    home.addDevice(plug1)
    home.addDevice(plug2)
    home.addDevice(doorbell1)
    home.toggleSwitch(0)
    home.getDevicesAt(0).setConsumptionRate(150)
    home.getDevicesAt(1).setConsumptionRate(25)
    print(home)
    home.turnOnAll()
    print(home)
    home.removeDeviceAt(0)
    print(home)

# testSmartHome()                       # Calling the test function for debugging

##### Additional note #####
# I am aware that the backend does not need input validation for the smart plug if it is being coded in the frontend
# to only be passed a correct value every time, the validation here is just acting as a backup and was used in testing
# and creation of the frontend to identify issues with my code in due process.
