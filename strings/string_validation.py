'''
bai 2
'''


def is_palindrome(s):
    s = s.lower()
    cleaned = ""
    for char in s:
        if char != " ":
            cleaned = cleaned + char
    reversed_s = ""
    for i in range(len(cleaned) - 1, -1, -1):
        reversed_s = reversed_s + cleaned[i]
    return cleaned == reversed_s
def is_anagram(s1, s2):
    
    s1 = s1.lower()
    s2 = s2.lower()

    return sorted(s1) == sorted(s2)

def has_all_unique_chars(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                return False 
    return True 
if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))  
    print(is_anagram("listen", "silent")) 
    print(has_all_unique_chars("abcdef"))                 
    print(has_all_unique_chars("hello"))     
