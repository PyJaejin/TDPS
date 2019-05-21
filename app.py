from flask import Flask

app = Flask(__name__)

@app.route(‘/’)
def index():
    return 'embadded test!!'

if __name__ == ‘__main__’ :
    app.run(host='localhost', port=8080)