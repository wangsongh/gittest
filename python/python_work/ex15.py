# encoding:utf-8
# Reading Files


# ����������������Ǵ��ݵģ�������ͨ�����ݲ�ͬ�Ĳ������Ըı�ֵ��
# �������ڹ����ж���ģ���ֵ�õģ�ֻ�������ڹ�����ʹ��

from sys import argv  # ��python���Լ�����ű��������Ҫ������

script,filename = argv  # ��ѹargv������������(�ű����ơ��ļ�����)
# ���д���ʱ���������������� python ex15.py ex15_sample.txt

# D:\python_work\ex15_sample.txt �ļ�·��

txt = open('/python_work/ex15_sample.txt','r')  #һ��Ҫ����·������Ȼ�Ҳ����ļ� ; r��ʾֻ��

# �˴��ر�ע��--ʹ����б��/���������ļ�·���Ƿ�б��\���պ��෴
# ����ʱ����һ���ܳ���GBK����ķ�ʽ����ʧ�ܣ��������������Դ򿪵��ĵ����ݻ��Ǳ���֮ǰ����ʹ��txt�ı��༭���༭��
# ��ʹ��notpad++���½��ĵ���notepadĬ��ʹ��utf-8��ʽ���ٴ����д���ͨ����

print(f"Here's your file {filename}:")  # ��ӡfilename�ļ�
print(txt.read())  # ��ȡ�ļ�

print("Type the filename again:")  # ��һ�δ�ӡ
file_again = input("> ")  # ��ʾ�� > ������һ���ļ���

txt_again = open(file_again)  # open�ļ�

print(txt_again.read())  # ��һ�δ�ӡ�ļ�
