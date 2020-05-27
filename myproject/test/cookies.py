from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response('')
    resp.set_cookie('username', 'the username')
    username = request.cookies.get('username')
    print(username)
    return username

@app.route('/test')
def test():
    return 'hello_world! 반가워요'


if __name__ == '__main__':
    # host지정
    # debug 지정. 운영 환경에서는 절대 사용하지 말아야한다.
    app.run(host='127.0.0.1', debug=True)