import unittest
import requests
import json

class TestAchievementIncomeDataStatisticsController(unittest.TestCase):

    def setUp(self):

        self.headers = {
            'Authorization': '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8'
        }

    def testQueryData(self):

        requestUrl = "http://localhost:8087/xxxxxxx/list/2/1"
        requestData = {"startYearMonth":"2020-02"}
        resp = requests.post(requestUrl, headers=self.headers, data=json.dumps(requestData, ensure_ascii=False).encode("utf-8"))
        print(resp.json())