import json
import pytest
import mongomock
from datetime import datetime
from pymongo import MongoClient
from freezegun import freeze_time
from populate import getDateRange, genDatesList,\
    genWeekMenuObj, saveMenu


class TestPopulate():

    @freeze_time('2018-10-19')
    def test_get_date_range(self, tmpdir, json_result_content):
        """
        Tests if method gets correct date range from file.
        """
        tmp_file = tmpdir.mkdir("sub").join("test_result.json")
        tmp_json = json.dumps(
            json_result_content,
            indent=4,
            ensure_ascii=False)
        tmp_file.write(tmp_json)
        dates = getDateRange(tmp_file)
        correct_dates = ['15/10/2018', '21/10/2018']
        assert dates == correct_dates

    def test_error_get_date_range(self, tmpdir, corrupted_json):
        """
        Tests if method raises exception with corrupted json.
        """
        tmp_file = tmpdir.mkdir("sub").join("test_result.txt")
        tmp_json = json.dumps(
            corrupted_json,
            indent=4,
            ensure_ascii=False)
        tmp_file.write(tmp_json)
        with pytest.raises(TypeError):
            getDateRange(tmp_file)

    def test_gen_dates_list(self):
        """
        Tests if method generates a correct list of dates.
        """
        dates = genDatesList('15/10/2018', '21/10/2018')
        correct_dates = ['15/10/2018', '16/10/2018',
                         '17/10/2018', '18/10/2018',
                         '19/10/2018', '20/10/2018', '21/10/2018']
        assert dates == correct_dates

    def test_bad_range_gen_dates_list(self):
        """
        Test if method returns empty list on bad range parameters.
        """
        dates = genDatesList('21/10/2018', '01/10/2018')
        assert dates == []

    def test_malformed_dates(self):
        """
        Tests if method raises exception on malformed date parameters
        """
        with pytest.raises(ValueError):
            genDatesList('151/02/018', '211/02/018')

    def test_gen_week_obj(self, json_week_menu):
        """
        Tests if method generates the object with required fields.
        """
        dates = genDatesList('15/10/2018', '21/10/2018')
        weekMenu = genWeekMenuObj(dates, json_week_menu)
        assert 'menu' in weekMenu
        assert 'dates' in weekMenu

    @freeze_time('2018-10-19')
    @mongomock.patch(servers='localhost', on_new='error')
    def test_save_menu(self, tmpdir, json_week_menu, json_result_content):
        client = MongoClient('localhost')
        collection = client.ru.menu
        tmp_file = tmpdir.join('test_weekMenu.json')
        tmp_json = json.dumps(
            json_week_menu,
            indent=4,
            ensure_ascii=False)
        tmp_file.write(tmp_json)
        dates_path = tmpdir.join('result.json')
        tmp_dates = json.dumps(
            json_result_content,
            indent=4,
            ensure_ascii=False)
        dates_path.write(tmp_dates)
        dates = genDatesList('15/10/2018', '21/10/2018')
        weekObj = genWeekMenuObj(dates, json_week_menu)
        saveMenu(tmp_file, dates_path)
        today = datetime.today().strftime('%d/%m/%Y')
        cursor = collection.find({'dates': today}, {'_id': 0})
        print(cursor)
        for document in cursor:
            assert document == weekObj
