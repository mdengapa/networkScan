import qqParamiko
import qqFiles
import json

def createBackup(sshClient, device):
    sshClient.ssh_Connect(device)
    output = sshClient.ssh_ExecCommand("sh run")
    qqFiles.writeMyFile(output, device)

def backup():
    with open("device.json") as uFile:
        jsonData = json.load(uFile)

    for switch in jsonData["switches"]:
        print(switch["hostName"], " :", switch["hostIP"])
        sshClient = qqParamiko.qqSSH()
        createBackup(sshClient,switch["hostIP"])
        sshClient.ssh_Close()
       