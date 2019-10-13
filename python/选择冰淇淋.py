#coding=utf-8
import easygui

n = easygui.enterbox("你好，你叫什么名字？")
f = easygui.buttonbox(n + ",你最喜欢什么口味的冰淇淋？",choices = ['香草','巧克力','草莓','其他'])
if f == '其他':
    of = easygui.enterbox('请输入你最喜欢的口味：')
else:
    easygui.msgbox(n + ",你选择了" + f + "口味。")
    easygui.msgbox(n + ",你选择了" + of + "口味。")