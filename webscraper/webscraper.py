import threading
from visitor import visitor
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    threading.Thread(target=visitor.visitor).start()
    return "<p>Olá, Fernanda!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)