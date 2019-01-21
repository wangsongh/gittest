# coding:utf-8
# Variables and Names

# 给变量赋值：
cars = 100 # 车的数量
space_in_a_car = 4.0 # 每辆车容纳人数
drivers = 30 # 司机数量
passengers = 90 # 乘客数量
cars_not_drive = cars-drivers # 没有开的车数量
cars_driven = drivers # 已开车数量
carpool_capacity = cars_driven * space_in_a_car # carpool 拼车 capacity ……的能力，容量
average_passengers_per_car = passengers / cars_driven # 已开的车，平均每辆载客数

# 打印显示 的字符串用引号包起，使用逗号分隔，相当于拼接
print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_drive,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
