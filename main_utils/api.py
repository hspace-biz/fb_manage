from typing import List, Tuple

import requests

from main_utils import define, file
from main_utils.error import error
from main_utils.server_config import Server_Configs


class Facebook_Account:
    def __init__(self, data: dict):
        self.uid = data.get("uid")
        self.user_code = data.get("user_code")
        self.master_code = data.get("master_code")
        self.name = data.get("name")
        self.state = data.get("state")
        self.last_time_update_profile = data.get("last_time_update_profile")
        self.last_time_update_friends = data.get("last_time_update_friends")
        self.last_time_update_state = data.get("last_time_update_state")
        self.last_action = data.get("last_action")
        self.last_time_action = data.get("last_time_action")
        self.cookies = data.get("cookies")


def login() -> (Tuple[define.ResultType, str]):
    result, _ = check_token()
    if result == define.ResultBase.OK:
        
        return define.ResultBase.OK, "OK"

    configs = Server_Configs()
    ip = configs.ip
    port = configs.port
    s_key = configs.s_key
    token = configs.token
    ma_tv = configs.code
    token = None
    s_key = None
    data = {
        "email": configs.username,
        "password": configs.password
    }
    try:
        _ip = ip.split(".")
        for __ip in _ip:
            __ip = int(__ip)
            if __ip < 0 or __ip > 255:
                return define.ResultBase.THE_IP_NOT_CORRECT, f"0<={__ip}<=255"
    except Exception as ex:
        return define.ResultBase.ERROR_UNKNOW, "Error: {ex}"

    url = f"http://{ip}:{port}"
    try:
        res = requests.get(url=url, timeout=10)
    except requests.exceptions.ConnectTimeout as ex:
        return define.ResultBase.SERVER_TIMEOUT, "Error: {ex}"
    except Exception as ex:
        return define.ResultBase.ERROR_UNKNOW, "Error: {ex}"

    res = requests.post(url=url+"/login", json=data)
    if res.status_code != 200:
        return define.ResultBase.LOGIN_FAILED, "Error: {res.text}"
    try:
        res = res.json()
        print(res)
        if res.get("secret_key") is None:
            return define.ResultBase.THE_RESPONSE_FORMAT_IS_NOT_SUPPORTED, f"secret_key not found"

        if res.get("token") is None:
            return define.ResultBase.THE_RESPONSE_FORMAT_IS_NOT_SUPPORTED, f"token not found"

        if res.get("token").get("token_type") is None:
            return define.ResultBase.THE_RESPONSE_FORMAT_IS_NOT_SUPPORTED, f"token_type not found"

        if res.get("token").get("access_token") is None:
            return define.ResultBase.THE_RESPONSE_FORMAT_IS_NOT_SUPPORTED, f"access_token not found"

        if res.get("code") is None:
            return define.ResultBase.THE_RESPONSE_FORMAT_IS_NOT_SUPPORTED, f"ma_tv not found"

        s_key = res.get("secret_key")
        token = res.get("token").get("token_type")+" " + \
            res.get("token").get("access_token")
        code = res.get("code")
        data = {
            "ip": ip,
            "port": port,
            "username": configs.username,
            "password": configs.password,
            "token": token,
            "s_key": s_key,
            "code": code
        }
        file.save_data_configs(data=data)
        return define.ResultBase.OK, "OK"
    except Exception as ex:
        return define.ResultBase.ERROR_UNKNOW, "Error: {ex}"


def check_token() -> (Tuple[define.ResultType,  str]):
    configs = Server_Configs()
    ip = configs.ip
    port = configs.port
    s_key = configs.s_key
    token = configs.token
    ma_tv = configs.code
    api = "check_connection"
    data = {
        "ma_tv": ma_tv
    }

    url = f"http://{ip}:{port}/{api}"

    header = {
        "Authorization": token,
        "s-key": s_key
    }

    res = requests.get(url, json=data, headers=header)
    print(res.text)
    if res.status_code == 200:
        return define.ResultBase.OK, None
    return define.ResultBase.ERROR_UNKNOW, None


def get_list_facebook_account() -> (Tuple[define.ResultType, List[Facebook_Account] | str]):
    configs = Server_Configs()
    ip = configs.ip
    port = configs.port
    s_key = configs.s_key
    token = configs.token
    ma_tv = configs.code
    api = "get_all_facebook_account_by_user_code"
    data = {
        "ma_tv": ma_tv
    }

    url = f"http://{ip}:{port}/{api}"

    header = {
        "Authorization": token,
        "s-key": s_key
    }
    try:
        res = requests.get(url, json=data, headers=header)
        if res.status_code == 400:
            return define.ResultBase.THE_TOKEN_IS_EXPIRE, None
        if res.status_code != 200:
            return define.ResultBase.ERROR_UNKNOW, res.status_code
        data = res.json()
        data = data.get("data")
        if data is None:
            return define.ResultBase.DATA_NOT_FOUND_IN_RESPONSE, res.json()

        list_account = []
        for _data in data:

            fb_account = Facebook_Account(data=_data)
            list_account.append(fb_account)
        return define.ResultBase.OK, list_account

    except requests.exceptions.Timeout as ex:
        return define.ResultBase.SERVER_TIMEOUT, None
    except Exception as ex:
        return define.ResultBase.ERROR_UNKNOW, error.get_error_mess_in_ex(ex)


def insert_cookie(cookies: dict, is_update: bool, upsert: bool = True) -> (define.ResultType):
    configs = Server_Configs()
    ip = configs.ip
    port = configs.port
    s_key = configs.s_key
    token = configs.token
    code = configs.code
    api = "insert_cookie_for_master_user"
    data = {
        "cookies": cookies,
        "is_update": is_update,
        "master_code": code,
        "upsert": upsert
    }

    url = f"http://{ip}:{port}/{api}"

    header = {
        "Authorization": token,
        "s-key": s_key
    }
    try:
        res = requests.put(url, json=data, headers=header)
        print(res.text)
        if res.status_code == 400:
            return define.ResultBase.THE_TOKEN_IS_EXPIRE
        if res.status_code != 200:
            return define.ResultBase.ERROR_UNKNOW
        res = res.json()
        print(res)
        # TODO: READ STATE IN SERVER AND MAP TO FILE
        if res.get("state") is None:
            return define.ResultBase.THE_RESPONSE_FORMAT_IS_NOT_SUPPORTED
        state = res["state"]
        if state.get("is_exists"):
            return define.ResultBase.THE_COOKIE_ALREADY_EXISTS
        if state.get("the_format_is_incorrect"):
            return define.ResultBase.THE_COOKIES_FORMAT_IS_INCORRECT
        if state.get("is_ok"):
            return define.ResultBase.OK

        return define.ResultBase.RESULT_UNKNOW

    except requests.exceptions.Timeout as ex:
        return define.ResultBase.SERVER_TIMEOUT
    except Exception as ex:
        return define.ResultBase.ERROR_UNKNOW
