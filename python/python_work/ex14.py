# coding:utf-8
# Prompting and Passing

from sys import argv # ��python���Լ���ű������Ҫʹ�õ�����

# �����������������ļ�ʱ����䣺python csript use_name (���磺python ex14.py Wangsonghui)
script, user_name = argv # ��ѹargv�� script��ʾpython�ű������֣�ex14.py�� ,user_name��Ҫ���Ĳ���
prompt = '> ' # ��ʾ�� >

print(f"Hi {user_name},I'm the {script} script.") 
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) # ����likes ��ʱ����input������

print(f"Where do you live {user_name}?")
lives = input(prompt) # ����lives ��ʱ����input������

print("What kind of computer do you have?")
computer = input(prompt) # ����computer ��ʱ����input������

# ������3����ʱ���������ֵ���뵽�������䲢���������ʽ��ӡ����
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
