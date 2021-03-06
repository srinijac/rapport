# views.py

from flask import Flask, render_template, request, flash, redirect, url_for
import json
from app import app
from app import tr
from app.tr import sendsms, addnumber

#twilio
from twilio.rest import Client
import cgi
import cgitb
import os
from subprocess import Popen

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/caregiver')
def about():
    return render_template("caregiver.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/tr', methods=['GET', 'POST'])
def backtohome():
    first = request.values.get("first_name")
    last = request.values.get("last_name")
    number = request.values.get("to_phone_num1")
    m = str(first) + " " + str(last) + " is signed up! Welcome to Rapport!"
    print(number)
    #tr.addnumber(number)
    tr.sendsms(number, m)
    # os.system('python tr.py')
    return render_template("index.html")

@app.route('/requirements', methods=['GET', 'POST'])
def homewithreminders():
    vitamins = request.values.get("vitamins_taken")
    water = request.values.get("glasses_taken")
    medication = request.values.get("medicine_taken")
    number = request.values.get("to_phone_num2")
    m = "You must take: " + str(vitamins) + ", " + str(water) + " glasses of water, and " + str(medication) + " medication."
    print(number)
    #tr.addnumber(number)
    tr.sendsms(number, m)
    # os.system('python tr.py')
    return render_template("indexfinal.html")
