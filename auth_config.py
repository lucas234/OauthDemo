# @Time    : 2021/5/26 9:21
# @Author  : lucas
# @File    : auth_config.py
# @Project : SSO
# @Software: PyCharm


class AuthConfig(object):
    GITHUB = {
        "client_id": "",
        "client_secret": "",
        "redirect_uri": "http://localhost:5000/oauth/callback/github",
    }

    GITEE = {
        "client_id": "",
        "redirect_uri": "http://localhost:5000/oauth/callback/gitee",
        "client_secret": "",
    }

    QQ = {
        "client_id": "",
        # 修改hosts文件将dev.test.com映射到127.0.0.1；
        "redirect_uri": "http://dev.test.com:5000/oauth/callback/gitee",
        "client_secret": "",
    }
