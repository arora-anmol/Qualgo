from flask import Flask, render_template, request
from models import calculate_score
app = Flask(__name__)


@app.route('/search')
def main():
    return render_template('main.html')


@app.route('/company_analysis')
def company_analysis():
    company_name = request.args.get('company')
    score = calculate_score(company_name)
    return render_template('company_analysis.html', company_name=company_name, score=score)


@app.route('/')
def hello():
    return 'Hello world'


if __name__ == '__main__':
    app.run(host='127.0.01', port=8080, debug=True)