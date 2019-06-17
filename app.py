from flask import Flask, render_template, request
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

@app.route('/value', methods=['GET', 'POST'])
def h_select():
    if request.method == 'GET':
        result = db_controller.get_setting()
        print(result)
        return json.dumps(result)
    elif request.method == 'POST':
        node_info = json.loads(request.data.decode('utf-8'))
        print(node_info)
        db_controller.set_setting(node_info['node_id'], node_info['temp_value'], node_info['humi_value'])
        return json.dumps({"result" : 1})
        

if __name__ == '__main__' :
    app.run(host='localhost', port=9080)
