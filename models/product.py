class Product:
    def __init__(self,name,description,quantity,purchase_price,selling_price,date_and_time,product_category,manufacturer,supplier="x",id=None):
        self.name=name
        self.description=description
        self.quantity=quantity
        self.purchase_price=purchase_price
        self.selling_price=selling_price
        self.date_and_time=date_and_time
        self.product_category=product_category
        self.manufacturer=manufacturer
        self.supplier=supplier
        self.id=id
