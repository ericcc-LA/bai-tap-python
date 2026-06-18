def find_odd_occurrence(numbers):
    
    
    count = {}
    
    
    for i in numbers:
        
        if i in count:
            
            count[i] +=1
            
        else:
            
            count[i] = 1
            
    for i, times in count.items():
        
        if times % 2 != 0 :
            
            return i
if __name__ == "__main__":       
    result = find_odd_occurrence([1, 2, 3, 2, 3, 1, 3])
    print("The number that occurs odd times is:", result)