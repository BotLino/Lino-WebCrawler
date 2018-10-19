import json
import pytest
from crawler.populate import getDateRange

JSON_RESULT_CONTENT = [
    {
        "text": "DARCY de 15/10/2018 a 21/10/2018"
    },
    {
        "text": "FCE, FGA e FUP de 15/10/2018 a 21/10/2018"
    },
    {
        "text": "FAL de 15/10/2018 a 19/10/2018"
    }
]

CORRUPTED_JSON = """
    [
        {
            "text": "DARCY de 15/10/2018 a 21/10/2018"
        },
        {
            "text": "FCE, FGA e FUP de 15/10/2018 a 21/10/2018"
        },
        {
            "text": "FAL de 15/10/2018 a 19/10/2018"
        },
        {
            text: wrong text
        }
"""


class TestPopulate():

    def test_get_date_range(self, tmpdir):
        """
        Tests if method gets correct date range from file.
        """
        tmp_file = tmpdir.mkdir("sub").join("test_result.json")
        tmp_json = json.dumps(
            JSON_RESULT_CONTENT,
            indent=4,
            ensure_ascii=False)
        tmp_file.write(tmp_json)
        dates = getDateRange(tmp_file)
        correct_dates = ['15/10/2018', '21/10/2018']
        assert dates == correct_dates

    def test_error_get_date_range(self, tmpdir):
        """
        Tests if method raises exception with corrupted json.
        """
        tmp_file = tmpdir.mkdir("sub").join("test_result.txt")
        tmp_json = json.dumps(
            CORRUPTED_JSON,
            indent=4,
            ensure_ascii=False)
        tmp_file.write(tmp_json)
        with pytest.raises(TypeError):
            getDateRange(tmp_file)
