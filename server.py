from flask import Flask,render_template,request
import mysql.connector

mydb = mysql.connector.connect(

    host= "database-pavan15f.cm8dpurmdxxc.ap-south-1.rds.amazonaws.com",
    user="admin",
    passwd="admin123",
    database="database_pavan15f"
)




mycursor = mydb.cursor()

#mycursor.execute("GRANT FILE ON *.* TO 'database_pavan15f'@'database-pavan15f.cm8dpurmdxxc.ap-south-1.rds.amazonaws.com'")

#mycursor.execute("CREATE TABLE profile(USN CHAR(10) PRIMARY KEY, emailid VARCHAR(255) UNIQUE,firstname varchar(255),lastname varchar(255),sslc integer,puc int,diploma int,degreemarks integer,course varchar(20),ugbranch varchar(20),ugcgpa int,pgbranch varchar(30),pgcgpa int,phnum char(10))")

sql = "INSERT INTO profile(USN,emailid,firstname,lastname,sslc,puc,diploma,degreemarks,course,ugbranch,ugcgpa,pgbranch,pgcgpa,phnum) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = ("4NI17CS213","p21wqav@gmail.com","Pav","kals",13,93,00,56,"Be","is",8.9,"no",00,"6344653982")
mycursor.execute(sql, val)
mydb.commit()


app = Flask(__name__)
app.config['SECRET KEY'] = "123vittal"
@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/view')
def view():
    mycursor.execute("select * from profile")
    dbs = mycursor.fetchall()
   # mycursor.execute("SELECT * from profile INTO OUTFILE 'std1.txt';")
    return render_template('view.html',res=dbs)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
