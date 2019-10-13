#1. Python Program to Find Maximum out of 3 numbers
num1 = int(input('Enter First Number ? '))
num2 = int(input('Enter Second Number ? '))
num3 = int(input('Enter Third Number ? '))
print (max(num1,num2,num3))

#2.Python Program to Find Maximum out of 3 numbers without using max()

if num1 > num2 and num1 > num3:
    print (num1)
elif num2 > num1 and num2 > num3:
    print (num2)
elif num3 > num1 and num3 > num2:
    print (num3)
else :
    print (num1)   #All are equal, print anyone 
