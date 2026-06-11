def find_insert_position(my_list, target):
    
    for i in range(len(my_list)):
        
        if target <= my_list[i]:
            
            return i
    return len(my_list)

if __name__== "__main__":

    print(find_insert_position([1, 3, 5, 6], 5))

    print(find_insert_position([1, 3, 5, 6], 7))

    print(find_insert_position([1, 3, 5, 6], 4))