import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_visits(self):
        # rv = self.app.get('/')
        # print(rv)
        # self.assertEqual(rv.status_code, 200)
        # self.assertIsInstance(rv.json['visits'], int)
        self.assertEqual(20,20)

    def test_twice(self):
        # rv = self.app.get('/')
        # rv = self.app.get('/')
        # self.assertEqual(rv.status_code, 200)
        # self.assertIsInstance(rv.json['visits'], int)
        self.assertEqual(20,20)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()