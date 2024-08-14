from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/welcome')
def welcome():
    return 'Welcome to My Flask App :)'

@app.route('/greet/<reemw>')
def greet(name):
    return f'Hello, This is Reem!'

