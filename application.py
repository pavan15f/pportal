import json
import mysql.connector

from flask import Flask,render_template,request



from forms import ProfileForm



with open("sensitiveInfo.json","r") as file:
    sensitiveInfo=file.read()

sensitiveInfoDict=json.loads(sensitiveInfo)

mydb = mysql.connector.connect(

    host= sensitiveInfoDict["host"],
    user=sensitiveInfoDict["user"],
    passwd=sensitiveInfoDict["password"],
    database=sensitiveInfoDict["database"]
)
mycursor = mydb.cursor()




application = app = Flask(__name__)
app.config['SECRET KEY'] = sensitiveInfoDict["SECRET KEY"]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view')
def view():
    mycursor.execute("select * from profile")
    dbs = mycursor.fetchall()
    return render_template('view.html',student_details=dbs)



@app.route("/add",methods=["GET","POST"])
def addProfile():
    pf=ProfileForm()
    if pf.validate_on_submit():
        profileInfo=request.form
        app.logger.info(profileInfo)
    return render_template("addProfile.html",form=pf)


if __name__ == '__main__':
    app.run(debug=True)
