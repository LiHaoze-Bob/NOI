#coding=utf-8
import easygui

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



