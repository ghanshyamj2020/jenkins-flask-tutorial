from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Changed it up a Ghanshyam Kumar Jaiswar hhhhhhhh'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
