# coding:utf-8
# What Was That?

tabby_cat = "\tI'm tabbed in."  # \t ˮƽ����һ���Ʊ��(4���ո�)
persian_cat = "I'm split\n\ton a line." # \n  \n������һ�У����У�
backslash_cat = "I'm \\ a \\ cat." # \\ ת��\�Լ�,����python�ַ�������\

# \b ɾ��ǰ�ߵĿո� �� \r ��������ݷŵ���ǰ�棬���һḲ��ǰ������� �� \a �������bell��������һ������~��
# \f �ϼ�ͷ ; \000 1��3λ�˽�����������������ַ� �� \xhh 1��2λʮ������������������ַ� 
my_cat = "I \a have a very \f beautiful \bcat  add \\r nihao become ahead." 

# triple-quotes �ȿ��Ա�ʾ�ַ����е�single-quote��Ҳ������python�ж�����ʾ
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

tiny_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''



print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(my_cat)
print(tiny_cat)
