from ichat import Postman

host = 'smtp.163.com'
port = 25
username = 'linkasde_system@163.com'
password = '2020IO'

instance = Postman(host, port, username, password)
# instance.debug(True)
instance.email('linkasde_system@163.com', '微信消息', '功能测试', ['scratchx@163.com', 'linkxsystem@163.com'])
