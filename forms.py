from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Email,regexp

class ProfileForm(FlaskForm):
    fName = StringField('First Name', validators=[DataRequired(message="Enter first name")])
    mName = StringField('Middle Name')
    lName = StringField('Last Name')
    email=StringField('Email',validators=[Email(message="Enter valid email")])
    usn=StringField('USN',validators=[regexp("4NI\d\d[A-Za-z][A-Za-z]\d\d\d",message="Enter valid USN")])
    submit=SubmitField("Submit")


    