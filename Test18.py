#Program to check if a Number is Positive, Negative or Zero

num = float(input("Enter a number: "))  
if num > 0:  
 print("{0} is a positive number".format(num))  
elif num == 0:  
   print("{0} is zero".format(num))   
else:  
   print("{0} is negative number".format(num))   
