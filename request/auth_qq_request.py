# @Time    : 2021/5/25 17:28
# @Author  : lucas
# @File    : auth_gitee_request.py
# @Project : SSO
# @Software: PyCharm
import requests
from request.auth_base_request import AuthBaseRequest
from auth_source import AuthSource
from utils.utils import build_url, get_real_state


class AuthQqRequest(AuthBaseRequest):
    # https://wiki.connect.qq.com/
    source = AuthSource.QQ

    def __init__(self, config):
        self.client_id = config.get("client_id")
        self.client_secret = config.get("client_secret")
        self.redirect_uri = config.get("redirect_uri")
        self.refresh_token = ""

    def get_access_token(self, code):
        body = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "redirect_uri": self.redirect_uri,

        }
        response = requests.post(self.source.get("access_token"), json=body)
        result = response.json()
        self.refresh_token = result.get("refresh_token")
        return result.get("access_token")

    def get_openid(self, access_token):
        params = {"access_token": access_token}
        response = requests.get(build_url(self.source.get("openid"), params=params))
        result = response.json()
        return result.get("openid")

    def get_user_info(self, access_token):
        openid = self.get_openid(access_token)
        params = {"access_token": access_token,
                  "oauth_consumer_key": self.client_id,
                  "openid": openid,
                  }
        response = requests.get(build_url(self.source.get("user_info"), params=params))
        result = response.json()
        return result

    def get_refresh_token(self):
        params = {"grant_type": "refresh_token",
                  "refresh_token": self.refresh_token}
        response = requests.get(build_url(self.source.get("access_token"), params=params))
        result = response.json()
        print(result)

    def authorize(self):
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "state": get_real_state()
        }
        return build_url(self.source.get("authorize"), params)


if __name__ == "__main__":
    from auth_config import AuthConfig
    qq = AuthQqRequest(AuthConfig.QQ)
    print(qq.authorize())
