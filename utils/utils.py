# @Time    : 2021/5/25 17:31
# @Author  : lucas
# @File    : utils.py
# @Project : SSO
# @Software: PyCharm
import uuid
from urllib.parse import urlencode


def get_real_state():
    return uuid.uuid4().hex[:9]


def build_url(base_url: str, params: dict, *path) -> str:
    url = base_url
    if path:
        for i in path:
            url = '{}/{}'.format(url, i)
    if params:
        url = '{}?{}'.format(url, urlencode(params))
    return url


if __name__ == "__main__":
    print(get_real_state())
    print(build_url("http://www.baidu.com", {"q": "selenium"}))
    print(build_url("http://www.baidu.com", {}, "新闻"))
