# encoding:utf-8
# Functions and Files

# 从python导入需要的模块
from sys import argv
# 解压argv包
script, input_file = argv
# 定义函数：函数名 print_all, 变量 f
def print_all(f):
# colon后indent 缩进4个空格
	print(f.read())

# 定义函数：rewind
def rewind(f):
# seek() 移动文件读取指针到指定位置
# fileObject.seek(offset[,whence]) 
# offset --开始的偏移量，也就是代表需要移动偏移的字节数（bytes）
# whence：可选，默认0，表示从文件开头算起，1代表从当前位置开始算起，2代表从文件末尾算起
	f.seek(0)

# 定义函数：print_a_line	
def print_a_line(line_count,f):
# read() 每次读取整个文件
# readlines() 每次读取整个文件，和read()的是，readlines()自动将文件内容分析成一个行的列表
# readline() 每次读取一行
	print(line_count,f.readline())

# 打开文件，赋值给current_file
current_file = open('/python_work/test.txt','r')

# 打印显示在第一行，提示下面要打印全部文档内容
print("First let's print the whole file:\n")

# print_all 读取文档
print_all(current_file)

print("\nNow let's rewind, kind of like a tape.\n")

# rewind 返回到文档开头
rewind(current_file)

print("Let's print three lines:")

# 打印的结果每行前面都添加一个序号
current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

