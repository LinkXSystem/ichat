import paramiko
from scp import SCPClient


class ScpServer(object):
    def __init__(self, host, port, username, password):
        self._server = paramiko.SSHClient()
        self._server.load_system_host_keys()
        self._server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._server.connect(host, port, username, password)

    def __getattr__(self, item):
        return self._server[item]

    # def heart(self):
    # self._server


class ScpClient(object):
    def __init__(self, server: ScpServer):
        self._client = SCPClient(server.get_transport())

    def __getattr__(self, item):
        return self._client[item]
