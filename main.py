import itchat

@itchat.msg_register('Text')
def text_reply(msg):
    response = str('现在暂时无法回复')
    if u'任平' in msg['Text'] or u'rp' in msg['Text']:
        itchat.send(msg=str('提我干嘛我只是个代码狗（抱枕头哭）'),toUserName=msg['FromUserName'])
    else:
        itchat.send(msg=str(response),toUserName=msg['FromUserName'])
    
@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        itchat.send(msg=str('打字打字（敲黑板）'),toUserName=msg['FromUserName'])
    elif msg['Type'] == 'Sharing':
        itchat.send(msg=str('打字打字（敲黑板）'),toUserName=msg['FromUserName'])
    elif msg['Type'] == 'Note':
        itchat.send(msg=str('打字打字（敲黑板）'),toUserName=msg['FromUserName'])
    elif msg['Type'] == 'Card':
        itchat.send(msg=str('打字打字（敲黑板）'),toUserName=msg['FromUserName'])
        
@itchat.msg_register(['FRIENDS'])
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('现在无法进行回复', msg['RecommendInfo']['UserName'])




itchat.auto_login(True,enableCmdQR=2)
itchat.run()

import warnings
warnings.filterwarnings("ignore")
