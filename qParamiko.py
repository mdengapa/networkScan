from paramiko import client, ssh_exception
from scp import SCPClient
from dotenv import dotenv_values
from dataclasses import dataclass

@dataclass
class qqSSH():
    _username = ""
    _password = ""
    _ipAddress  = ""
    _port = 22

    def ssh_credentials(self,host) -> None:
        output = dotenv_values("credentials.env")
        if host == "CISCO":
            self._username = output["CISCO_USER"]
            self._password = output["CISCO_PASSWORD"]
            self._ipAddress = output["CISCO_IPADDRESS"]
        elif host == "LINUX":
            self._username = output["LINUX_USER"]
            self._password = output["LINUX_PASSWORD"]
            self._ipAddress = output["LINUX_IPADDRESS"]
    def __init__(self, host) -> None:
        self.ssh_credentials(host)
        self.sshClient = client.SSHClient()
       
    def ssh_username(self, vParameter) -> None:
        self._username = vParameter
    
    def ssh_password(self, vParameter) -> None:
        self._password = vParameter

    def ssh_port(self, vParameter) -> None:
        self._port = vParameter

    def ssh_Connect(self, hostIP=None) -> bool:
        _output: bool = False
        try:
            self.sshClient.set_missing_host_key_policy(client.AutoAddPolicy())
            if (hostIP != None):
                hostname=hostIP 
            else:
                hostname = self._ipAddress
            self.sshClient.connect(hostname, 
                            port=self._port, 
                            username=self._username, 
                            password=self._password,
                            allow_agent=False,
                            look_for_keys=False)
            _output = True
        except ssh_exception.NoValidConnectionsError:
            print("SSH Port not reachable")
        except ssh_exception.BadAuthenticationType as err_message:
            print(f"Authentication failed, check credentials. {err_message}")
        except ssh_exception.AuthenticationException:
            print("Authentication failed, check credentials")
        except ssh_exception.SSHException:
            print("Connection error.")
        return _output

    def ssh_ExecCommand(self, command) -> str:
        stdin, stdout, stderr = self.sshClient.exec_command(command)
        output = stdout.read().decode()
        return(output)

    def ssh_Close(self) -> None:
        try: 
            self.sshClient.close()
        except ssh_exception.NoValidConnectionsError:
            print("SSH Port not reachable")
        except ssh_exception.AuthenticationException:
            print("Authentication failed, check credentials")
    
    def ssh_SCP(self, localFile: str, remoteFile: str):
        with SCPClient(self.sshClient.get_transport()) as scp:
            scp.put(localFile, remoteFile)
