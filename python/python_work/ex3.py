#coding:utf-8
# Numbers and Math:
# +:plus ; -:minus ; /:slash ; *:asterisk ; %:percent
# <:less-than ; >:greater-than ; <=:less-than-equal ; >=:greater-than-equal

print("I will now count my chickens:")

print("Hens",25+30/6) # 结果浮点格式：30.0
print("Rooster",100-25*3%4) # 100 - 25 * 3/100 * 4 = 97
# 3%4相当于：百分之三乘以4（12%）

print(100-25%4) # 100 - 25/100 * 4 = 99
print(25/100*4) # 1.0
print(25%4) # 1

# 为什么有的结果是浮点有的不是？

print("Now I will count the eggs:")

print(3+2+1-5+4%2-1/4+6)

print("Is it true that 3+2<5-7?")
print(3+2<5-7)

print("What is 3+2?",3+2)
print("What is 5-7?",5-7)

print("Oh,that is why it's False.")

print("How about some more.")

print("Is it greater?",5>-2)
print("Is it greater or equal?",5>=-2)
print("Is it less or equal?",5<=-2)
