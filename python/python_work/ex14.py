# coding:utf-8
# Prompting and Passing

from sys import argv # 从python特性集向脚本添加需要使用的特性

# 两个变量参数，打开文件时的语句：python csript use_name (例如：python ex14.py Wangsonghui)
script, user_name = argv # 解压argv包 script表示python脚本的名字（ex14.py） ,user_name需要传的参数
prompt = '> ' # 提示符 >

print(f"Hi {user_name},I'm the {script} script.") 
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) # 参数likes 临时保存input的内容

print(f"Where do you live {user_name}?")
lives = input(prompt) # 参数lives 临时保存input的内容

print("What kind of computer do you have?")
computer = input(prompt) # 参数computer 临时保存input的内容

# 把上面3个临时变量保存的值传入到下面的语句并保留代码格式打印出来
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
