import pdb
from models.product import Product
from models.manufacturer import Manufacturer
from models.product_category import ProductCategory
from models.supplier import Supplier
import repositories.product_repository as product_repository
import repositories.product_category_repository as product_category_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.supplier_repository as supplier_repository

product_category_repository.delete_all()
manufacturer_repository.delete_all()
supplier_repository.delete_all()
product_repository.delete_all()

product_category1=ProductCategory("Nuts")
product_category_repository.save(product_category1)

product_category2=ProductCategory("Fruits")
product_category_repository.save(product_category2)

product_category3=ProductCategory("Hats")
product_category_repository.save(product_category3)

product_category4=ProductCategory("Cheese")
product_category_repository.save(product_category4)

product_category5=ProductCategory("Bags")
product_category_repository.save(product_category5)

product_category6=ProductCategory("Lamps")
product_category_repository.save(product_category6)

manufacturer1=Manufacturer("Londas",123456789,"Tequila Wharf 69")
manufacturer_repository.save(manufacturer1)

manufacturer2=Manufacturer("Salls",987654321,"Harambe Lives 123")
manufacturer_repository.save(manufacturer2)

manufacturer3=Manufacturer("Cap-Trash",832175123,"Bikini Bottom 1")
manufacturer_repository.save(manufacturer3)

manufacturer4=Manufacturer("Yummy-Goo",763453443,"56 Camel Lane")
manufacturer_repository.save(manufacturer4)

manufacturer5=Manufacturer("Nuttin But Nuts",894843982,"22 Saltlake Avenue")
manufacturer_repository.save(manufacturer5)

supplier1=Supplier("Yuko",25,2,10000,1122334455,"221B Baker St")
supplier_repository.save(supplier1)

supplier2=Supplier("Heraz",12,1,0,57483920,"742 Evergreen Terrace")
supplier_repository.save(supplier2)

supplier3=Supplier("Skippio",53,5,2500000,998877665,"79 Springfield lane")
supplier_repository.save(supplier3)

supplier4=Supplier("Zacks",32,3,250000,323454567,"42 Hillbill avenue")
supplier_repository.save(supplier4)

supplier5=Supplier("Freeman Co",19,1,150000,555666444,"32 Wallaby Way Sidney")
supplier_repository.save(supplier5)

product1=Product("Almonds","Africa-Roasted-Salted",350,10000,12000,"12/10/2021-10:53",product_category1,manufacturer1,supplier1)
product_repository.save(product1)

product2=Product("Apples","Spanish-Red",500,5000,7000,"22/11/2021-09:26",product_category2,manufacturer2,supplier1)
product_repository.save(product2)

product3=Product("Pairs","Spanish-Ripe",1000,12000,14000,"23/11/2021-13:46",product_category2,manufacturer2,supplier2)
product_repository.save(product3)

product4=Product("Cowbody-hat","Chinchila-fur/American",10,100000,200000,"12/1/2022-12:33",product_category3,manufacturer3,supplier2)
product_repository.save(product4)

product5=Product("Dried Pinapple","No additives-Brazil",1800,180,300,"27/09/21-13:12",product_category2,manufacturer4,supplier3)
product_repository.save(product5)

product6=Product("Cashew Nuts","American-Dried",189,100000,150000,"14/02/22-07:59",product_category1,manufacturer5,supplier5)
product_repository.save(product6)

product7=Product("Industrial Plastic Bugs","Black-5mm-Extra Large",400,400,800,"23/6/21-12:12",product5,manufacturer2,supplier4)
product_repository.save(product7)












# Filter database by Manufacturer
# Get manufacturer id
# Get manufacturers table id and products foreign key matches
# Send new data list to products/index.html