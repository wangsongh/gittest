# coding:utf-8
# Parameters,Unpacking,Variables

# Hold up ! features have another name : modules(模块)
# import: 从Python特性集向脚本添加使用哪些特性，不必一次给所有的特性，程序较小规模
# argv : argument variable 参数变量，这个变量保存运行Python脚本时传递给它的参数
from sys import argv 
# read the WYSS section for how to run this

# 解包argv，然后就可以分配需要的变量（只需要保存运行时传递的几个参数，而不需要保存所有的参数）
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
