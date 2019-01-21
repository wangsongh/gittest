# encoding:utf-8
# Reading Files

from sys import argv  # 从sys包获取需要的变量给argv

script,filename = argv  # ex15_sample 文件名

# D:\python_work\ex15_sample.txt 文件路径

txt = open('/python_work/test.txt','r')  #一定要加上路径，不然找不到文件 ; r表示只读
# 此处特别注意--使用正斜杠/，而复制文件路径是反斜杠\，刚好相反
 
print(f"Here's your file {filename}:")  # 打印filename文件
print(txt.read())  # 读取文件

print("Type the filename again:")  # 再一次打印
# file_again = input("> ")  # 提示符 >

# txt_again = open(file_again)  # open文件

# print(txt_again.read())  # 再一次打印文件
