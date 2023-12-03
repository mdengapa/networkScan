import qParamiko
import qFiles
import json

def createBackup(sshClient, device):
    sshClient.ssh_Connect(device)
    output = sshClient.ssh_ExecCommand("sh run")
    qFiles.writeMyFile(output, device)

def backup():
    with open("device.json") as uFile:
        jsonData = json.load(uFile)

    for switch in jsonData["switches"]:
        print(switch["hostName"], " :", switch["hostIP"])
        sshClient = qParamiko.qqSSH()
        createBackup(sshClient,switch["hostIP"])
        sshClient.ssh_Close()
       