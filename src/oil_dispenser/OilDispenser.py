import serial

class OilDispenser:
    def __init__(self, port, baudrate=57600, timeout=1):
        self.port = port
        self.serial = serial.Serial(port)

        # open the port
        self.open()

    # port utilities
    def open(self):
        try:
            self.serial.open()
        except serial.SerialException:
            print("Failed to open port.")

    def close(self):
        self.serial.close()

    def getVersion(self):
        self.serial.write(b'?version\n')
        return self.serial.readline()

    def getVoltages(self):
        self.serial.write(b'?voltages\n')
        return self.serial.readline()

    def getPowerSupply(self):
        self.serial.write(b'?powersupply\n')
        return self.serial.readline()

    # dispenser utilities
    def dispense(self, time: int):
        instruction = b'!drop ' + bytes(str(time), encoding='utf8')
        self.serial.write(instruction + b'\n')

    def setTimebase(self, timebase: int):
        instruction = b'!timebase ' + bytes(str(timebase), encoding='utf8')
        self.serial.write(instruction + b'\n')

    def getTimebase(self):
        self.serial.write(b'!timebase\n')
        return self.serial.readline()


if __name__ == "__main__":
    # test OilDispenser class
    dispenser = OilDispenser('COM7')
    dispenser.open()