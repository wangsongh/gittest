# coding:utf-8
# Strings and Text


types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# 当想对已经创建的字符串应用格式时，会使用.format() syntax语法
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a righe side."

# + 号 可以把字符串拼接在一起
print(w + e)
