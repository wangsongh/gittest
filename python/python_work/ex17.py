# coding:utf-8
# More Files

# ��ű��������Ҫ��ģ��
from sys import argv
# ����ļ����ڷ���True����������ڷ���False
from os.path import exists

# ��ѹargv��
script, from_file, to_file = argv

# ���ӡ�ڵ�һ����ʾ��copying from from_file_name to to_fele_name
print(f"Copying from {from_file} to {to_file}")

# ��ʾ���������Ժ󣬴�Դ�����ļ������󶨱���indata
indata = open('/python_work/test17.txt','rb+').read()
# we could do these two on one line,how?
# in_file = open('/python_work/test.txt','rb+')
# indata = in_file.read()

# ��ӡ�ĵڶ�����ʾ��������ı����ȣ�bytes��
print(f"The input file is {len(indata)} bytes long")

# ��ӡ�����У��ж�д����ļ��Ƿ���ڣ������ڷ��أ�True
print(f"Does the output file exist? {exists(to_file)}")

# ��ӡ�����У���׼�����ˣ��س�������Ҫ���ذ�CTRL-C
print("Ready, hit RETURN to cintinue, CTRL-C to abort.")
input()

# ����������ʼд��Ŀ���ļ�
# �ȴ�д����ļ���Ȼ��������Դ�ļ���indata������д��
out_file = open('/python_work/to_file17.txt','wb') # 'w'�ᱨ����Ϊ�洢��ʽĬ���Ƕ����Ʒ�ʽ
out_file.write(indata)

# д���ļ��Ժ���ʾ���
print("Alright, all done.")

# ���һ�����ر��ļ�
out_file.close()
# indata.close()
