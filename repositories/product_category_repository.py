from db.run_sql import run_sql
from models.product_category import ProductCategory
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.supplier_repository as supplier_repository

def save(product_category):
    sql="INSERT INTO product_categories(name) VALUES (%s) RETURNING *"
    values=[product_category.name]
    results=run_sql(sql,values)
    product_category.id=results[0]['id']
    return product_category

def select_all():
    product_categories=[]
    sql="SELECT * FROM product_categories"
    results=run_sql(sql)
    for row in results:
        product_category=ProductCategory(row['name'],row['id'])
        product_categories.append(product_category)
    return product_categories

def delete_all():
    sql="DELETE FROM product_categories"
    run_sql(sql)

def delete(id):
    sql="DELETE FROM product_categories WHERE id=%s"
    values=[id]
    run_sql(sql,values)

def select(id):
    product_category=None
    sql="SELECT * FROM product_categories WHERE id=%s"
    values=[id]
    results=run_sql(sql,values)[0]
    if results is not None:
        product_category=ProductCategory(results['name'],results['id'])
    return product_category

def update(product_category):
    sql="UPDATE product_categories  SET name = %s WHERE id=%s"
    values=[product_category.name,product_category.id]
    run_sql(sql,values)

def select_category(id):
    products=[]
    sql="SELECT * FROM products WHERE product_category_id=%s"
    values=[id]
    results=run_sql(sql,values)
    for row in results:
        supplier=supplier_repository.select(row['supplier_id'])
        manufacturer=manufacturer_repository.select(row['manufacturer_id'])
        product_category=select(row['product_category_id'])
        product=Product(row['name'],row['description'],row['quantity'],"{:.2f}".format(int(row['purchase_price'])/100),"{:.2f}".format(int(row['selling_price'])/100),row['date_and_time'],product_category, manufacturer,supplier,row['id'])
        products.append(product)
    return products
