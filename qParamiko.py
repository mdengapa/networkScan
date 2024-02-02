import paramiko
import scpclient
from dotenv import dotenv_values

class qqSSH():
    _username = ""
    _password = ""
    _ipAddress  = ""
    _port = 22

    def ssh_credentials(self,host):
        output = dotenv_values("credentials.env")
        if (host == "CISCO"):
            self._username = output["CISCO_USER"]
            self._password = output["CISCO_PASSWORD"]
            self._ipAddress = output["CISCO_IPADDRESS"]
        elif (host == "LINUX"):
            self._username = output["LINUX_USER"]
            self._password = output["LINUX_PASSWORD"]
            self._ipAddress = output["LINUX_IPADDRESS"]

    def __init__(self, host) -> None:
        self.ssh_credentials(host)
        self.sshClient = paramiko.SSHClient()
       
    def ssh_username(self, vParameter):
        self._username = vParameter
    
    def ssh_password(self, vParameter):
        self._password = vParameter

    def ssh_port(self, vParameter):
        self._port = vParameter

    def ssh_Connect(self, hostIP=None):
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if (hostIP != None):
            hostname=hostIP 
        else:
            hostname = self._ipAddress
        self.sshClient.connect(hostname, 
                        port=self._port, 
                        username=self._username, 
                        password=self._password)

    def ssh_ExecCommand(self, command):
        stdin, stdout, stderr = self.sshClient.exec_command(command)
        output = stdout.read().decode()
        return(output)

    def scpWriteFile(self, localFile, remoteFile):
        scp =  scpclient(self.sshClient.get_transport()) 
        scp.put(localFile, remoteFile)

    def ssh_Close(self):
        self.sshClient.close()

