# @Time    : 2021/5/25 17:28
# @Author  : lucas
# @File    : auth_gitee_request.py
# @Project : SSO
# @Software: PyCharm
import requests
from request.auth_base_request import AuthBaseRequest
from auth_source import AuthSource
from utils.utils import build_url


class AuthGiteeRequest(AuthBaseRequest):
    # https://gitee.com/api/v5/oauth_doc#/
    source = AuthSource.GITEE

    def __init__(self, config):
        self.client_id = config.get("client_id")
        self.client_secret = config.get("client_secret")
        self.redirect_uri = config.get("redirect_uri")
        self.refresh_token = ""

    def get_access_token(self, code):
        body = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "client_secret": self.client_secret,
            "code": code
        }
        response = requests.post(self.source.get("access_token"), json=body)
        result = response.json()
        self.refresh_token = result.get("refresh_token")
        return result.get("access_token")

    def get_user_info(self, access_token):
        params = {"access_token": access_token}
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
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code"
        }
        return build_url(self.source.get("authorize"), params)


if __name__ == "__main__":
    from auth_config import AuthConfig
    gitee = AuthGiteeRequest(AuthConfig.GITEE)
    print(gitee.authorize())
