number = int(input("Enter a number: "))  
  
sum_total = 0  
current_number = 1  
  
while current_number <= number:  
    sum_total += current_number  
    current_number += 1  
 
print("The sum from 1 to", number, "is:", sum_total)  
