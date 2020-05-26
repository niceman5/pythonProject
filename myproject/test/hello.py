from flask import Flask
app = Flask(__name__)
'''
route() 데코레이터는 함수와 URL을 연결해준다.
@app.route(‘/’) def index():
return ‘Index Page’
@app.route(‘/hello’) def hello():

return ‘Hello World’

URL의 변수 부분을 추가하기위해 여러분은 <variable_name>``으로 URL에 특별한 영역으로 표시해야된다.
그 부분은 함수의 키워드 인수로써 넘어간다.  선택적으로, ``<converter:variable_name>

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


int	accepts integers
float	like int but for floating point values
path	like the default but also accepts slashes



'''
@app.route('/')
def hello_world():
    return 'hello_world'

if __name__ == '__main__':
    # host지정
    # debug 지정. 운영 환경에서는 절대 사용하지 말아야한다.
    app.run(host='127.0.0.1', debug=True)