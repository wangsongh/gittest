# encoding:utf-8
# Reading Files

from sys import argv  # ��sys����ȡ��Ҫ�ı�����argv

script,filename = argv  # ex15_sample �ļ���

# D:\python_work\ex15_sample.txt �ļ�·��

txt = open('/python_work/test.txt','r')  #һ��Ҫ����·������Ȼ�Ҳ����ļ� ; r��ʾֻ��
# �˴��ر�ע��--ʹ����б��/���������ļ�·���Ƿ�б��\���պ��෴
 
print(f"Here's your file {filename}:")  # ��ӡfilename�ļ�
print(txt.read())  # ��ȡ�ļ�

print("Type the filename again:")  # ��һ�δ�ӡ
# file_again = input("> ")  # ��ʾ�� >

# txt_again = open(file_again)  # open�ļ�

# print(txt_again.read())  # ��һ�δ�ӡ�ļ�
