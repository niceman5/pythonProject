from flask import Flask, jsonify
app = Flask(__name__)
count = 0

@app.route('/')
def hello():
    global count
    count = count + 1
    return jsonify(
        text='Hello. world',
        count=count
    )    


@app.route('/abuse')
def abuse():
    global count
    count = count + 100
    return jsonify(
        text='Hello. world',
        count=count
    )    

'''
main선언없이 실행
flask run


'''
if __name__ == '__main__':
    app.run(debug=True)