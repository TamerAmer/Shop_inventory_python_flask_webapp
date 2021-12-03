from db.run_sql import run_sql
from models.manufacturer import Manufacturer

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
        manufacturer=Manufacturer(row['name'],row['telephone_number'],row['address'])
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
    sql="DELETE * FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql="DELETE * FROM manufacturers WHERE id=%s"
    values=[id]
    run_sql(sql,values)