import qParamiko
import qFiles
import json

def backup():
    with open("device.json") as uFile:
        jsonData = json.load(uFile)

    for switch in jsonData["switches"]:
        print(switch["hostName"], " :", switch["hostIP"])
        sshClient = qParamiko.qqSSH("CISCO")
        sshClient.ssh_Connect(switch["hostIP"])
        output = sshClient.ssh_ExecCommand("sh run")
        qFiles.writeMyFile(output, switch["hostIP"])
        sshClient.ssh_Close()
        

       