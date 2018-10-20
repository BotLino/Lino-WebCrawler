import mongomock
from server import getMenu
from pymongo import MongoClient
from freezegun import freeze_time


class TestServer():
    @freeze_time('2018-10-19')
    @mongomock.patch(servers='localhost', on_new='error')
    def test_update_database(self, test_client):
        res = test_client.get('/cardapio/update')
        assert res.status_code == 200

    @freeze_time('2018-10-19')
    @mongomock.patch(servers='localhost', on_new='error')
    def test_get_menu(self, test_client, db_example):
        client = MongoClient('localhost')
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        test_menu = getMenu()
        assert test_menu == db_example['menu']

    @freeze_time('2018-10-19')
    @mongomock.patch(servers='localhost', on_new='error')
    def test_error_empty_db(self):
        client = MongoClient('localhost')
        collection = client.ru.menu
        collection.drop()
        test_menu = getMenu()
        assert test_menu is None
