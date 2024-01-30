from wtforms import Form
from wtforms import StringField,TelField, IntegerField
from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms.validators import DataRequired, Email
class UserForm(Form):
  nombre=StringField("nombre")
  apaterno=StringField("apaterno")
  amaterno=StringField("amaterno")
  email=EmailField("email")
  edad=IntegerField("edad")