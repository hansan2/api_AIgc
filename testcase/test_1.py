import unittest
import json
import requests
from tools.handler_sign import HandlerSign

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.device_id = "uCode_06377883b20734f2"
        self.sign = HandlerSign(self.device_id).sign_rand()
        self.app_id = "980020029"
        self.headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "X-Ubt-Appid": self.app_id,
            "X-Ubt-Deviceid": self.device_id,
            "X-Ubt-Sign": self.sign
        }

    def test_something(self):
        self.data = {
            "content": "前进50米",
            "deviceId": self.device_id,
            "language": ""
        }
        rsp = requests.post(
            url="https://test79.ubtrobot.com/ai-engine/llm/chat", json=self.data, headers=self.headers)
        print(rsp.text)
        data = {
            "Action": {
                "logic": "serial",
                "motion": [
                    {
                        "direction": "forward",
                        "distance": "50"
                    }
                ]
            }
        }
        json_str = json.dumps(data)
        self.assertIn("forward",rsp.text)
        #self.assertEqual(rsp.status_code, 210)  # add assertion here


if __name__ == '__main__':
    unittest.main()
