import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask,render_template,request

app = Flask('__name__')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def home(): 
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html',name=name)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operation = request.form.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'
    return render_template('calculator.html', result=result)

if(__name__=='__main__'):
    app.run(
        host=os.getenv('URL'),
        port=os.getenv('PORT'),
        debug=True
    )
