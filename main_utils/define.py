

from telnetlib import AUTHENTICATION


class ResultType():
    CODE = {}

    def __init__(self, code: str, msg: str, is_error: bool = False, is_ok: bool = False):
        self.code = code
        self.msg = msg
        self.is_error = is_error
        self.is_ok = is_ok
        ResultType.CODE[code] = self

    def to_dict(self):
        return {
            "code": self.code,
            "msg": self.msg,
            "is_error": self.is_error,
            "is_ok": self.is_ok
        }


class ResultBase:
    ALREADY_EXISTS: ResultType = ResultType(
        code=0, msg="ALREADY_EXISTS", is_error=True)
    THE_COOKIE_UPDATED: ResultType = ResultType(
        code=1, msg="THE_COOKIE_UPDATED", is_ok=True)
    SERVER_TIMEOUT: ResultType = ResultType(
        code=2, msg="SERVER_TIMEOUT", is_error=True)
    LOGIN_FAILED: ResultType = ResultType(
        code=3, msg="LOGIN_FAILED", is_error=True)
    LOGIN_SUCCESSFULLY: ResultType = ResultType(
        code=4, msg="LOGIN_SUCCESSFULLY", is_ok=True)
    THE_TOKEN_IS_EXPIRE: ResultType = ResultType(
        code=5, msg="THE_TOKEN_IS_EXPIRE", is_error=True)
    ERROR_UNKNOW: ResultType = ResultType(
        code=6, msg="ERROR_UNKNOW", is_error=True)
    THE_RESPONSE_FORMAT_IS_NOT_SUPPORTED: ResultType = ResultType(
        code=7, msg="THE_RESPONSE_FORMAT_IS_NOT_SUPPORTED", is_error=True)
    OK: ResultType = ResultType(code=8, msg="OK", is_ok=True)
    THE_COOKIES_FORMAT_IS_INCORRECT: ResultType = ResultType(
        code=9, msg="THE_COOKIES_FORMAT_IS_INCORRECT", is_error=True)
    RESULT_UNKNOW: ResultType = ResultType(
        code=11, msg="RESULT_UNKNOW", is_error=True)
    THE_PROXY_CONNECTION_LOST: ResultType = ResultType(
        code=12, msg="THE_PROXY_CONNECTION_LOST", is_error=True)
    DATA_NOT_FOUND_IN_RESPONSE: ResultType = ResultType(
        code=13, msg="DATA_NOT_FOUND_IN_RESPONSE", is_error=True)
    THE_IP_NOT_CORRECT: ResultType = ResultType(
        code=14, msg="THE_IP_NOT_CORRECT", is_error=True)
    AUTHENTICATION_CONFIG_NONE: ResultType = ResultType(
        code=15, msg="AUTHENTICATION_CONFIG_NONE", is_error=True)
    PERMISSION_DENIED: ResultType = ResultType(
        code=16, msg="PERMISSION_DENIED", is_error=True)
