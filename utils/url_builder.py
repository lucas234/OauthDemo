# @Time    : 2021/5/24 17:36
# @Author  : lucas
# @File    : url_builder.py
# @Project : SSO
# @Software: PyCharm
from urllib.parse import urlencode


class UrlBuilder(object):

    _baseurl = ""
    _params = dict()

    def from_baseurl(self, baseurl):
        self._baseurl = baseurl
        return self

    def with_path(self, path):
        self._baseurl = f"{self._baseurl}/{path}"
        return self

    def query_param(self, key, value):
        self._params[key] = value
        return self

    def query_params(self, dict_):
        self._params.update(dict_)
        return self

    def __str__(self):
        if not self._params:
            return self._baseurl
        return f"{self._baseurl}?{urlencode(self._params)}"
        # or return urlparse.urlunparse( ( "http", self.domain, self.path, self.params, "", "" )

    def build(self):
        return self.__str__()

if __name__ == '__main__':
    u = UrlBuilder()
    print(u.from_baseurl("www.example.com")
           .with_path('bobloblaw'))
    print(u.query_param('lawyer','yes'))
    print(u.with_path('elvis')
           .query_param('theking','true'))
    print(u.from_baseurl("www.example.com")
           .query_params({"state": 1, "callback":"http://localhost:8080/callback"}).build())