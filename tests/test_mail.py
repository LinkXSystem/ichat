import unittest
from ichat import Postman

host = 'smtp.163.com'
port = 25
username = 'linkasde_system@163.com'
password = '1349_asdelkji'


class TestMail(unittest.TestCase):

    def test_instance(self):
        instance = Postman(host, port, username, password)
        instance.email('linkasde_system@163.com', '测试', '功能测试', ['yz@lejurobot.com'])


if __name__ == '__main__':
    unittest.main()
