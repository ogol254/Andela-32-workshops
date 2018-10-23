from ...db_con import init_db


class Products():
    """docstring for Orsersoperations"""

    def __init__(self):
        self.db = init_db()

    def save(self, name, price, quantity):

        payload = {
            'name': name,
            'price': price,
            'quantity': quantity
        }

        query = """INSERT INTO products (name, price, quantity) VALUES
                (%(name)s, %(price)s, %(quantity)s)"""
        curr = self.db.cursor()
        curr.execute(query, payload)
        self.db.commit()
        return payload

    def getorders(self):

        dbconn = self.db
        curr = dbconn.cursor()
        curr.execute("""SELECT product_id, name, price, quantity FROM products;""")
        data = curr.fetchall()
        resp = []

        for i, items in enumerate(data):
            product_id, name, price, quantity = items
            datar = dict(
                product_id=int(product_id),
                name=name,
                quantity=int(quantity),
                Price=int(price)
            )
            resp.append(datar)
        return resp
