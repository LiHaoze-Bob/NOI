#coding=utf-8
import random,easygui,os,json
count = 0

fd = open("user.json", mode='r')
line = fd.readline()
users = json.loads(line)
user = users[0]
fd.close()

inputValues = []

choice = easygui.buttonbox("选择您的登录方式",choices = ["登录","注册"])
#  注册窗口，添加一个新的用户
if choice == "注册":
    adduser = easygui.multpasswordbox('请输入您的用户名和密码：', '注册窗口', ["用户名", "密码"])
    new_user = {}
    new_user['username'] = adduser[0]
    new_user['password'] = adduser[1]
    new_user['winTimes'] = 0
    new_user['playTimes'] = 0
    users.append(new_user)
    save = json.dumps(users)
    print (save)
    fd = open("user.json", mode='w')
    fd.write(save)
    fd.flush()
    fd.close()

if choice == "登录":
    while(count < 3):
        if count == 0:
            inputValues = easygui.multpasswordbox('请输入游戏密码：', '登录窗口', ["用户名", "密码"])    
        else:
            inputValues = easygui.multpasswordbox('用户名或密码错误，请重新输入：', '登录窗口', ["用户名", "密码"])
        
            if inputValues[0] == user['username'] and inputValues[1] == user['password']:
                break
        count = count + 1
        
    if inputValues[0] == user['username'] and inputValues[1] == user['password']:
        easygui.msgbox("密码正确。",ok_button = "进入游戏")
        easygui.msgbox("你好，我是一个智能机器人!我有一个秘密，它是一个1至100的整数。我会给你5次机会，快来猜吧（还有小提示哦）！",ok_button = "开始游戏")
        while(1):
            secret = random.randint(0,100)
            tries = 0  
            user['playTimes'] = user['playTimes'] + 1
            while tries < 5:
                tries = tries + 1
                guess = easygui.integerbox("请输入你猜的数:",lowerbound = 1,upperbound = 100)
                if guess > secret:
                    easygui.msgbox("这个数比" + str(guess) + "要小哦！")
                elif guess < secret:
                    easygui.msgbox("这个数比" + str(guess) + "要大哦！")
                elif guess == secret:
                    easygui.msgbox("你       猜       对       了\n你       猜       对       了\n你       猜       对       了\n你       猜       对       了"),
                    user['winTimes'] = user['winTimes'] + 1
                    easygui.msgbox("用户"+str(user['username'])+"   游戏次数："+str(user['playTimes'])+"  获胜次数："+str(user['winTimes']),ok_button = "Let's go!!!")
                    break
                else:
                    easygui.msgbox("您的机会已用完，下次加油！   揭晓答案:" + str(secret))
                    easygui.msgbox("用户"+str(user['username'])+"   游戏次数："+str(user['playTimes'])+"  获胜次数："+str(user['winTimes']),ok_button = "Let's go!!!")
                    start = easygui.buttonbox("是否要再来一局?: ",choices = ['是','否'])
                    if start == '否':
                        save = json.dumps(user)
                        fd = open("user.json", mode='w')
                        fd.write(save)
                        fd.close()
                        break
    else:
        easygui.msgbox('你的密码不正确，不能进入该游戏！')



