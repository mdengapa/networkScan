
import time
import os
import schedule

def _fileName(deviceName):
    #DateName = str(time.strftime("%Y%m%d-%H_%M_%S", time.gmtime()))
    DateName = str(time.strftime("%Y%m%d", time.gmtime()))
    output = deviceName + "_" + DateName + ".ios"
    return output

def writeMyFile(inputData, deviceName):
    localFile = _fileName(deviceName)
    with open(localFile, 'w') as my_data:
        my_data.write(inputData)

def readMyFile(inputFile):
    ref = open(inputFile)
    ref_content = ref.readlines()
    ref.close()  
    print(f"Current directory {os.getcwd()}")
    print(ref_content,'utf8')  

    #sshInvokeShell(ssh, **devnet_csr)
#schedule.every(15).seconds.do(connectSimple(ssh, **devnet_csr))

    for line in output.splitlines():
        print(line)