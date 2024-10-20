from flask import Flask, render_template, redirect, request, url_for
from klkl import bus

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('mainbus.html')

@app.route('/search',methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        return render_template('searchbus.html')

@app.route('/fas',methods = ['POST', 'GET'])
def fas():
    if request.method == 'POST':
        message = list(request.form.listvalues())[0][0]
        a = bus(message)
        c=[]
        for b in a:
            c.append(b['시작'] + '~' + b['끝'] + '\n첫차 -, 막차 -, 배차 -분\n' + b['지역'])
        print(c[0])
        return render_template("fas.html", result=c)
