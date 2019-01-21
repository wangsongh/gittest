# encoding:utf-8
# Reading Files


# 变量与参数：参数是传递的（过程中通过传递不同的参数可以改变值）
# 变量是在过程中定义的，赋值用的，只能在所在过程中使用

from sys import argv  # 从python特性集中向脚本中添加需要的特性

script,filename = argv  # 解压argv包，两个参数(脚本名称、文件名称)
# 运行代码时，传递两个参数： python ex15.py ex15_sample.txt

# D:\python_work\ex15_sample.txt 文件路径

txt = open('/python_work/ex15_sample.txt','r')  #一定要加上路径，不然找不到文件 ; r表示只读

# 此处特别注意--使用正斜杠/，而复制文件路径是反斜杠\，刚好相反
# 测试时，这一步总出错，GBK编码的方式解码失败，但复制其他可以打开的文档内容还是报错，之前可能使用txt文本编辑器编辑的
# 遂使用notpad++重新建文档，notepad默认使用utf-8格式，再次运行代码通过。

print(f"Here's your file {filename}:")  # 打印filename文件
print(txt.read())  # 读取文件

print("Type the filename again:")  # 再一次打印
file_again = input("> ")  # 提示符 > 再输入一次文件名

txt_again = open(file_again)  # open文件

print(txt_again.read())  # 再一次打印文件
