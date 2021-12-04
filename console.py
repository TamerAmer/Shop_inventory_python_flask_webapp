import pdb
from models.product import Product
from models.manufacturer import Manufacturer
from models.product_category import ProductCategory
import repositories.product_repository as product_repository
import repositories.product_category_repository as product_category_repository
import repositories.manufacturer_repository as manufacturer_repository

product_category1=ProductCategory("Nuts")
product_category_repository.save(product_category1)

product_category2=ProductCategory("Fruits")
product_category_repository.save(product_category2)

product_category3=ProductCategory("Hats")
product_category_repository.save(product_category3)

manufacturer1=Manufacturer("Londas",123456789,"Tequila Wharf 69")
manufacturer_repository.save(manufacturer1)

manufacturer2=Manufacturer("Salls",987654321,"Harambe Lives 123")
manufacturer_repository.save(manufacturer2)

manufacturer3=Manufacturer("Cap-Trash",832175123,"Bikini Bottom 1")
manufacturer_repository.save(manufacturer3)

product1=Product("Almonds","Africa-Roasted-Salted",350,10000,12000,"12/10/2021-10:53",product_category1,manufacturer1)
product_repository.save(product1)

product2=Product("Apples","Spanish-Red",500,5000,7000,"22/11/2021-09:26",product_category2,manufacturer2)
product_repository.save(product2)

product3=Product("Pairs","Spanish-Ripe",1000,12000,14000,"23/11/2021-13:46",product_category2,manufacturer2)
product_repository.save(product3)

product4=Product("Cowbody-hat","Chinchila-fur/American",10,100000,200000,"12/1/2022-12:33",product_category3,manufacturer3)
product_repository.save(product4)

