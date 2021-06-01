# @Time    : 2021/5/25 17:21
# @Author  : lucas
# @File    : auth_github_request.py
# @Project : SSO
# @Software: PyCharm
import requests
from request.auth_base_request import AuthBaseRequest
from utils.utils import build_url, get_real_state
from auth_source import AuthSource


class AuthGithubRequest(AuthBaseRequest):
    # https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps
    source = AuthSource.GITHUB

    def __init__(self, config):
        self.client_id = config.get("client_id")
        self.client_secret = config.get("client_secret")
        self.redirect_uri = config.get("redirect_uri")

    def get_access_token(self, code):
        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code}
        header = {"Accept": "application/json"}
        response = requests.post(self.source.get("access_token"), json=body, headers=header)
        result = response.json()
        return result.get("access_token")

    def get_user_info(self, access_token):
        header = {"Authorization": f"token {access_token}"}
        response = requests.get(self.source.get("user_info"), headers=header)
        result = response.json()
        return result

    def authorize(self):
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": "user",
            "state": get_real_state()
        }
        return build_url(self.source.get("authorize"), params)


if __name__ == "__main__":
    from auth_config import AuthConfig

    github = AuthGithubRequest(AuthConfig.GITHUB)
    print(github.authorize())
