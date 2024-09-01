from flask import Flask, render_template, request
import selectt

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      #result = request.form
      a = list(request.form.listvalues())[0][0]
      b = selectt.selectt(a)
      print(a)
      print(b)
      return render_template("result.html",result = b)

if __name__ == '__main__':
   app.run(debug = True)
