# encoding:utf-8
# Functions and Files

# ��python������Ҫ��ģ��
from sys import argv
# ��ѹargv��
script, input_file = argv
# ���庯���������� print_all, ���� f
def print_all(f):
# colon��indent ����4���ո�
	print(f.read())

# ���庯����rewind
def rewind(f):
# seek() �ƶ��ļ���ȡָ�뵽ָ��λ��
# fileObject.seek(offset[,whence]) 
# offset --��ʼ��ƫ������Ҳ���Ǵ�����Ҫ�ƶ�ƫ�Ƶ��ֽ�����bytes��
# whence����ѡ��Ĭ��0����ʾ���ļ���ͷ����1����ӵ�ǰλ�ÿ�ʼ����2������ļ�ĩβ����
	f.seek(0)

# ���庯����print_a_line	
def print_a_line(line_count,f):
# read() ÿ�ζ�ȡ�����ļ�
# readlines() ÿ�ζ�ȡ�����ļ�����read()���ǣ�readlines()�Զ����ļ����ݷ�����һ���е��б�
# readline() ÿ�ζ�ȡһ��
	print(line_count,f.readline())

# ���ļ�����ֵ��current_file
current_file = open('/python_work/test.txt','r')

# ��ӡ��ʾ�ڵ�һ�У���ʾ����Ҫ��ӡȫ���ĵ�����
print("First let's print the whole file:\n")

# print_all ��ȡ�ĵ�
print_all(current_file)

print("\nNow let's rewind, kind of like a tape.\n")

# rewind ���ص��ĵ���ͷ
rewind(current_file)

print("Let's print three lines:")

# ��ӡ�Ľ��ÿ��ǰ�涼���һ�����
current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

