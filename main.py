from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
import forms

app=Flask(__name__)
app.secret_key="esta es mi clave secreta"

@app.errorhandler(404)
def page_not_found(e):
 return render_template("404.html"),404

@app.before_request
def before_request():
  g.nombre="Mario"
  print("before 1")
  
@app.after_request
def after_request(response):
  print("after 3")
  return response
  

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/alumnos2", methods=["GET", "POST"])
def alumnos2():
  alumno_clase=forms.UserForm(request.form)
  print("alumno: {}".format(g.nombre))
  nom=""
  apa=""
  ama=""
  edad=""
  email=""
  if request.method=="POST" and alumno_clase.validate():
    nom=alumno_clase.nombre.data
    apa=alumno_clase.apaterno.data
    ama=alumno_clase.amaterno.data
    edad=alumno_clase.edad.data
    email=alumno_clase.email.data
    print("Nombre: {}".format(nom))
    print("Apaterno: {}".format(apa))
    print("Amaterno: {}".format(ama))
    print("Edad: {}".format(edad))
    print("Email: {}".format(email))
    
    mensaje="Bienvenido {}".format(nom)
    flash(mensaje)
  return render_template("alumnos2.html", form=alumno_clase, nom=nom, apa=apa, ama=ama, edad=edad, email=email)

@app.route("/alumnos")
def alumnos():
  titulo="UTL"
  nombres=["mario", "pedro","juan","dario"]
  return render_template("alumnos.html",titulo=titulo, nombres=nombres)

@app.route("/maestros")
def maestros():
  return render_template("maestros.html")

@app.route("/Hola")
def hola():
  return "<h1>Saludos desde Hola</h1>"

@app.route("/Saludo")
def saludo():
  return "<h1>Saludos desde Saludo</h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
  return "hola: "+nom

@app.route("/numero/<int:n1>")
def numero(n1):
  return "Numero: {}".format(n1)

@app.route("/usr/<int:id>/<string:nom>")
def func(id, nom):
  return "ID: {} Nombre: {}".format(id, nom)

@app.route("/suma/<float:n1>/<float:n2>")
def func2(n1,n2):
  return "la suma: {} + {} = {}".format(n1, n2, n1+n2)

@app.route("/calcular", methods=["GET","POST"])
def calcular():
  if request.method=="POST":
    num1=request.form.get("n1")
    num2=request.form.get("n2")
    return"La multiplicación de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))
  return'''
  <form action="/calcular" method="POST">
    <label>N1:</label>
    <input type="text" name="n1"><br>
    <label>N2:</label>
    <input type="text" name="n2"><br>
    <input type="submit"/>
  </form>
'''

@app.route("/OperasBas")
def operas():
  return render_template("OperaBas.html")

@app.route("/resultado", methods=["GET","POST"])
def result():
    if request.method=="POST":
      num1=request.form.get("n1")
      num2=request.form.get("n2")
      return"La multiplicación de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))
   

if __name__=="__main__":
  app.run(debug=True)
  