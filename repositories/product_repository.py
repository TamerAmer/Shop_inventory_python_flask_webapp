from db.run_sql import run_sql
# from models.manufacturer import Manufacturer
from models.product import Product
# from models.product_category import ProductCategory
import repositories.product_category_repository as product_category_repository
import repositories.manufacturer_repository as manufacturer_repository

def save(product):
    sql="INSERT INTO products(name, description, quantity, purchase_price, selling_price, date_and_time, manufacturer_id, product_category_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values=[product.name,product.description,product.quantity,product.purchase_price,product.selling_price,product.date_and_time,product.manufacturer.id,product.product_category.id]
    results=run_sql(sql,values)
    id=results[0]['id']
    product.id=id
    return product

def select_all():
    products=[]
    sql="SELECT * FROM products"
    results=run_sql(sql)
    for row in results:
        manufacturer=manufacturer_repository.select(row['manufacturer_id'])
        product_category=product_category_repository.select(row['product_category_id'])
        product=Product(row['name'],row['description'],row['quantity'],row['purchase_price'],row['selling_price'],row['date_and_time'],product_category, manufacturer,row['id'])
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
        manufacturer=manufacturer_repository.select(results['manufacturer_id'])
        product_category=product_category_repository.select(results['product_category_id'])
        product=Product(results['name'],results['description'],results['quantity'],results['purchase_price'],results['selling_price'],results['date_and_time'],manufacturer,product_category,results['id'])
    return product

def update(product):
    sql="UPDATE products SET (name,description,quantity,purchase_price,selling_price,date_and_time,product_category_id,manufacturer_id) = (%s,%s,%s,%s,%s,%s,%s,%s) WHERE id=%s"
    values=[product.name,product.description,product.quantity,product.purchase_price,product.selling_price,product.date_and_time,product.product_category.id,product.manufacturer.id,product.id]
    run_sql(sql,values)