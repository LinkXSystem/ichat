import itchat
from ichat import Robot, CommonUtils

itchat.auto_login(hotReload=True)

instance = itchat.new_instance()
instance.auto_login(hotReload=True, statusStorageDir='robot.pkl')

robot = Robot()


@instance.msg_register(itchat.content.TEXT)
def listener(message):
    # user = message['User']
    # if CommonUtils.equal(user['NickName'], 'izhi-robot'):
    #     return 'Hello, This is robot !'
    return robot.flow(message)


instance.run()
