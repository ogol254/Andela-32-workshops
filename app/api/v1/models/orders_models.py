orders = []


class OrdersOperations():
    """docstring for Orsersoperations"""

    def __init__(self):
        self.orders = orders

    def save(self, item1, item2, price):

        payload = {
            'id': len(orders) + 1,
            'Description': {'Item 1': item1, 'Item 2': item2},
            'Price': price
        }

        self.orders.append(payload)

        return self.orders

    def getorders(self):
        return self.orders

    def getone(self, id):
        for order in self.orders:
            if(order['id'] == id):
                return orders

        return "No such Order"
