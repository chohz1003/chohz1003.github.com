from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('mainbus.html')

@app.route('/search',methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        return render_template('searchbus.html')


if __name__ == "__main__":
    app.run(debug = True)
