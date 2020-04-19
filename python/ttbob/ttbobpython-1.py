#coding=utf-8
import easygui,json,os,random
import easygui as g
time=0
count=0
look_for_users_time=0
del_user_time=0
code=0
inputValues=[]
fd = open("class.json",mode="r")
line = fd.readline()
users = json.loads(line)
user = users[0]
fd.close() 
        
def success():
    easygui.msgbox('\n'.join([''.join([('Love'[(x-y)%4]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]),ok_button='Thank you!')    
    while(1):
        choice=g.buttonbox(msg='Please choose the thing you want to do.',title='Homepage',choices=('game','talk with your friends','tools','back','settings'))    
        if choice=='talk with your friends':
            g.msgbox(msg="Sorry,it is not open yet.")
        elif choice=='game':
            game=g.buttonbox(msg='Please choose the game you want to play',title='Window',choices=('Guess the number',''))
            if game=='Guess the number':
                guess_the_number()
        elif choice=='tools':
            tool=g.buttonbox(msg='Please choose the tool you want to use',title='Window',choices=('Judge prime numbers','The conversion between Fahrenheit and Celsius'))
            if tool=='Judge prime numbers':
                zhi_shu_pan_duan()
            elif tool=='The conversion between Fahrenheit and Celsius':
                C_and_F()
        elif choice=="back":
            break
        elif choice=='settings':
            choose_setting=g.buttonbox(msg='username:'+user['username']+'/n'+'code:'+str(user['code'])+'/n'+'class:'+user['class']+'/n'+"playtimes:"+str(user["playtimes"])+'/n'+"wintimes:"+str(user['wintimes']),choices=('delete your account','change password','back'))
            if choose_setting=='delete your account':
                finally_choose=g.buttonbox(msg='Are you sure you want to delete your account?',choices=('Yes','No'))
                if finally_choose=='Yes':
                    global del_user_time
                    del_user_time=del_user_time+1
                    g.msgbox('Bye!')
                    del users[code]
                    save = json.dumps(users)
                    fd = open("class.json", mode='w')
                    fd.write(save)
                    fd.flush()
                    fd.close()                    
                    break
                else:
                    continue
            
                
def guess_the_number():
    easygui.msgbox("你好，我是一个智能机器人!我有一个秘密，它是一个1至100的整数。我会给你5次机会，快来猜吧（还有小提示哦）！",ok_button = "开始游戏")
    while(1):
        secret = random.randint(0,100)
        tries = 0  
        user['playtimes']=user['playtimes'] + 1
        while tries < 5:
            tries = tries + 1
            guess = easygui.integerbox("请输入你猜的数:",lowerbound = 1,upperbound = 100)
            if guess > secret:
                easygui.msgbox("这个数比" + str(guess) + "要小哦！")
            elif guess < secret:
                easygui.msgbox("这个数比" + str(guess) + "要大哦！")
            elif guess == secret:
                easygui.msgbox("你       猜       对       了\n你       猜       对       了\n你       猜       对       了\n你       猜       对       了"),
                user['wintimes'] = user['wintimes'] + 1
                easygui.msgbox("用户"+str(user['username'])+"   游戏次数："+str(user['playtimes'])+"  获胜次数："+str(user['wintimes']),ok_button = "Let's go!!!")
                break
        else:
            easygui.msgbox("您的机会已用完，下次加油！   揭晓答案:" + str(secret))
            easygui.msgbox("用户"+str(user['username'])+"   游戏次数："+str(user['playtimes'])+"  获胜次数："+str(user['wintimes']),ok_button = "Let's go!!!")
            start = easygui.buttonbox("是否要再来一局?: ",choices = ['是','否'])
            if start == '否':
                save = json.dumps(user)
                fd = open("class.json", mode='w')
                fd.write(save)
                fd.close()
                break
            
def zhi_shu_pan_duan():
    easygui.msgbox("你好，这个程序可以帮你判断一个数是否是质数。",ok_button = "开始吧！")
    while(1):
        num = easygui.integerbox("请输入要判断的数",lowerbound = 2,upperbound = 2e10)
        is_prime = False
        for i in range (2,num): 
            if num%i == 0:
                is_prime = True
        if is_prime == True:
            easygui.msgbox(str(num) + "不是质数。")
        else:
            easygui.msgbox(str(num) + "是质数。")  
        start = easygui.buttonbox("是否还要使用",choices = ["是","否"])
        if start == "否":
            break
        
def C_and_F():
    yes = 'y'
    while(1):
        easygui.msgbox("您好，这里是温度转换器。（只限摄氏度和华氏度）")
        a = easygui.buttonbox("请选择您要转换的温度种类（开始时的单位）：",choices = ['摄氏度','华氏度'])
        if a == '摄氏度':
            s = easygui.enterbox("输入数值:")
            z = 1.8 * float(s) + 32
            easygui.msgbox(str(s) + "摄氏度等于" + str(z) + "华氏度")
            restart = True
        elif a == '华氏度':
            o = easygui.enterbox("输入数值:")
            x = ((float(o) - 32)/1.8)
            easygui.msgbox(str(o) + "华氏度等于" + str(x) + "摄氏度")
            restart = True
        else:
            easygui.msgbox("输入错误，请重新输入！")
            restart = False

        if restart == True:
            start = easygui.buttonbox("是否还需要换算？",choices = ['是','否'])
            if start == '否' :
                break    

way=g.buttonbox(msg="Please choose the way to go in:",choices=("register","enter"))
if way=="enter":
    inputValues=g.multpasswordbox('please enter the password：', 'window',["username","password"])
    for a_user in users:
        if a_user["username"] == inputValues[0]:
            while(count<5):
                if inputValues[0] == a_user["username"] and inputValues[1] == a_user["password"]:
                    user = a_user
                    g.msgbox('Welcome to come back, '+inputValues[0]+'.',ok_button='Thank you!')
                    success()
                    break
                else:
                    count = count + 1
                    left_count=5-count
                    inputValues = g.multpasswordbox('The username or the password is wrong,you have '+str(left_count)+' time<s> left,please enter them again', 'window', ["username","password"])              
            else:
                g.msgbox("Sorry,break.")
        else:
            g.msgbox('Your username is wrong,break.')
        break
else:
    code=len(users)+del_user_time
    adduser = g.multpasswordbox('Please enter your username and password：', 'window', ["user name", "password"])
    while(1):
        one_user=users[look_for_users_time]
        one_username=one_user["username"]
        if adduser[0]==one_username:
            look_for_users_time=0
            g.msgbox('The user name already exists, please change it.','window','OK')
            adduser = g.multpasswordbox('Please enter your new username and password：', 'window', ["user name", "password"])
        else:
            look_for_users_time=look_for_users_time+1
            if look_for_users_time<code:
                continue
            else:
                break
    user_class=g.enterbox(msg='Please enter your class:',title='window')
    character=g.buttonbox(msg="choose the character,think it carefully",choices=("Student","Teacher"))
    new_user = {}
    new_user["username"] = adduser[0]
    new_user["password"] = adduser[1]
    new_user["class"] = user_class
    new_user["code"] = code
    new_user['playtimes'] = "0"
    new_user['wintimes'] = "0"
    users.append(new_user)
    save = json.dumps(users)
    g.msgbox(new_user)
    fd = open("class.json", mode='w')
    fd.write(save)
    fd.flush()
    fd.close()
    success()    
    
    
    