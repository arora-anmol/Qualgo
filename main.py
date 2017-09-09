from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/search')
def main():
    return render_template('main.html')
