import paramiko
from dotenv import load_dotenv, dotenv_values


class qqSSH():
    _username = ""
    _password = ""
    _port = 22

    def ssh_credentials(self):
        """load_dotenv() """
        output = dotenv_values("devices.env")
        self._username = output["USER"]
        self._password = output["PASSWORD"]


    def __init__(self) -> None:
        self.ssh_credentials()
        self.sshClient = paramiko.SSHClient()
       
    def ssh_username(self, vParameter):
        self._username = vParameter
    
    def ssh_password(self, vParameter):
        self._password = vParameter

    def ssh_port(self, vParameter):
        self._port = vParameter

    def ssh_Connect(self, hostIP):
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshClient.connect(hostname=hostIP, 
                        port=self._port, 
                        username=self._username, 
                        password=self._password)

    def ssh_ExecCommand(self, command):
        stdin, stdout, stderr = self.sshClient.exec_command(command)
        output = stdout.read().decode()
        return(output)

    def ssh_Close(self):
        self.sshClient.close()

