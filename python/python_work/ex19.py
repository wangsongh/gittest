# coding:utf-8
# Functions and Variables

def cheese_and_crackers(cheese_count,boxes_of_crackers): # ����һ���������������ĺ���
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n") # \n ÿһ�δ��θ�һ��
    
    
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)  # ������������������ֵ
	
# �ȸ�ֵ�����������ٰѱ���ֵ��������	
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)
	
