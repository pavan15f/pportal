from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,FloatField,DateField
from wtforms.validators import DataRequired,Email,regexp

class ProfileForm(FlaskForm):
    fName = StringField('First Name', validators=[DataRequired(message="Enter first name")])
    mName = StringField('Middle Name')
    lName = StringField('Last Name')

    email=StringField('Email',validators=[Email(message="Enter valid email")])
    usn=StringField('USN',validators=[regexp("4NI\d\d[A-Za-z][A-Za-z]\d\d\d",message="Enter valid USN")])
    
    sslcName = StringField("SSLC/10th Institution Name")
    sslcMarks=StringField("SSLC Marks(%)",validators=[DataRequired(message="Required")])
    sslcYop= DateField("Year Of Passing")

    pucName = StringField("PUC/12th Institution Name")
    pucMarks=StringField("PUC/Diploma Marks(%)",validators=[DataRequired(message="Required")])
    pucYop=DateField("Year Of Passing")
    
    diplomaMarks = StringField("Diploma Marks(%)")
    diplomaYop = DateField("Year Of Passing")

    degreeMarks=StringField("Degree (%)",validators=[DataRequired(message="Required")])
    degreeYop=DateField("Degree Course",validators=[DataRequired(message="Required")])
    course = StringField("Course")

    ugBranch = StringField("UG-Branch")
    ugCgpa = StringField("UG-Cgpa")

    pgBranch = StringField("PG-Branch")
    pgCgpa = StringField("PG-Cgpa")

    phNum = StringField("Phone Number")

    submit=SubmitField("Submit")