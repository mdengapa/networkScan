
import qqParamiko

# CISCO Command : cdp neigbords

class Device:
    def __init__(self, deviceID, local="", remote="", platform="", IPAddress=""):
        self.DeviceID:str  = deviceID
        self.LocalPort:str  = local
        self.RemotePort:str  = remote
        self.Platform:str  = platform
        self.hostIP:str = IPAddress

    def updatePlatform(self, _platform):
        self.Platform = _platform

    def __str__(self):
        return " .DeviceID: " + self.DeviceID
    
    def __del__(self):
        #print("Destruyendo objeto ", self.DeviceID)
        pass

def existDevice(_deviceID, switches):
        return any(device.DeviceID == _deviceID for device in switches)
"""        exist:bool = False
        _item:int = 0
        while _item < len(switches):
            if _deviceID == switches[_item].DeviceID:
                exist = True
                break
            _item += 1
        return exist
"""

def isSwitch(_platform):
    _switchPark = ['WS','SF', 'C9']
    return _platform in _switchPark

def addDevice(input:str, switches):
    input = input.strip()
    if input and len(input) > 1:
        switchName = input[0:16].rstrip()
        platform = input[58:60] if len(input) > 50 else "WS"
        if not existDevice(switchName, switches) and isSwitch(platform):
            switch = Device(switchName, "", "", platform)
            switches.append(switch)
    """
    if input[0:1] != " " and len(input.rstrip()) > 1:
        if len(input) > 50:
            switchName = input[0:16].rstrip()
            _platform = input[58:60]
        else:
            switchName = input.replace("\r","")
            _platform = "WS"
        if existDevice(switchName, switches) == False:
 #           print ("Exist: " + str(switchName))
  #      else:
            if isSwitch(_platform):
                switch = Device(switchName, "","",_platform)
                switches.append(switch)
    """

def listSwitches(switches):
    print("Total de switches:" + str(len(switches)))
    _item = 0
    while _item < len(switches):
        print("switch item: " + str(_item).zfill(2) + " :" + switches[_item].DeviceID + " - Platform : " + switches[_item].Platform) 
        _item += 1

def readLines(input:str):
    _fullLine = ""
    _lineNumber = 1
    _posCharacter = 0
    switches:Device = []
    for _character in input:
        _posCharacter += 1
        if _character == "\n":
            if _lineNumber > 6:
                addDevice(_fullLine, switches)
            _fullLine = ""
            _lineNumber += 1
            _posCharacter = 0
        else:
            _fullLine = _fullLine + _character
    return switches
           
def executeCommand(_host, _IOSCommand):
    _sshClient = qqParamiko.qqSSH()
    _sshClient.ssh_Connect(_host)
    output = _sshClient.ssh_ExecCommand(_IOSCommand)
    #View command output
    #print(output,'utf8')
    _switches = readLines(output)
    _sshClient.ssh_Close()
    return _switches

def getDeviceIP(input:str):
    _fullLine = ""
    _lineNumber = 1
    _posCharacter = 0
    switches:Device = []
    for _character in input:
        _posCharacter += 1
        if _character == "\n":
            if _lineNumber > 6:
                addDevice(_fullLine, switches)
            _fullLine = ""
            _lineNumber += 1
            _posCharacter = 0
        else:
            _fullLine = _fullLine + _character
    _IPAddress = "IPaddress"
    return _IPAddress

def searchNeighbors(_host = '192.168.152.187', _IOSCommand = ("sh cdp neighbors")):
    _switches = executeCommand(_host, _IOSCommand)
    _item = 0
    while _item < len(_switches):
        print("switch item: " + str(_item).zfill(2) + " :" + _switches[_item].DeviceID + " - Platform : " + _switches[_item].Platform) 
        _output = searchNeigborsDetail(_host, _switches[_item].DeviceID )
        _switches[_item].hostIP = getDeviceIP(_output)
        _item += 1

def searchNeigborsDetail(_host = '', _hostname=""):
    _IOSCommand = "sh cdp entry " + _hostname
    _sshClient = qqParamiko.qqSSH()
    _sshClient.ssh_Connect(_host)
    _output = _sshClient.ssh_ExecCommand(_IOSCommand)
    print(_output,'utf8')
    _sshClient.ssh_Close()
    return _output
