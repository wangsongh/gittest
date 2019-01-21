# coding:utf-8
# Asking Questions

# We put an end=' ' at the end of each print line. 
# This tells print to not end the line with a newline character and go to the next line.
print("How old are you?",end=' ') 
age = input()
print("How tall are you?",end=' ')
height = input()
print("How much do you weigh?",end=' ')
weigh = input()


# 和上面的写法的结果一样
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weigh} heavy.") 
