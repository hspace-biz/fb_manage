import requests
from main_utils.logger import logger
from main_utils.error import exceptions
from main_utils.define import ResultType,ResultBase
class Proxy:
    def __init__(self,proxy_str:str = None,
                 proxy_ip:str = None, proxy_port:str = None,
                 proxy_username:str = None,proxy_password:str = None
    ):
        if proxy_str:
            proxy_ip,proxy_port,proxy_username,proxy_password = proxy_str.replace(" ","").split(":")
        
        if not all([proxy_ip,proxy_port,proxy_username,proxy_password]):
            proxy_ip,proxy_port,proxy_username,proxy_password = None,None,None,None
        
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
    
    def to_url(self) -> (str):
        """Retrun url: user_name:pass@ip:port

        Returns:
            str: url
        """
        return f'{self.proxy_username}:{self.proxy_password}@{self.proxy_ip}:{self.proxy_port}'

    def to_dict(self) -> (dict):
        """Return proxy dict:
        {
            'http': f'http://sername:pass@ip:port',
            'https': f'https://sername:pass@ip:port',
        }

        Args:
            self (_type_): _description_

        Returns:
            dict: {
                'http': f'http://sername:pass@ip:port',
                'https': f'https://sername:pass@ip:port'
            }
        """
        return {
            'http': f'http://{self.to_url()}',
            'https': f'https://{self.to_url()}'
        }
        
    def check_connection(self)->(ResultType):
        self.session = requests.Session()
        self.session.proxies = self.to_dict()
        try:
            logger(f"Site check: https://ifconfig.me/")
            res = self.session.get("https://ifconfig.me/")
            logger().info(f' == My IP: {res.text}')
        except:
            return ResultBase.THE_PROXY_CONNECTION_LOST
        return ResultBase.OK
    
        
