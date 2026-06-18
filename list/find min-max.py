# baif 3

def  tim_min(numbers):
    
    so_min = numbers[0]
    
    for i in range(1, len(numbers)):
        
        if numbers[i] < so_min:
            
            so_min = numbers[i]
            
    return so_min


print("so nho nhat la:" , tim_min([1 ,2 ,3 , 4, 5, 6]))
        
def tim_max(numbers):
    
    
    so_max = numbers[0]
        
    for i in range(1, len(numbers)):
            
            if numbers[i] > so_max:
                
                so_max = numbers[i]
                
                
    return so_max

if __name__ == "__main__":

    print("so nho nhat la:" , tim_min([1 ,2 ,3 , 4, 5, 6]))
    print("so lon nhat la:" , tim_max([1, 2, 3, 4, 5, 6]))                