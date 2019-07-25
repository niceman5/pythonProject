# flask_var2.py
from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter, ValidationError
from flask import url_for

_USERS = {'1':'Trarek', '2':'Freya'}
_IDS = {id for id, var in _USERS.items()}

class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()

    def to_url(self, value):
        return _IDS[value]

app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser

@app.route('/api/person/<registered:name>')

def person(name):
    response = jsonify({'Hello hey ':name})
    # print(url_for('person', name='Trarek'))

    return response

if __name__ == '__main__':    
    app.run()