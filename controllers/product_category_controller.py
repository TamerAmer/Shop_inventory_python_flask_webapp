from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product_category import ProductCategory
import repositories.product_category_repository as product_category_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.supplier_repository as supplier_repository

product_categories_blueprint = Blueprint("product_categories", __name__)

@product_categories_blueprint.route("/product_categories")
def product_categories():
    product_categories = product_category_repository.select_all() # NEW
    return render_template("product_categories/index.html", product_categories=product_categories)

@product_categories_blueprint.route("/product_categories/new", methods=['GET'])
def new_product_category():
    return render_template("product_categories/new.html")

@product_categories_blueprint.route("/product_categories", methods=['POST'])
def create_product_category():
    name=request.form['name']
    product_category=ProductCategory(name)
    product_category_repository.save(product_category)
    return redirect("/product_categories")

@product_categories_blueprint.route("/product_categories/<id>/edit")
def edit_product_category(id):
    product_category=product_category_repository.select(id)
    return render_template("product_categories/edit.html", product_category=product_category)

@product_categories_blueprint.route("/product_categories/<id>", methods=['POST'])
def update_product_category(id):
    name=request.form['name']
    product_category=ProductCategory(name,id)
    product_category_repository.update(product_category)
    print(product_category.name,product_category.id)
    return redirect("/product_categories")

@product_categories_blueprint.route("/product_categories/<id>")
def show_product_category(id):
    product_category = product_category_repository.select(id)
    return render_template('product_categories/show.html', product_category=product_category)

@product_categories_blueprint.route("/product_categories/<id>/delete")
def delete_product_category(id):
    product_category_repository.delete(id)
    return redirect("/product_categories")

@product_categories_blueprint.route("/product_categories/<id>/show")
def show_products(id):
    suppliers=supplier_repository.select_all()
    manufacturers=manufacturer_repository.select_all()
    product_categories=product_category_repository.select_all()
    products=product_category_repository.select_category(id)
    return render_template("products/index.html", products=products,product_categories=product_categories,manufacturers=manufacturers,suppliers=suppliers)

@product_categories_blueprint.route("/product_categories/filter_results", methods=['POST'])
def filter_products():
    product_category_id=request.form['product_category_id']
    return redirect(f"/product_categories/{product_category_id}/show")
