import unittest
from run import app
import json


class TestOrder(unittest.TestCase):
    """docstring for TestOrder"""

    def setup(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
            "item 1": "Infinix",
            "item 2": "Data",
            "price": 20000
        }

    def test_post_order(self):
        response = self.app.post('/api/v1/orders', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], "Success")
        self.assertEqual(response.status_code, 201)

    def teardown(self):
        pass


if __name__ == '__main__':
    unittest.main()
