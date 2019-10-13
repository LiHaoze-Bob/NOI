#coding=utf-8
import easygui

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
