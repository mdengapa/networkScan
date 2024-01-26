import qIOS_commands
import qBackup
import MoveExportAvocet

def backup():
    print("Start Backup Process ...")
    qBackup.backup()
def tracking():
    #qqIOS_commands.searchNeighbors()
    qIOS_commands.searchNeighbors()
    print("Process Complete !!!")

def linuxConnect():
    qIOS_commands.connect2Linux()
    print("Connection done!!!")

while True:
    print("1. Backup")
    print("2. CDP")
    print("3. Connect to Linux")
    print("0. Exit")

    choice = input("Enter Choice: ")
    choice = choice.strip()

    if (choice == "1"):
        print("Backup process starting ...")
        backup()
    elif (choice =="2"):
        tracking()
    elif (choice =="3"):
        linuxConnect()
    elif (choice == "4"):
        MoveExportAvocet()
    elif (choice == "0"):
        print("Exit")
        break
    else:
        print("Invalid option")
