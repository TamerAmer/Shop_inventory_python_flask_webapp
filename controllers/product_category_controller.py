from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product_category import ProductCategory
import repositories.product_category_repository as product_category_repository
import repositories.product_repository as product_repository

product_categories_blueprint = Blueprint("product_categories", __name__)

@product_categories_blueprint.route("/product_categories")
def product_categories():
    product_categories = product_category_repository.select_all() # NEW
    return render_template("product_categories/index.html", product_categories=product_categories)

@product_categories_blueprint.route("/product_categories/new", methods=['GET'])
def new_task():
    return render_template("product_categories/new.html")

@product_categories_blueprint.route("/product_categories", methods=['POST'])
def create_task():
    name=request.form['name']
    product_category=ProductCategory(name)
    product_category_repository.save(product_category)
    return redirect("/product_categories")