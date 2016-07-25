from flask import Flask, render_template, request,redirect

#mysql = MySQL()
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('signin.html')


@app.route('/showIndex')
def showIndex():
    return render_template('index.html')


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    return redirect('/showIndex')
      
if __name__ == "__main__":
    app.run()
