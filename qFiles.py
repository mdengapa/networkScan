
import time
import os
import shutil
import filecmp
from dotenv import dotenv_values


import schedule

def _fileName(deviceName):
    #DateName = str(time.strftime("%Y%m%d-%H_%M_%S", time.gmtime()))
    DateName = str(time.strftime("%Y%m%d", time.gmtime()))
    output = deviceName + "_" + DateName + ".ios"
    return output

def writeMyFile(inputData, deviceName):
    output = dotenv_values("credentials.env")
    workDir = output["CISCO_BACKUPFOLDER"]
    #workDir = '/home/q4qum/PKM/PKM/20-AREAS/201-RKF/2010-Network/'
    workFile = _fileName(deviceName)
    with open(workDir + workFile, 'w') as my_data:
        my_data.write(inputData)
    fileUpdate(workDir, workFile)

def readMyFile(inputFile):
    ref = open(inputFile)
    ref_content = ref.readlines()
    ref.close()  
    print(f"Current directory {os.getcwd()}")
    print(ref_content,'utf8')  
    #for line in output.splitlines():
    #   print(line)
    #sshInvokeShell(ssh, **devnet_csr)
#schedule.every(15).seconds.do(connectSimple(ssh, **devnet_csr))

def fileUpdate(workDir, workFile):
    # appDir = '/home/q4qum/python/'
    backupDir = workDir + 'backup/'
    backupFiles = os.listdir(workDir)
    oldFile = workFile[0:workFile.index("_")]

    for file in backupFiles:
        if "_" in file:
            newFile = file[0:file.index("_")]
            dateFile = file[file.index("_")+1:len(file)-4]
            if (oldFile == newFile):
                if not ((workDir + file) == (workDir + workFile)):
                    if (filecmp.cmp(workDir + file, workDir + workFile, shallow=False)):
                        print("Borrar " + workDir + file)
                        os.remove(workDir + file)
                    else:
                        print("Mover a backup: " + workDir + file)
                        shutil.move(workDir + file, backupDir + file)

def loadFile():
    output = dotenv_values("credentials.env")
    workDir = output["CISCO_BACKUPFOLDER"]
    serverDir = output["CISCO_SERVERFOLDER"]
    for file in workDir:
        shutil.copy(workDir + file, serverDir + file)
        #scp archivo.txt usuario@dominio.com:/home/usuario
        print("Copy into the server folders: " + serverDir + file)

