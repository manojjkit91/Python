#Python program to Check given number is prime number or not
num = int(input('Enter a Number ? '))
count = 0
for i in range(1,num):
    if num % i == 0:
        count = count + 1
    if count == 2:
        print('The Given Number is Prime !!')
    else:
        print('The Given Number is not Prime !!')
         
