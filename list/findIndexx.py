# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:03:55 2026

@author: minhq
"""

def find_index(listInput: list[int], target: int) -> int:
    
    for i in range(len(listInput)):
        
        if listInput[i] == target:
            
            return i
        
        else:
            
            return -1

if __name__ == "__main__":
    index = find_index([1, 2, 3, 4, 5], 3)
    print("The index is:", index)
