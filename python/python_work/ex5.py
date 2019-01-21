# coding:utf-8
# More Variables and Printing

# 赋值变量
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# 这两种写法结果一样，有什么区别？？
print("Let's talk about", my_name,".")
print(f"Let's talk about {my_name}.")


print(f"He's {my_height} inches tall")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")


# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight

# f 干嘛用的？？ format:必须使用字母f作为“格式”的开头
#  （You also must start the string with the letter f for “format”）
# 使用特殊的序列 {} 把变量嵌入字符中

# 第一种写法使用比较方便，可以将变量直接嵌入字符串中
print(f"If I add {my_age},{my_height}, and {my_weight} I get {total}.")
print("If I add",my_age,my_height,",and", my_weight,"I get",total,".")

# 1千米（km）=0.621英里（mile） 1米（m）=3.281英尺（ft）=1.094码（yd） 
# 1厘米（cm）=0.394英寸（in） 1英寸（in）=2.54厘米（cm）
var_cm = round(0.394 * my_height,4) # round() 四舍五入函数，保留小数点位数
print(f"My height is {my_height} inchs ,so it is {var_cm} cm")
