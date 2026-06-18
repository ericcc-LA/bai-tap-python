'''
bai 7 
'''


def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count


def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count


def char_frequency(s):
    freq = {}
    for char in s:
        if char == " ":
            continue
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


if __name__ == "__main__":
    print(count_vowels("hello world"))
    print(char_frequency("aabbcc"))
