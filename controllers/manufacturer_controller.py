from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def product_categories():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers=manufacturers)

@manufacturers_blueprint.route("/manufacturers/new", methods=['GET'])
def new_task():
    return render_template("manufacturers/new.html")

@manufacturers_blueprint.route("/manufacturers", methods=['POST'])
def create_task():
    name=request.form['name']
    telephone_number=int(request.form['telephone_number'])
    address=request.form['address']
    manufacturer=Manufacturer(name,telephone_number,address)
    manufacturer_repository.save(manufacturer)
    return redirect("/manufacturers")