def sum_numbers(number):  
    total_sum = 0  
    current_number = 1  
      
    while current_number <= number:  
        total_sum += current_number     
        current_number += 1            
          
    return total_sum  
  
if __name__ == "__main__":  
    number = int(input("Enter a number: "))    
    result = sum_numbers(number)  
    print(result)  
