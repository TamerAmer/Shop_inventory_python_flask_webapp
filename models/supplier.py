class Supplier:
    def __init__(self,name,total_orders,pending_orders,outstanding_balance,telephone_number,address,id=None):
        self.name=name
        self.total_orders=total_orders
        self.pending_order=pending_orders
        self.outstanding_balance=outstanding_balance
        self.telephone_number=telephone_number
        self.address=address
        self.id=id