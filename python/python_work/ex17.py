# coding:utf-8
# More Files

# 向脚本中添加需要的模块
from sys import argv
# 如果文件存在返回True，如果不存在返回False
from os.path import exists

# 解压argv包
script, from_file, to_file = argv

# 会打印在第一行提示：copying from from_file_name to to_fele_name
print(f"Copying from {from_file} to {to_file}")

# 提示复制数据以后，打开源数据文件，并绑定变量indata
indata = open('/python_work/test17.txt','rb+').read()
# we could do these two on one line,how?
# in_file = open('/python_work/test.txt','rb+')
# indata = in_file.read()

# 打印的第二行显示：输入的文本长度（bytes）
print(f"The input file is {len(indata)} bytes long")

# 打印第三行：判断写入的文件是否存在，若存在返回：True
print(f"Does the output file exist? {exists(to_file)}")

# 打印第四行：若准备好了，回车继续，要返回按CTRL-C
print("Ready, hit RETURN to cintinue, CTRL-C to abort.")
input()

# 若继续，则开始写入目标文件
# 先打开写入的文件，然后把上面的源文件（indata）内容写入
out_file = open('/python_work/to_file17.txt','wb') # 'w'会报错，因为存储方式默认是二进制方式
out_file.write(indata)

# 写入文件以后，提示完成
print("Alright, all done.")

# 最后一步，关闭文件
out_file.close()
# indata.close()
