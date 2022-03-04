from main_utils.file import read_data_configs


class Server_Configs:

    def __init__(self):
        data = read_data_configs()
        self.ip = data.get("ip")
        self.port = data.get("port")
        self.username = data.get("username")
        self.password = data.get("password")
        self.token = data.get("token")
        self.s_key = data.get("s_key")
        self.code = data.get("code")
