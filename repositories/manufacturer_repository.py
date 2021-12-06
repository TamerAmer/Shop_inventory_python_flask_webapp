from db.run_sql import run_sql
from models.manufacturer import Manufacturer
import repositories.product_category_repository as product_category_repository
from models.product import Product

def save(manufacturer):
    sql="INSERT INTO manufacturers(name,telephone_number,address) VALUES (%s,%s,%s) RETURNING *"
    values=[manufacturer.name,manufacturer.telephone_number,manufacturer.address]
    result=run_sql(sql,values)
    manufacturer.id=result[0]['id']
    return manufacturer

def select_all():
    manufacturers=[]
    sql="SELECT * FROM manufacturers"
    resuslts=run_sql(sql)
    for row in resuslts:
        manufacturer=Manufacturer(row['name'],row['telephone_number'],row['address'],row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer=None
    sql="SELECT * FROM manufacturers WHERE id=%s"
    values=[id]
    results=run_sql(sql,values)[0]
    if results is not None:
        manufacturer=Manufacturer(results['name'],results['telephone_number'],results['address'],results['id'])
    return manufacturer

def delete_all():
    sql="DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql="DELETE FROM manufacturers WHERE id=%s"
    values=[id]
    run_sql(sql,values)

def update(manufacturer):
    sql="UPDATE manufacturers SET (name,telephone_number,address)=(%s,%s,%s) WHERE id=%s"
    values=[manufacturer.name,manufacturer.telephone_number,manufacturer.address,manufacturer.id]
    run_sql(sql,values)

def select_manufacturer(id):
    products=[]
    sql="SELECT * FROM products WHERE manufacturer_id=%s"
    values=[id]
    results=run_sql(sql,values)
    for row in results:
        manufacturer=select(row['manufacturer_id'])
        product_category=product_category_repository.select(row['product_category_id'])
        product=Product(row['name'],row['description'],row['quantity'],row['purchase_price'],row['selling_price'],row['date_and_time'],product_category, manufacturer,row['id'])
        products.append(product)
    return products