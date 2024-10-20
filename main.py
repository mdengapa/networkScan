from qIOS_cdpNeighbors import neighbors
from qIOS_cdpNeighborsDetail import neighbordsDetail, listSwitches, Device, joinJSON
from qLinux_cmd import exec_MoveFiles2Server
from qBackup import backup

#ROOT: str = "192.168.130.100"
#ROOT: str = "192.168.130.101"
#ROOT: str = "192.168.130.139"
#ROOT: str = "192.168.130.140"
#ROOT: str = "192.168.130.147"
#ROOT: str = "192.168.130.180"
#ROOT: str = "192.168.130.198"
#ROOT: str = "192.168.130.103"
#ROOT: str = "192.168.130.187"
#ROOT: str = "192.168.130.182"
#ROOT: str = "192.168.130.190"
#ROOT: str = "192.168.130.193"
#ROOT: str = "192.168.130.195"
#ROOT: str = "192.168.130.144"
#ROOT: str = "192.168.130.145"
#ROOT: str = "192.168.130.196"
#ROOT: str = "192.168.130.184"
#ROOT: str = "192.168.130.189"
#ROOT: str = "192.168.130.102"
#ROOT: str = "192.168.130.149"
#ROOT: str = "192.168.130.148"
#ROOT: str = "192.168.130.176"
#ROOT: str = "192.168.130.173"
#ROOT: str = "192.168.130.188"
#ROOT: str = "192.168.130.194"  OP2
#ROOT: str = "192.168.130.146"
#ROOT: str = "192.168.130.183"
#ROOT: str = "192.168.130.181"
ROOT: str = "192.168.130.10"

def main() -> None:
    # switches: Device = neighbordsDetail(ROOT)
    # if len(switches) > 0:
    #     listSwitches(switches,ROOT)
    # joinJSON()
    # print("Process finished !!!")

    while True:
        print("1. Backup")
        print("2. CDP neighbors")
        print("3. CDP neighbors detail")
        print("4. Synchronize backup files")
        print("0. Exit")
        choice = input("Enter Choice: ").strip()

        if choice == "1":
            print("Backup process starting ...")
            backup()
        elif choice == "2":
            neighbors(ROOT)
            print("Subprocess completed!!!")
        elif choice == "3":
            switches: list = neighbordsDetail(ROOT)
            if len(switches) > 0:
                listSwitches(switches,ROOT)
        elif choice == "4":
            exec_MoveFiles2Server()
        elif choice == "0":
            print("Exit")
            break
        else:
            print("Invalid option")
        print("Process Completed !!!")


if __name__ == "__main__":
    main()