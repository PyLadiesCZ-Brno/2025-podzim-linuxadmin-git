# task_39_reverse_vowels.py

def reverse_vowels(s: str) -> str:
    """
    Vrátí řetězec s přeházenými samohláskami v opačném pořadí.
    Ostatní znaky zůstávají na místě.
    """
    vowels_lst = []
    index_lst = []
    for index, char in enumerate(s):
        if char in "AEIOUaeiou":
            index_lst.append(index)
            vowels_lst.append(char)
    vowels_lst.reverse()
    for index, vowel in list(zip(index_lst, vowels_lst)):
        s = s[:index] + vowel + s[index + 1:]
    return s


print(reverse_vowels("leetcode"))
