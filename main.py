from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import requests
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

app = Flask(__name__)

response = requests.get('https://fakestoreapi.com/products')
products = response.json()

@app.route('/')
def home():
    bestsellers_main = products[13:17]  
    trending_now = products[6:9]
    bestsellers = products[3:6]
    featured_products = products[0:3]
    return render_template('index.html',products=bestsellers_main, trending_now=trending_now, bestsellers=bestsellers, featured_products=featured_products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/shipping-info')
def shipping_info():
    return render_template('shipping-info.html')

@app.route('/return-policy')
def return_policy():
    return render_template('return-policy.html')

@app.route('/terms-of-service')
def TermsOfService():
    return render_template('tos.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/categories')
def category():
    return render_template('category.html',products=products)

if __name__ == '__main__':
    app.run(debug=True)