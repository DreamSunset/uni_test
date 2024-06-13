import unittest
import requests

class TestBaiduMapAPI(unittest.TestCase):

    def setUp(self):
        # 设置API Key和基础URL
        self.api_key = 'ec7mfrYmlcnP4l9Y0iftCnJt17BBinPj'
        self.base_url = 'https://api.map.baidu.com/place/v2/search'

    def test_geocoding_success(self):
        # 测试成功的地理请求
        params = {
            'query': '南京航空航天大学',
            'region': '南京',
            'city_limit': 'true',
            'output': 'json',
            'ak': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 0)
        self.assertIn('results', data)
        # 确保返回的是列表
        self.assertIsInstance(data['results'], list)
        # 检查列表中的每个元素是否包含'name'键
        for item in data['results']:
            self.assertIn('name', item)
        for item in data['results']:
            print(f"搜索结果: {item['name']}")

    def test_geocoding_invalid_key(self):
        # 测试使用无效API Key的请求
        params = {
            'address': '南京航空航天大学将军路校区',
            'output': 'json',
            'ak': 'invalid_api_key'
        }
        response = requests.get(self.base_url, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertNotEqual(data['status'], 0)
        print(f"返回码200，无效AK例子成功识别")

    def test_geocoding_invalid_address(self):
        # 测试使用无效地址的请求
        params = {
            'address': '这是一个无效的地址',
            'output': 'json',
            'ak': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertNotEqual(data['status'], 0)
        print(f"无效地址例子成功识别")


if __name__ == '__main__':
    unittest.main()
