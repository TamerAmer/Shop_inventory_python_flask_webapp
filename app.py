from flask import Flask, render_template

from controllers.manufacturer_controller import manufacturers_blueprint
from controllers.product_category_controller import product_categories_blueprint
from controllers.product_controller import products_blueprint
from controllers.supplier_controller import suppliers_blueprint
import repositories.product_category_repository as product_category_repository

app = Flask(__name__)

app.register_blueprint(suppliers_blueprint)
app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(product_categories_blueprint)
app.register_blueprint(products_blueprint)


@app.route('/')
def home():
    product_categories=product_category_repository.select_all()
    return render_template('index.html',product_categories=product_categories)

if __name__ == '__main__':
    app.run(debug=True)