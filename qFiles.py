
import time
import os
import shutil
import filecmp
import schedule

def _fileName(deviceName):
    #DateName = str(time.strftime("%Y%m%d-%H_%M_%S", time.gmtime()))
    DateName = str(time.strftime("%Y%m%d", time.gmtime()))
    output = deviceName + "_" + DateName + ".ios"
    return output

def writeMyFile(inputData, deviceName):
    workDir = '/home/q4qum/PKM/PKM/20-AREAS/201-RKF/2010-Network/'
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
                        print("Borrar " + file)
                        os.remove(backupDir + file)
                    else:
                        print("Mover a backup: " + workDir + file)
                        shutil.move(workDir + file, backupDir + file)