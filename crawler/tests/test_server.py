import mongomock
import json
from server import getMenu, isValidDay
from pymongo import MongoClient
from freezegun import freeze_time
import os

DB_URI = os.getenv('DB_URI', "localhost")


class TestServer():
    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_update_database(self, test_client):
        try:
            res = test_client.get('/cardapio/update')
            assert res.status_code == 200
        except Exception as e:
            res = test_client.get('/cardapio/update')
            assert res.status_code == 502

    def test_is_valid_day(self):
        assert isValidDay('Wednesday') is True

    def test_bad_is_valid_day(self):
        assert isValidDay('MisspelledWednesday') is False

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_get_menu(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        test_menu = getMenu()
        assert test_menu == db_example['menu']

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_error_empty_db(self):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.drop()
        test_menu = getMenu()
        assert test_menu is None

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_get_week_menu(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        res = test_client.get('/cardapio/week')
        data = json.loads(res.get_data(as_text=True))
        assert data == db_example['menu']

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_get_day_menu(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        res = test_client.get('/cardapio/Wednesday')
        data = json.loads(res.get_data(as_text=True))
        assert data == db_example['menu']['Wednesday']

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_bad_get_day_menu(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        res = test_client.get('/cardapio/MisspelledDay')
        data = json.loads(res.get_data(as_text=True))
        assert res.status_code == 400
        assert data['status'] == 'error'

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_get_day_lunch(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        res = test_client.get('/cardapio/Wednesday/Almoco')
        data = json.loads(res.get_data(as_text=True))
        assert res.status_code == 200
        assert data == db_example['menu']['Wednesday']['ALMOÇO']

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_bad_get_day_lunch(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        res = test_client.get('/cardapio/MisspelledDay/Almoco')
        data = json.loads(res.get_data(as_text=True))
        assert res.status_code == 400
        assert data['status'] == 'error'

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_get_day_break_fast(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        res = test_client.get('/cardapio/Wednesday/Desjejum')
        data = json.loads(res.get_data(as_text=True))
        assert res.status_code == 200
        assert data == db_example['menu']['Wednesday']['DESJEJUM']

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_bad_get_day_break_fast(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        res = test_client.get('/cardapio/MisspelledDay/Desjejum')
        data = json.loads(res.get_data(as_text=True))
        assert res.status_code == 400
        assert data['status'] == 'error'

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_get_day_dinner(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        res = test_client.get('/cardapio/Wednesday/Jantar')
        data = json.loads(res.get_data(as_text=True))
        assert res.status_code == 200
        assert data == db_example['menu']['Wednesday']['JANTAR']

    @freeze_time('2018-10-19')
    @mongomock.patch(servers=DB_URI, on_new='error')
    def test_bad_get_day_dinner(self, test_client, db_example):
        client = MongoClient(DB_URI)
        collection = client.ru.menu
        collection.replace_one(
            {'dates': db_example['dates']},
            db_example,
            upsert=True)
        res = test_client.get('/cardapio/MisspelledDay/Jantar')
        data = json.loads(res.get_data(as_text=True))
        assert res.status_code == 400
        assert data['status'] == 'error'

    @freeze_time('2018-10-19')
    def test_get_pdf(self, test_client, json_result_content):
        res = test_client.get('/cardapio/pdf')
        assert res.status_code == 200
