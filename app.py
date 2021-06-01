from flask import Flask, render_template, request, redirect, url_for
from request.auth_gitee_request import AuthGiteeRequest
from request.auth_github_request import AuthGithubRequest
from request.auth_qq_request import AuthQqRequest
from auth_config import AuthConfig

app = Flask(__name__)


@app.route('/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/oauth/render/<platform>')
def render_auth(platform):
    auth_request = get_auth_request(platform)
    authorize_url = auth_request.authorize()
    return redirect(authorize_url, 302)


@app.route('/oauth/callback/<platform>')
def callback(platform):
    code = request.args.get("code")
    # 验证state(失败回到登录界面，成功继续),该步骤 略
    # state = request.args.get("state")
    auth_request = get_auth_request(platform)
    user_info = auth_request.login(code)
    name = user_info['login']
    if platform.lower() == "qq":
        name = user_info['login']
    return redirect(url_for('user', name=name))


def get_auth_request(platform):
    auth_requests = {
        "gitee": lambda: AuthGiteeRequest(AuthConfig.GITEE),
        "github": lambda: AuthGithubRequest(AuthConfig.GITHUB),
        "qq": lambda: AuthQqRequest(AuthConfig.QQ),
    }
    auth_request = auth_requests.get(platform.lower())
    if auth_request:
        return auth_request()
    else:
        raise Exception("未获取到有效的Auth配置!")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
