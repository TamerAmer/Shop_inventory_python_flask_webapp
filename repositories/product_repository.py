from db.run_sql import run_sql
# from models.manufacturer import Manufacturer
from models.product import Product
# from models.product_category import ProductCategory
import repositories.product_category_repository as product_category_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.supplier_repository as supplier_repository

def save(product):
    sql="INSERT INTO products(name, description, quantity, purchase_price, selling_price, date_and_time, manufacturer_id, product_category_id, supplier_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values=[product.name,product.description,product.quantity,product.purchase_price,product.selling_price,product.date_and_time,product.manufacturer.id,product.product_category.id,product.supplier.id]
    results=run_sql(sql,values)
    id=results[0]['id']
    product.id=id
    return product

def return_python_objects(results):
    products=[]
    for row in results:
        supplier=supplier_repository.select(row['supplier_id'])
        manufacturer=manufacturer_repository.select(row['manufacturer_id'])
        product_category=product_category_repository.select(row['product_category_id'])
        product=Product(row['name'],row['description'],row['quantity'],"{:.2f}".format(int(row['purchase_price'])/100),"{:.2f}".format(int(row['selling_price'])/100),row['date_and_time'],product_category, manufacturer, supplier,row['id'])
        products.append(product)
    return products


def select_all():
    products=[]
    sql="SELECT * FROM products"
    results=run_sql(sql)
    for row in results:
        supplier=supplier_repository.select(row['supplier_id'])
        manufacturer=manufacturer_repository.select(row['manufacturer_id'])
        product_category=product_category_repository.select(row['product_category_id'])
        product=Product(row['name'],row['description'],row['quantity'],"{:.2f}".format(int(row['purchase_price'])/100),"{:.2f}".format(int(row['selling_price'])/100),row['date_and_time'],product_category, manufacturer, supplier,row['id'])
        products.append(product)
    return(products)

def delete_all():
    sql="DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql="DELETE FROM products WHERE id=%s"
    values=[id]
    run_sql(sql,values)

def select(id):
    product=None
    sql="SELECT * FROM products WHERE id=%s"
    values=[id]
    results=run_sql(sql,values)[0]
    if results is not None:
        supplier=supplier_repository.select(results['supplier_id'])
        manufacturer=manufacturer_repository.select(results['manufacturer_id'])
        product_category=product_category_repository.select(results['product_category_id'])
        product=Product(results['name'],results['description'],results['quantity'],results['purchase_price'],results['selling_price'],results['date_and_time'],product_category,manufacturer,supplier,results['id'])
    return product

def update(product):
    sql="UPDATE products SET (name,description,quantity,purchase_price,selling_price,date_and_time,product_category_id,manufacturer_id,supplier_id) = (%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE id=%s"
    values=[product.name,product.description,product.quantity,product.purchase_price,product.selling_price,product.date_and_time,product.product_category.id,product.manufacturer.id,product.supplier.id,product.id]
    run_sql(sql,values)

def sort_by_category():  
    sql="SELECT * FROM products INNER JOIN product_categories ON products.product_category_id = product_categories.id ORDER BY product_categories.name"
    products=[]
    results=run_sql(sql)
    for row in results:
        supplier=supplier_repository.select(row['supplier_id'])
        manufacturer=manufacturer_repository.select(row['manufacturer_id'])
        product_category=product_category_repository.select(row['product_category_id'])
        product=Product(row['name'],row['description'],row['quantity'],"{:.2f}".format(int(row['purchase_price'])/100),"{:.2f}".format(int(row['selling_price'])/100),row['date_and_time'],product_category, manufacturer, supplier,row['id'])
        products.append(product)
    return products

def sort_by_category_desc():
    sql="SELECT * FROM products INNER JOIN product_categories ON products.product_category_id = product_categories.id ORDER BY product_categories.name DESC"
    results=run_sql(sql)
    return return_python_objects(results)

def sort_by_name():
    sql="SELECT * FROM products ORDER BY products.name"
    results=run_sql(sql)
    return return_python_objects(results)

def sort_by_name_desc():
    sql="SELECT * FROM products ORDER BY products.name DESC"
    results=run_sql(sql)
    return return_python_objects(results)

def sort_by_supplier():
    sql="SELECT * FROM products INNER JOIN suppliers ON products.supplier_id = suppliers.id ORDER BY suppliers.name"
    results=run_sql(sql)
    return return_python_objects(results)

def sort_by_supplier_desc():
    sql="SELECT * FROM products INNER JOIN suppliers ON products.supplier_id = suppliers.id ORDER BY suppliers.name DESC"
    results=run_sql(sql)
    return return_python_objects(results)

def sort_by_manufacturer():
    sql="SELECT * FROM products INNER JOIN manufacturers ON products.manufacturer_id = manufacturers.id ORDER BY manufacturers.name"
    results=run_sql(sql)
    return return_python_objects(results)

def sort_by_manufacturer_desc():
    sql="SELECT * FROM products INNER JOIN manufacturers ON products.manufacturer_id = manufacturers.id ORDER BY manufacturers.name DESC"
    results=run_sql(sql)
    return return_python_objects(results)
