from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def tests():
    return 'embadded test!!'

@app.route('/')
def main():
    return render_template("main.html")

if __name__ == '__main__' :
    app.run(host='localhost', port=8080)