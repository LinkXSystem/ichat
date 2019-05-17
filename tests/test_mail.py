import unittest
from ichat import Postman
from docs.conf import SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD


class TestMail(unittest.TestCase):

    def test_instance(self):
        instance = Postman(SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD)
        instance.email('linkasde_system@163.com', '微信消息', '功能测试', ['linkasde_system@163.com', 'yz@lejurobot.com'])


if __name__ == '__main__':
    unittest.main()
