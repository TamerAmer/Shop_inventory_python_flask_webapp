from db.run_sql import run_sql
from models.product import Product
from models.supplier import Supplier
import repositories.product_category_repository as product_category_repository
import repositories.manufacturer_repository as manufacturer_repository

def save(supplier):
    sql="INSERT INTO suppliers(name,total_orders,pending_orders,outstanding_balance,telephone_number,address) VALUES (%s,%s,%s,%s,%s,%s) RETURNING *"
    values=[supplier.name,supplier.total_orders,supplier.pending_orders,supplier.outstanding_balance,supplier.telephone_number,supplier.address]
    results=run_sql(sql,values)
    supplier.id=results[0]['id']
    return supplier

def select_all():
    suppliers=[]
    sql="SELECT * FROM suppliers"
    results=run_sql(sql)
    for row in results:
        supplier=Supplier(row['name'],row['total_orders'],row['pending_orders'],"{:.2f}".format(int(row['outstanding_balance'])/100),row['telephone_number'],row['address'],row['id'])
        suppliers.append(supplier)
    return suppliers

def delete_all():
    sql="DELETE FROM suppliers"
    run_sql(sql)

def delete(id):
    sql="DELETE FROM suppliers WHERE id=%s"
    values=[id]
    run_sql(sql,values)

def select(id):
    supplier=None
    sql="SELECT * FROM suppliers WHERE id=%s"
    values=[id]
    results=run_sql(sql,values)[0]
    if results is not None:
        supplier=Supplier(results['name'],results['total_orders'],results['pending_orders'],"{:.2f}".format(int(results['outstanding_balance'])/100),results['telephone_number'],results['address'],results['id'])
    return supplier

def update(supplier):
    sql="UPDATE suppliers  SET (name,total_orders,pending_orders,outstanding_balance,telephone_number,address) = (%s,%s,%s,%s,%s,%s) WHERE id=%s"
    values=[supplier.name,supplier.total_orders,supplier.pending_orders,supplier.outstanding_balance,supplier.telephone_number,supplier.address,supplier.id]
    run_sql(sql,values)

def select_category(id):
    products=[]
    sql="SELECT * FROM products WHERE supplier_id=%s"
    values=[id]
    results=run_sql(sql,values)
    for row in results:
        manufacturer=manufacturer_repository.select(row['manufacturer_id'])
        product_category=product_category_repository.select(row['product_category_id'])
        supplier=select(row['supplier_id'])
        product=Product(row['name'],row['description'],row['quantity'],"{:.2f}".format(int(row['purchase_price'])/100),"{:.2f}".format(int(row['selling_price'])/100),row['date_and_time'],product_category, manufacturer,supplier,row['id'])
        products.append(product)
    return products
