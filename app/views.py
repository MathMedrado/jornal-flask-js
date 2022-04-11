from crypt import methods
from itertools import product
from math import prod
from select import select
from django import views
from markupsafe import re
from .model import Products
from . import db
from flask import Blueprint, render_template, request, session
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'] )
def home():
    
    list = db.session.query(Products).all()

    return render_template('home.html',lista=list)

@views.route('/registry', methods=['GET', 'POST'])
def registry():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        price = data.get('price')
        type =  data.get('type')
        new_product = Products(name=name, price=price, type=type)
        db.session.add(new_product)
        db.session.commit()
        return render_template('home.html')

    return render_template('add.html')

@views.route('/remove', methods=['GET','POST'])
def remove():
    list = db.session.query(Products).all()

    return render_template('remove.html',lista=list)



@views.route('/deletar-prod', methods=['POST'])
def deletaProd():
    resposta = json.loads(request.data)
    value = resposta["resp"]
    prod = Products.query.get(value)

    db.session.delete(prod)
    db.session.commit()

    return render_template('home.html')