from flask import Flask
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

if __name__ == '__main__':
    # host지정
    # debug 지정. 운영 환경에서는 절대 사용하지 말아야한다.
    app.run(host='127.0.0.1', debug=True)