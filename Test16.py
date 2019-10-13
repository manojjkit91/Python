#Program to Sort Words in Alphabetic Order
user_str = input("Enter a string: ")  
# breakdown the string into a list of words  
words = user_str.split()  
# sort the list  
words.sort()  
# display the sorted words  
for word in words:  
   print(word)  
