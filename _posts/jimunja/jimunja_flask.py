from flask import Flask, render_template, request
import jimunja_select

app = Flask(__name__)

@app.route('/')
def student():
   first_img = jimunja_select.select('입력')
   return render_template('input.html',result = first_img)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      message = list(request.form.listvalues())[0][0]
      img_message = jimunja_select.select(message)
      return render_template("result.html",result = img_message)

if __name__ == '__main__':
   app.run(debug = True)