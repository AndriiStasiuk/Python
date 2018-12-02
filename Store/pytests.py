import requests


def test_root():
    test = requests.get('http://127.0.0.1:5000/')
    test.raise_for_status()
    assert test.status_code == 200
    assert not test.is_redirect


def test_fail():
    test = requests.get('http://127.0.0.1:5000/andrii')
    assert test.status_code == 404
    assert not test.is_redirect


def test_register():
    test = requests.post('http://127.0.0.1:5000/register', data=({'password': '123456',
                                                                  'email': 'asjdlfkjsl@sdjfskl.com',
                                                                  'firstName': 'Andrii',
                                                                  'lastName': 'Stasuk',
                                                                  'city': 'Ternopil',
                                                                  'country': 'Ukraine',
                                                                  'phone': '5648953'}))
    test.raise_for_status()
    assert test.status_code == 200
    assert test.text


def test_logout():
    test = requests.get('http://127.0.0.1:5000/logout')
    test.raise_for_status()
    assert test.status_code == 200


def test_removeItem():
    test = requests.get('http://127.0.0.1:5000/removeItem', data=({'productId': 1}))
    test.raise_for_status()
    assert test.status_code == 200


def test_admin():
    test = requests.get('http://127.0.0.1:5000/add')
    test.raise_for_status()
    assert test.status_code == 200


def test_remove():
    test = requests.get('http://127.0.0.1:5000/remove')
    test.raise_for_status()
    assert test.status_code == 200


def test_updateProfile():
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
    test.raise_for_status()
    assert test.status_code == 200


def test_login():
    test = requests.post('http://127.0.0.1:5000/login', data=({'email': 'asjdlfkjsl@sdjfskl.com',
                                                               'password': '123456'}))
    test.raise_for_status()
    assert test.status_code == 200


def test_profileHomeBadRequest():
    test = requests.get('http://127.0.0.1:5000/acount/profile')
    assert test.status_code == 404
