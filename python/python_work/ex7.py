# coding:utf-8
# More Printing

print("Mary had a little lamb.")
print("It's fleece was white as {}.".format('snow')) #对已经创建的字符串格式化：.format()
print("And everywhere that Mary went.")
print("." * 10) # what'd that do  ##连续10个. 

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6) # 没有end=' ' 只打印此行内容，下面会换行
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') # 有end=' ' 打印此行内容和下面的内容
print(end7 + end8 + end9 + end10 + end11 + end12)
# 下面的结果和上面两行的一样
print(end1 + end2 + end3 + end4 + end5 + end6 + ' ' + end7 + end8 + end9 + end10 + end11 + end12) 


