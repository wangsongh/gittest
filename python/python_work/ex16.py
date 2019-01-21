# coding:utf-8
# Reading and Writing Files

# close : close the file
# read : reads the comments of the file
# readline : reads just one line of a text file
# truncate : empties the file
# write('stuff') : Write 'stuff' to the file
# seek(0) : Moves the rear/write location to the begining of the file

# The argv is the argument variable
from sys import argv  # Python ѯ����ʹ����Щģ�飬���ذ����е�ģ�鶼�ӽ�����

# unpacks argv,it gets assigned to two variables you can work with:script,filename
script, filename = argv 

# print them out
print(f"We're going to erase {filename}.")        # erase filename ����ļ�����
print("If you don't want that, hit CTRL-C (^C).") # ����������ݰ� CTRL-C
print("If you do want that, hit RETURN.")         # ���Ҫ������ݣ���ENTER��

# input ?
input("?")

print("Opening the file...") # ���ļ�

# target �����Ѿ��򿪵��ļ�ʵ���� target. ���漴 �Ըô��ļ��Ĳ���������
# ����target.truncate([size]) #���ļ��óɹ涨�Ĵ�С��Ĭ�ϵ��ǲõ���ǰ�ļ�������ǵ�λ�á�
target = open('/python_work/ex15_sample.txt','w')

# ######## �򿪵��� ex15_sample.txt,���нű�ʱ python ex16.py test16.txt ,�������д��ex15_sample����
# ######## test16.txt�����ڣ�����տ�ʼ���ܴ治�����ĵ���������ھ�ֱ��д�룬�����ھ��½��Ժ�д��
# ���нű�ʱ����filename��test16.txt���򿪵���ex15_sample.txt��Ϊʲô����������д��ex15_sample.txt������ 

print("Truncating the file. Goodbye!") # �������
target.truncate()

print("Now I'm going to ask you for three lines.") # ����3��

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.") # д���µ�����

# target.write(line1+"\n"+line2+"\n"+line3) ������ȼ�

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.") # ���ر�
target.close()
