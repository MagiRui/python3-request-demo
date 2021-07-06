import unittest
import json
import requests

class TestUrgePayControllerV2(unittest.TestCase):

    def setUp(self):
        self.headers = {
            'Authorization': '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8'
        }


    def testList(self):

        requestUrl = "http://localhost:8087/v2/xxxxx/list?currentPage=1&pageSize=10&billAge=&realName=%E4%B8%8A%E6%B5%B7&companyName=&username=&channelAgencyId=&repayAccountFrom=&repayAccountTo=&overdueDaysFrom=&overdueDaysTo=&repayTimeFrom=&repayTimeTo=&urgePayTimeFrom=&urgePayTimeTo=&litigationRepay=0&businessMan=&orderByColumns=overdueDays&orderBySeq=asc"

        resp = requests.get(requestUrl, headers=self.headers)
        print(resp.json())

    def testPayDetailGet(self):

        requestUrl = "http://localhost:8087/v2/xxxx/payDetail/xxxx1"

        resp = requests.get(requestUrl, headers=self.headers)
        print(resp.json())