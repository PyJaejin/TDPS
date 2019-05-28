from flask import Flask, render_template
from src.DB_Controller import DB_Controller
import json
from datetime import datetime

app = Flask(__name__)
db_controller = DB_Controller()

@app.route('/test', methods=['GET'])
def tests():
    return 'embadded test!!'

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/select')
def h_select():
    result = db_controller.get_setting()
    print(result)
    return json.dumps(result)

if __name__ == '__main__' :
    app.run(host='localhost', port=8080)
