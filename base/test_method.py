# coding=utf-8
import unittest
from base.demo import RunMain
import json
from mock import mock
from base.mock_demo import mock_test
import HTMLTestRunner


class TestMethod(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("类执行之前的方法")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("类执行之后的方法")

    def setUp(self):
        print("test-->setup")
        self.run = RunMain(url='http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?char=11', method="POST")
        # self.run = RunMain()
        # self.userid = self.test_01()

    # def tearDown(self):
    #     print("test-->tearDown")

    def test_01(self):
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?char=11'
        data = {
            'timestamp': '1507006626132',
            'uid': '5249191',
            'uuid': '5ea7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '0b4c502ba647664be04dfedb32ad4f3d',
            'cid': '0',
            'errorCode': 1006
        }
        # mock_data = mock.Mock(return_value=data)
        # print(mock_data)
        # self.run.run_main = mock_data
        res = mock_test(self.run.run_main, data, url, "POST", data)
        # res = self.run.run_main(url, 'POST', data)
        # res = json.loads(res)
        print(res)
        # self.assertEqual(res['data']['errorCode'], 1006, "测试失败")
        self.assertEqual(res['errorCode'], 1006, "测试失败")
        # self.userid = 10002
        # return self.userid
        globals()['userid'] = '1000909'
        print('这是第一个case')

    # @unittest.skip('test_02')
    def test_02(self):
        # print(userid)
        url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?char=11'
        data = {
            'timestamp': '1507006626132',
            'uid': '5249192',
            'uuid': '5ea7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '0b4c502ba647664be04dfedb32ad4f3d',
            'cid': '0'
        }
        res = self.run.run_main(url, 'POST', data)
        print(type(res))
        res = json.loads(res)
        print(res)
        self.assertEqual(res['data']['errorCode'], 1006, "测试失败")
        # print(self.userid)
        print('这是第二个case')


if __name__ == "__main__":
    # filepath = "../report/htmlreport.html"
    # fp = open(filepath, 'wb')
    # suite = unittest.TestSuite()
    # suite.addTest(TestMethod('test_01'))
    # suite.addTest(TestMethod('test_02'))
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is first report')
    # runner.run(suite)
    unittest.main()
    # unittest.TextTestRunner().run(suite)
