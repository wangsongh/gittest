# coding:utf-8
# Parameters,Unpacking,Variables

# Hold up ! features have another name : modules(ģ��)
# import: ��Python���Լ���ű����ʹ����Щ���ԣ�����һ�θ����е����ԣ������С��ģ
# argv : argument variable �������������������������Python�ű�ʱ���ݸ����Ĳ���
from sys import argv 
# read the WYSS section for how to run this

# ���argv��Ȼ��Ϳ��Է�����Ҫ�ı�����ֻ��Ҫ��������ʱ���ݵļ���������������Ҫ�������еĲ�����
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
