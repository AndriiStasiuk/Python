import main
import unittest
import requests


class FlaskTestCase(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(main.parse([1, 2, 3, 4, 5, 6, 7]), [[1, 2, 3, 4, 5, 6, 7]])

    def test_root(self):
        test = requests.get('http://127.0.0.1:5000/')
        return self.assertEqual(test.status_code, 200)

    def test_fail(self):
        test = requests.get('http://127.0.0.1:5000/andrii')
        return self.assertEqual(test.status_code, 404)

    def test_register(self):
        test = requests.post('http://127.0.0.1:5000/register', data=({'password': '123456',
                                                                      'email': 'asjdlfkjsl@sdjfskl.com',
                                                                      'firstName': 'Andrii',
                                                                      'lastName': 'Stasuk',
                                                                      'city': 'Ternopil',
                                                                      'country': 'Ukraine',
                                                                      'phone': '5648953'}))
        return self.assertEqual(test.status_code, 200)

    def test_logout(self):
        test = requests.get('http://127.0.0.1:5000/logout')
        return self.assertEqual(test.status_code, 200)

    def test_removeItem(self):
        test = requests.get('http://127.0.0.1:5000/removeItem', data=({'productId': 1}))
        return self.assertEqual(test.status_code, 200)

    def test_admin(self):
        test = requests.get('http://127.0.0.1:5000/add')
        return self.assertEqual(test.status_code, 200)

    def test_remove(self):
        test = requests.get('http://127.0.0.1:5000/remove')
        return self.assertEqual(test.status_code, 200)

    def test_updateProfile(self):
        test = requests.post('http://127.0.0.1:5000/updateProfile', data=({'email': 'asjdlfkjsl@sdjfskl.com',
                                                                           'firstName': 'Andrii',
                                                                           'lastName': 'Stasuk',
                                                                           'address1': 'Lviv',
                                                                           'address2': 'Kyiv',
                                                                           'zipcode': '0129',
                                                                           'city': 'Lviv',
                                                                           'state': 'Lviv',
                                                                           'country': 'Ukraine',
                                                                           'phone': '096977555'}))
        return self.assertEqual(test.status_code, 200)

    def test_login(self):
        test = requests.post('http://127.0.0.1:5000/login', data=({'email': 'asjdlfkjsl@sdjfskl.com',
                                                                   'password': '123456'}))
        return self.assertEqual(test.status_code, 200)

    def test_profileHomeBadRequest(self):
        test = requests.get('http://127.0.0.1:5000/acount/profile')
        return self.assertEqual(test.status_code, 404)


if __name__ == '__main__':
    unittest.main()
