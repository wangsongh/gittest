# coding:utf-8
# Variables and Names

# ��������ֵ��
cars = 100 # ��������
space_in_a_car = 4.0 # ÿ������������
drivers = 30 # ˾������
passengers = 90 # �˿�����
cars_not_drive = cars-drivers # û�п��ĳ�����
cars_driven = drivers # �ѿ�������
carpool_capacity = cars_driven * space_in_a_car # carpool ƴ�� capacity ����������������
average_passengers_per_car = passengers / cars_driven # �ѿ��ĳ���ƽ��ÿ���ؿ���

# ��ӡ��ʾ ���ַ��������Ű���ʹ�ö��ŷָ����൱��ƴ��
print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_drive,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
