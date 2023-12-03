import qIOS_commands
import qBackup

def backup():
    print("Start Backup Process ...")
    qBackup.backup()
def tracking():
    #qqIOS_commands.searchNeighbors()
    qIOS_commands.searchNeighbors()
    print("Process Complete !!!")

while True:
    print("1. Backup")
    print("2. CDP")
    print("0. Exit")

    choice = input("Enter Choice: ")
    choice = choice.strip()

    if (choice == "1"):
        print("Backup process starting ...")
        backup()
    elif (choice =="2"):
        tracking()
    elif (choice == "0"):
        print("Exit")
        break
    else:
        print("Invalid option")
