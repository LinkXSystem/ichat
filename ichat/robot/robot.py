# import itchat
#
# message = 'Hello, World!'
#
# user = 'filehelper'
#
# itchat.auto_login(enableCmdQR=False, hotReload=True)
#
# itchat.send(message, toUserName=user)

# import itchat
#
# newInstance = itchat.new_instance()
# newInstance.auto_login(hotReload=True, statusStorageDir='robot.pkl')
#
#
# @newInstance.msg_register(itchat.content.TEXT)
# def reply(msg):
#     return msg.text
#
#
# newInstance.run()

# import itchat
#
#
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     print(msg)
#     return msg.text
#
#
# itchat.auto_login()
# itchat.run()
