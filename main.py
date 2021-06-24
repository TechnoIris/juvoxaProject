from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

import config

web_site = Flask(__name__)
web_site.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
web_site.config['SQLALCHEMY_DATABASE_URI']="postgresql://maath:_14326@localhost:5432/hospital"
db = SQLAlchemy(web_site)
migrate = Migrate(web_site, db)

web_site.config.update(
    TESTING=True,
    SECRET_KEY=b'something'
)


class Prescription(db.Model):
    __tablename__ = 'prescription'

    id = db.Column(db.Integer, primary_key=True)
    prescription = db.Column(db.String())
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

    def __init__(self, name, model, doors):
        self.prescription = prescription
        self.doctor = doctor
        self.patient = patient


class Doctor(db.Model):
    __tablename__ = 'doctor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'))

    def __init__(self, name, hospital):
        self.name = name
        self.hospital = hospital

class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name, hospital):
        self.name = name

class Hospital(db.Model):
    __tablename__ = 'hospital'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())



class MainDB(db.Model):
    __tablename__ = 'maindb'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    who = db.Column(db.String())
    passphrase = db.Column(db.String())

    def __init__(self, name, who, passphrase):
        self.name = name
        self.who = who
        self.passphrase = passphrase

    def __repr__(self):
        return f"<User {self.name} Created>"

@web_site.route('/')
def index():
	return render_template('index.html')


@web_site.route('/register/')
def generate_user():
	return render_template('register.html', message="")


@web_site.route('/check_log/', methods=["GET", "POST"])
def check_log():
	if request.method == "POST":
		name = request.form.get('Name', None)
		type = request.form.get('Type', None)
		pas1 = request.form.get('passphrase', None)
		pas2 = request.form.get('passphrasecopy', None)
		if name != '' and type != '' and pas1 != '' and pas2 != '':
			if pas1 != pas2:
				return render_template('register.html', message="password didn't match.")
			new_user = MainDB(name=name, who=type, passphrase=pas1)
			db.session.add(new_user)
			db.session.commit()
		else:
			return render_template('register.html', message="[*]Mandatory: Fill all the form fields.")
	return render_template('login.html', message=f"successfully registered the {type} as {name}.")

@web_site.route('/login/')
def login_user():
	return render_template('login.html', message="")

@web_site.route('/Hospital/<name>', methods=['GET', 'PUT', 'DELETE'])
def HospitalPage(name):
	hospital = Hospital.query.filter_by(name=name).first()
	data = []
	if hospital:
		x = Doctor.query.filter_by(hospital_id = hospital.id)
		for i in x:
			did = i.id
			dname = Doctor.query.filter_by(id=did).first()
			data.append([dname.name])
	return render_template('hospital.html', message=f"Welcome to the portal: hospital {name} helpline desk", data=data)

@web_site.route('/Doctor/<name>', methods=['GET', 'PUT', 'DELETE'])
def DoctorPage(name):
	doctor = Doctor.query.filter_by(name=name).first()
	data = []
	if doctor:
		x = Prescription.query.filter_by(doctor_id = doctor.id)
		for i in x:
			pid = i.patient_id
			pname = Patient.query.filter_by(id=pid).first()
			data.append([pname.name, i.prescription])
	return render_template('doctor.html', name=name, data=data)

@web_site.route('/Patient/<name>', methods=['GET', 'PUT', 'DELETE'])
def PatientPage(name):
	pname = Patient.query.filter_by(name=name).first()
	data = []
	if pname:
		x = Prescription.query.filter_by(patient_id = pname.id)
		for i in x:
			did = i.doctor_id
			dname = Doctor.query.filter_by(id=did).first()
			data.append([dname.name, i.prescription])
	return render_template('patient.html', name=name, data=data)


@web_site.route('/director/', methods=['GET', 'POST'])
def redirect_user():
	if request.method == "POST":
		name = request.form.get('Name', None)
		type = request.form.get('Type', None)
		passphrase = request.form.get('passphrase', None)
		if name != '' and passphrase != '':
			access = MainDB.query.filter_by(name = name, who = type, passphrase=passphrase).limit(1).first()
			if access:
				if access.who == 'doctor':
					return redirect(url_for('.DoctorPage', name=name))
				elif access.who == 'hospital':
					return redirect(url_for('.HospitalPage', name=name))
				else:
					return redirect(url_for('.PatientPage', name=name))
			return render_template('login.html', message="No records found...")


if __name__ == '__main__':
	web_site.run(host='0.0.0.0', port=8080)
