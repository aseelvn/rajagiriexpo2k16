from flask import Flask, render_template, request,redirect
#from flask.ext.mysql import MySQL
#from werkzeug.wsgi import LimitedStream

#mysql = MySQL()
app = Flask(__name__)

# MySQL configurations

#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'mysqlaccount'
#app.config['MYSQL_DATABASE_DB'] = 'expo'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)

@app.route('/')
def main():
    return render_template('signin.html')


@app.route('/showIndex')
def showIndex():
    return render_template('index.html')


@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        
        _password = request.form['inputPassword']
        if (_password in ("abcd","abcde")):
            return redirect('/showIndex')
        else:
            return render_template("error.html")
        

       # con = mysql.connect()
        #cursor = con.cursor()
        #cursor.callproc('sp_validateLogin',(_password,))
        #data = cursor.fetchall()

        


        #if len(data) > 0:
         #   if (str(data[0][0])==_password):
                
          #      return redirect('/showIndex')
           # else:
            #    return render_template('error.html')
        #else:
         #   return render_template('error.html')
            

    except Exception as e:
        return render_template('error.html',error = str(e))
    #finally:
       # cursor.close()
        #con.close()


if __name__ == "__main__":
    app.run()
