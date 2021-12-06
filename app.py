from flask import Flask, render_template

from controllers.manufacturer_controller import manufacturers_blueprint
from controllers.product_category_controller import product_categories_blueprint
from controllers.product_controller import products_blueprint
from controllers.supplier_controller import suppliers_blueprint

app = Flask(__name__)

app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(product_categories_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(suppliers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)