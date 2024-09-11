from flask import Flask, render_template, request
import jimunja_select
from jimunja_separation import korean_separation

app = Flask(__name__)

@app.route('/')
def input():
   first_img = jimunja_select.select('입력')
   return render_template('input.html',result = first_img[0])

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      message = list(request.form.listvalues())[0][0]
      separation_message = korean_separation(message)
      img_message = jimunja_select.select(separation_message)
      return render_template("result.html",result1 = img_message[0], result2 = img_message[1:])

if __name__ == '__main__':
   app.run(debug = True)
