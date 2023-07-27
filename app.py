from flask import Flask

app = Flask(__name__)

@app.get('/zombie')
def hello_world():  # put application's code here2
    return {"risk": "42"}

if __name__ == '__main__':
    app.run()
