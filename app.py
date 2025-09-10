from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return f"<h1>Текущая дата и время:</h1><h2>{current_time}</h2>"

if __name__ == '__main__':
    app.run(debug=True)