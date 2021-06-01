# @Time    : 2021/5/25 17:21
# @Author  : lucas
# @File    : auth_base_request.py
# @Project : SSO
# @Software: PyCharm
from abc import abstractmethod, ABCMeta


class AuthBaseRequest(metaclass=ABCMeta):

    @abstractmethod
    def get_access_token(self, code):
        pass

    @abstractmethod
    def get_user_info(self, access_token):
        pass

    @abstractmethod
    def authorize(self):
        pass

    def login(self, code):
        try:
            access_token = self.get_access_token(code)
            user = self.get_user_info(access_token)
            return user
        except Exception as e:
            print(f"Failed to login with oauth authorization. {e}")
            return None
