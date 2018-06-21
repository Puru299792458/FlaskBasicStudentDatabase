from flask import Flask,redirect,url_for,request,render_template
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
