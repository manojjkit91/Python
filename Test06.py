#Python program to check given number is armstrong or not
num = int(input('Enter a Number ? '))
temp = num
armchk = 0
digits = 0

#find number of digits in given number

while temp != 0:
    temp = temp // 10
    digits = digits + 1
temp = num
while temp != 0:
    rem = temp % 10
    armchk = armchk + rem ** digits
    temp = temp // 10
if num == armchk:
    print ('The Given Number is armstrong')
else:
    print ('The Given Number is not armstrong')
