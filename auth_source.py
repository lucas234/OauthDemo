# @Time    : 2021/5/24 13:26
# @Author  : lucas
# @File    : auth_default_source.py
# @Project : SSO
# @Software: PyCharm


class AuthSource(object):
    GITHUB = {
        "authorize": "https://github.com/login/oauth/authorize",
        "access_token": "https://github.com/login/oauth/access_token",
        "user_info": "https://api.github.com/user",
    }

    GITEE = {
        "authorize": "https://gitee.com/oauth/authorize",
        "access_token": "https://gitee.com/oauth/token",
        "user_info": "https://gitee.com/api/v5/user",
    }

    QQ = {
        "authorize": "https://graph.qq.com/oauth2.0/authorize",
        "access_token": "https://graph.qq.com/oauth2.0/token",
        "user_info": "https://graph.qq.com/user/get_user_info",
        "openid": "https://graph.qq.com/oauth2.0/me",
    }
