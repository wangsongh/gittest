# coding:utf-8
# Reading and Writing Files

# close : close the file
# read : reads the comments of the file
# readline : reads just one line of a text file
# truncate : empties the file
# write('stuff') : Write 'stuff' to the file
# seek(0) : Moves the rear/write location to the begining of the file

# The argv is the argument variable
from sys import argv  # Python 询问你使用哪些模块，不必把所有的模块都加进程序

# unpacks argv,it gets assigned to two variables you can work with:script,filename
script, filename = argv 

# print them out
print(f"We're going to erase {filename}.")        # erase filename 清除文件内容
print("If you don't want that, hit CTRL-C (^C).") # 不想清除数据按 CTRL-C
print("If you do want that, hit RETURN.")         # 如果要清除数据，按ENTER键

# input ?
input("?")

print("Opening the file...") # 打开文件

# target 代表已经打开的文件实例； target. 后面即 对该打开文件的操作方法；
# 例：target.truncate([size]) #把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。
target = open('/python_work/ex15_sample.txt','w')

# ######## 打开的是 ex15_sample.txt,运行脚本时 python ex16.py test16.txt ,最后数据写到ex15_sample中了
# ######## test16.txt不存在，我想刚开始不管存不存在文档，如果存在就直接写入，不存在就新建以后写入
# 运行脚本时传的filename是test16.txt，打开的是ex15_sample.txt，为什么不报错，而是写到ex15_sample.txt里面了 

print("Truncating the file. Goodbye!") # 清空数据
target.truncate()

print("Now I'm going to ask you for three lines.") # 请求3行

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.") # 写入新的数据

# target.write(line1+"\n"+line2+"\n"+line3) 和下面等价

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.") # 最后关闭
target.close()
