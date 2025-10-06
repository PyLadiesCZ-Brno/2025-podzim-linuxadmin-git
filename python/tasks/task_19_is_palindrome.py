# task_19_is_palindrome.py

def is_palindrome(s: str) -> bool:
    """
    Vrátí True, pokud je řetězec palindrom.
    """
    cislo = len(s)
    
    for i in range(cislo//2):
        if s[i] != s[-i-1]:
            return False

    return True
