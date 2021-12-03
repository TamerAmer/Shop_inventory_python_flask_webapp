from db.run_sql import run_sql
from models.product_category import ProductCategory

def save(product_category):
    sql="INSERT INTO product_categories(name) VALUES (%s) RETURNING *"
    values=[product_category.name]
    results=run_sql(sql,values)
    product_category.id=results[0]['name']
    return product_category

def select_all():
    product_categories=[]
    sql="SELECT * FROM product_categories"
    results=run_sql(sql)
    for row in results:
        product_category=ProductCategory(row['name'])
        product_categories.append(product_category)
    return product_categories

def delete_all():
    sql="DELETE * FROM product_categories"
    run_sql(sql)

def delete(id):
    sql="DELETE * FROM product_categories WHERE id=%s"
    values=[id]
    run_sql(sql,values)

def select(id):
    product_category=None
    sql="SELECT * FROM product categories WHERE id=%s"
    values=[id]
    results=run_sql(sql,values)
    if results is not None:
        product_category=ProductCategory(results['name'],results['id'])
    return product_category

