# coding:utf-8
# More Variables and Printing

# ��ֵ����
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# ������д�����һ������ʲô���𣿣�
print("Let's talk about", my_name,".")
print(f"Let's talk about {my_name}.")


print(f"He's {my_height} inches tall")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")


# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight

# f �����õģ��� format:����ʹ����ĸf��Ϊ����ʽ���Ŀ�ͷ
#  ��You also must start the string with the letter f for ��format����
# ʹ����������� {} �ѱ���Ƕ���ַ���

# ��һ��д��ʹ�ñȽϷ��㣬���Խ�����ֱ��Ƕ���ַ�����
print(f"If I add {my_age},{my_height}, and {my_weight} I get {total}.")
print("If I add",my_age,my_height,",and", my_weight,"I get",total,".")

# 1ǧ�ף�km��=0.621Ӣ�mile�� 1�ף�m��=3.281Ӣ�ߣ�ft��=1.094�루yd�� 
# 1���ף�cm��=0.394Ӣ�磨in�� 1Ӣ�磨in��=2.54���ף�cm��
var_cm = round(0.394 * my_height,4) # round() �������뺯��������С����λ��
print(f"My height is {my_height} inchs ,so it is {var_cm} cm")
