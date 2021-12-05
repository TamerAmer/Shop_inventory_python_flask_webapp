from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_category_repository as product_category_repository

products_blueprint = Blueprint("products", __name__)


@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)


@products_blueprint.route("/products/new")
def new_task():
    product_categories = product_category_repository.select_all()
    manufacturers = manufacturer_repository.select_all()
    return render_template(
        "products/new.html",
        product_categories=product_categories,
        manufacturers=manufacturers
    )


@products_blueprint.route("/products", methods=['POST'])
def create_task():
    manufacturer_id = request.form["manufacturer_id"]
    product_category_id = request.form["product_category_id"]
    print(manufacturer_id)
    print(product_category_id)
    name = request.form["name"]
    description = request.form["description"]
    quantity = request.form["quantity"]
    purchase_price = request.form["purchase_price"]
    selling_price = request.form["selling_price"]
    date_and_time = request.form["date_and_time"]
    manufacturer = manufacturer_repository.select(int(manufacturer_id))
    product_category = product_category_repository.select(int(product_category_id))
    product = Product(
        name,
        description,
        quantity,
        purchase_price,
        selling_price,
        date_and_time,
        product_category,
        manufacturer
    )
    product_repository.save(product)
    return redirect("/products")
