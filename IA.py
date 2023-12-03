import qParamiko
import qFiles
import qqInventory

class Device:
    def __init__(self, deviceID, local="", remote="", platform="WS", IPAddress=""):
        self.DeviceID = deviceID
        self.LocalPort = local
        self.RemotePort = remote
        self.Platform = platform
        self.hostIP = IPAddress

def existDevice(_deviceID, switches):
    return any(device.DeviceID == _deviceID for device in switches)

def isSwitch(_platform):
    switchPark = ['WS', 'SF', 'C9']
    return _platform in switchPark

def addDevice(input, switches):
    input = input.strip()
    if input and len(input) > 1:
        switchName = input[0:16].rstrip()
        platform = input[58:60] if len(input) > 50 else "WS"
        if not existDevice(switchName, switches) and isSwitch(platform):
            switch = Device(switchName, "", "", platform)
            switches.append(switch)

def searchNeighbors(_host='', _IOSCommand="sh cdp neighbors"):
    sshClient = qParamiko.qqSSH()
    sshClient.ssh_Connect(_host)
    output = sshClient.ssh_ExecCommand(_IOSCommand)
    switches = readLines(output)
    sshClient.ssh_Close()

    for device in switches:
        print(f"Device: {device.DeviceID} - Platform: {device.Platform}")
        output = searchNeighborsDetail(_host, device.DeviceID)
        device.hostIP = getDeviceIP(output)

def readLines(input):
    fullLine = ""
    lineNumber = 1
    switches = []
    
    for character in input:
        if character == "\n":
            if lineNumber > 6:
                addDevice(fullLine, switches)
            fullLine = ""
            lineNumber += 1
        else:
            fullLine += character
    return switches

def getDeviceIP(input):
    # Implementar la lógica para obtener la dirección IP del dispositivo
    pass

def searchNeighborsDetail(_host='', _hostname=""):
    IOSCommand = f"sh cdp entry {_hostname}"
    sshClient = qParamiko.qqSSH()
    sshClient.ssh_Connect(_host)
    output = sshClient.ssh_ExecCommand(IOSCommand)
    sshClient.ssh_Close()
    return output

if __name__ == "__main__":
    searchNeighbors()