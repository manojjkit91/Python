#Python program to print all possible armstrong numbers
#between 100 to 10000
num = 100
while num <= 10000:
    temp = num
    armchk = 0
    digits = 0
    
    while temp != 0:
       temp = temp // 10
       digits = digits + 1
    temp = num
    
    while temp != 0:
        rem = temp % 10
        armchk = armchk + rem ** digits
        temp = temp // 10
    if num == armchk:
        print (num)
    num = num + 1
