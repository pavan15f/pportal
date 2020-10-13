from flask import Flask,render_template,request
import mysql.connector

mydb = mysql.connector.connect(

    host= "database-pavan15f.cm8dpurmdxxc.ap-south-1.rds.amazonaws.com",
    user="admin",
    passwd="admin123",
    database="database_pavan15f"
)
mycursor = mydb.cursor()




app = Flask(__name__)
app.config['SECRET KEY'] = "123vittal"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view')
def view():
    mycursor.execute("select * from profile")
    dbs = mycursor.fetchall()
    return render_template('view.html',student_details=dbs)


if __name__ == '__main__':
    app.run(debug=True)
