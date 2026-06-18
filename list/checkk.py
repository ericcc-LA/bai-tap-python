def check(danhsach, target):
    
    for i in range(len(danhsach)):
        
        if danhsach[i] == target:
            
            return True
        
        else:
            
            return False
        
if __name__ == "__main__":

    result = check([1, 2, 3, 4], 3)
    print("The result is:", result)
            