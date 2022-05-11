from email.mime import application
from multiprocessing.spawn import import_main_path
from random import randint
from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from random import randint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/store"#on definie l'url de la database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)#creation de la db permettant l'interraction avec la base de données

faker = Faker()

def populate_table():
    for n in range(0,100):
        x=faker.first_name()
        y=faker.last_name()
        mail=x+'.'+y+'@gmail.com'
        new_user = User(x, y, faker.pyint(0,80), mail, faker.job()) #creation de 100 personnes aléatoire
        apps = ['Facebook', 'Twitter', 'Instagram', 'Linkedin', 'Snapchat', 'Youtube', 'Discord', 'Teams', 'Skype']
        nb_app=randint(0,8)
        applications = []
        for app_n in range (0, nb_app) :
            app = Application(apps[app_n],faker.name(),faker.pyint(0,10))
            applications.append(app)
        new_user.applications = applications #on associe a l'user plusierurs applications 
        db.session.add(new_user)
    db.session.commit()
 
@app.route("/", methods =["POST","GET"]) #on défini la route de l'api 
def users():
    if request.method == "GET" :
        result = User.query.all()
        users = []
        for row in result : 
            user = {
                "id":row.id,
                "firstname": row.firstname,
                "lastname":row.lastname,
                "age":row.age,
                "email":row.email,
                "job":row.job
            }
            users.append(user)
        return jsonify(users)

class User(db.Model): #le db est crée grâce à la commande flask
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    job = db.Column(db.String(100))
    applications = db.relationship('Application')

    def __init__(self, firstname, lastname , age, email, job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self. email = email
        self.job = job

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appname = db.Column(db.String(100))
    username = db.Column(db.String(100))
    lastconnection = db.Column(db.Integer)
    email = db.Column(db.String(100))
    job = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, appname, username , lastconnection):
        self.appname = appname
        self.username = username
        self.lastconnection = lastconnection

if __name__ == '__main__':#point d'entrée de l'application
    db.drop_all()#ca supprime tout et ca recreer par la suite 
    db.create_all()
    populate_table()
    app.run(host="0.0.0.0", port=8080, debug=True)