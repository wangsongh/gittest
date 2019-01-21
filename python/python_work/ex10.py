# coding:utf-8
# What Was That?

tabby_cat = "\tI'm tabbed in."  # \t 水平增加一个制表符(4个空格)
persian_cat = "I'm split\n\ton a line." # \n  \n处另起一行（换行）
backslash_cat = "I'm \\ a \\ cat." # \\ 转义\自己,告诉python字符串中有\

# \b 删除前边的空格 ； \r 后面的内容放到最前面，并且会覆盖前面的内容 ； \a 响铃符（bell），发出一声“滴~”
# \f 上箭头 ; \000 1到3位八进制数所代表的任意字符 ； \xhh 1到2位十六进制所代表的任意字符 
my_cat = "I \a have a very \f beautiful \bcat  add \\r nihao become ahead." 

# triple-quotes 既可以表示字符串中的single-quote，也可以在python中多行显示
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
