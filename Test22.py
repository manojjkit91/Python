num = int(input("Enter a number: "))  
sum = 0 
digit = 0 
temp = num  
while temp > 0:
	temp = temp // 10
	digit=digit + 1 
temp = num
while temp > 0:  
   rem = temp % 10  
   sum += rem ** digit  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  
