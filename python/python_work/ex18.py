# coding:utf-8
# Names,Variables,Code,Functions

# ###First line instruction

# We tell Python we want to make a function using def for "define"
# function name : print_two
# *args(asterisk[�Ǻ�] args): which is a lot like your argv parameter but for function
#                            This has to go inside parentheses to work.(�����������������)
# We end this line with a :(colon) and start indenting.(��ð�Ž�������ʼ����)
def print_two(*args):
	
# second line instruction
# After the colon,all the lines that are indented four spaces
# Our first indented line is one that unpacks the arguments,the same as with your scripts.  	
	arg1,arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok,that *args is actually pointless,we can just do this
# In python we can skip the whole unpacking arguments(���������������) - 
# and use the names we want right inside parentheses
def print_two_again(arg1,arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
	print("I got nothin'.")
	
print_two("Zed","Shae")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
