from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository
import repositories.manufacturer_repository as manufacturer_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all() # NEW
    return render_template("suppliers/index.html", suppliers=suppliers)

@suppliers_blueprint.route("/suppliers/new", methods=['GET'])
def new_supplier():
    return render_template("suppliers/new.html")

@suppliers_blueprint.route("/suppliers", methods=['POST'])
def create_supplier():
    name=request.form['name']
    total_orders=request.form['total_orders']
    pending_orders=request.form['pending_orders']
    outstanding_balance=request.form['outstanding_balance']
    telephone_number=request.form['thelephone_number']
    address=request.form['address']
    supplier=Supplier(name,total_orders,pending_orders,outstanding_balance,telephone_number,address)
    supplier_repository.save(supplier)
    return redirect("/suppliers")

@suppliers_blueprint.route("/suppliers/<id>/edit")
def edit_supplier(id):
    supplier=supplier_repository.select(id)
    return render_template("suppliers/edit.html", supplier=supplier)

@suppliers_blueprint.route("/suppliers/<id>", methods=['POST'])
def update_supplier(id):
    name=request.form['name']
    total_orders=request.form['total_orders']
    pending_orders=request.form['pending_orders']
    outstanding_balance=request.form['outstanding_balance']
    telephone_number=request.form['thelephone_number']
    address=request.form['address']
    supplier=Supplier(name,total_orders,pending_orders,outstanding_balance,telephone_number,address,id)
    supplier_repository.update(supplier)
    return redirect("/suppliers")

@suppliers_blueprint.route("/suppliers/<id>")
def show_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template('suppliers/show.html', supplier=supplier)

@suppliers_blueprint.route("/suppliers/<id>/delete")
def delete_supplier(id):
    supplier_repository.delete(id)
    return redirect("/suppliers")

@suppliers_blueprint.route("/suppliers/<id>/show")
def show_products(id):
    manufacturers=manufacturer_repository.select_all()
    suppliers=supplier_repository.select_all()
    products=supplier_repository.select_category(id)
    return render_template("products/index.html", products=products,suppliers=suppliers,manufacturers=manufacturers)

@suppliers_blueprint.route("/suppliers/filter_results", methods=['POST'])
def filter_products():
    supplier_id=request.form['supplier_id']
    return redirect(f"/suppliers/{supplier_id}/show")