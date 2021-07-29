
# import a library

from types import MethodDescriptorType
from flask import Flask, render_template, request
import joblib
# instance of an app

app = Flask(__name__)

model = joblib.load('dib_79.pkl')

@app.route('/')
def welcome():
    #return "welcome"
     return render_template('welcome.html')

@app.route('/html')
def html():
    return render_template('HTML Introduction.html')

@app.route('/Userinput')
def Userinput():
    return render_template('UserInputScreen.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/blog', methods = ['POST'])
def blog_page():
    
    a = request.form.get('preg')
    b = request.form.get('plas')
    c = request.form.get('pres')
    d = request.form.get('skin')
    e = request.form.get('test')
    f = request.form.get('mass')
    g = request.form.get('pedi')
    h = request.form.get('age')
    # print(Exp, email, contact, address)

    
  
    output = model.predict([[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h)]])

    if output[0] == 1:
        output1 = 'diabetic'
    else:
        output1 = 'not diabetic'
    
    return render_template('blog.html',predict_text = f'the person is {output1}')

    

@app.route('/contact')
def contact_page():
    return 'contact page'

#run the app
if __name__ == "__main__":
    app.run(debug=True)