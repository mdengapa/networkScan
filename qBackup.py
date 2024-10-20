from qParamiko import qqSSH
from qFile import writeMyFile
import json


def backup():
    with open("device.json") as uFile:
        json_data = json.load(uFile)

    for switch in json_data["switches"]:
        print(switch["hostName"], " :", switch["hostIP"])
        ssh_client = qqSSH("CISCO")
        ssh_client.ssh_Connect(switch["hostIP"])
        output = ssh_client.ssh_ExecCommand("sh run")
        writeMyFile(output, switch["hostIP"])
        ssh_client.ssh_Close()

