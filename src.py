# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:46:29 2023

@author: DELL
"""

import mysql.connector as conn
from flask import Flask, render_template, request

cnx = conn.connect(user = 'root', password = ' ', host = 'localhost', database = 'recymate_db')
cursor = cnx.cursor()

app = Flask(__name__)

@app.route("/fetch-login-info", methods=["POST"])
def fetch_login_info():
    username = request.form.get('uname')
    password = request.form.get('pass')
    cursor.execute('CREATE TABLE IF NOT EXISTS login_info (uname varchar[10], pass varchar[10])')
    cursor.execute('INSERT INTO login_info (\'{0}\', \'{1})\')'.format(username, password))
    return "Data has been stored in the database successfully."

# @app.route("/fetch-pickup-info", methods=["POST"])
# def fetch_pickup_info():
#     name = request.form.get('pickup_requester_name')
#     phone_num = request.form.get('pickup_requester_phone')
#     address = request.form.get('pickup_requester_address')
    
#     cursor.execute('CREATE TABLE IF NOT EXISTS pickup_info (name varchar[10], addr varchar[30], phone varchar[10])')
#     cursor.execute('INSERT INTO pickup_info (\'{0}\', \'{1})\', \'{2}\')'.format(name, address, phone_num))
#     return "Data has been stored in the database successfully."

@app.route("/")
def homepage():
    return render_template('index.html')