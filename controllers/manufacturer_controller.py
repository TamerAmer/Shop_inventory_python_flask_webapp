from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_category_repository as product_category_repository
import repositories.supplier_repository as supplier_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers=manufacturers)

@manufacturers_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    return render_template("manufacturers/new.html")

@manufacturers_blueprint.route("/manufacturers", methods=['POST'])
def create_manufacturer():
    name=request.form['name']
    telephone_number=int(request.form['telephone_number'])
    address=request.form['address']
    manufacturer=Manufacturer(name,telephone_number,address)
    manufacturer_repository.save(manufacturer)
    return redirect("/manufacturers")

@manufacturers_blueprint.route("/manufacturers/<id>/edit")
def edit_manufacturer(id):
    manufacturer=manufacturer_repository.select(id)
    return render_template("manufacturers/edit.html", manufacturer=manufacturer)

@manufacturers_blueprint.route("/manufacturers/<id>", methods=["POST"])
def update_manufacturer(id):
    name=request.form['name']
    telephone_number=request.form['telephone_number']
    address=request.form['address']
    manufacturer=Manufacturer(name,telephone_number,address,id)
    manufacturer_repository.update(manufacturer)
    return redirect("/manufacturers",)

@manufacturers_blueprint.route("/manufacturers/<id>/delete")
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")
    
@manufacturers_blueprint.route("/manufacturers/<id>/show")
def show_products(id):
    suppliers=supplier_repository.select_all()
    product_categories=product_category_repository.select_all()
    manufacturers=manufacturer_repository.select_all()
    products=manufacturer_repository.select_manufacturer(id)
    return render_template("products/index.html", products=products, manufacturers=manufacturers, product_categories=product_categories,suppliers=suppliers)

@manufacturers_blueprint.route("/manufacturers/filter_results", methods=['POST'])
def filter_products():
    manufacturer_id=request.form['manufacturer_id']
    return redirect(f"/manufacturers/{manufacturer_id}/show")