from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product_category import ProductCategory
import repositories.product_category_repository as product_category_repository
import repositories.product_repository as product_repository

product_categories_blueprint = Blueprint("product_categories", __name__)