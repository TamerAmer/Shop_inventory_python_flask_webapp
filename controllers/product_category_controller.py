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