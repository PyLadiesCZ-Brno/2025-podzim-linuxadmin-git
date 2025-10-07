# task_05_count_vowels.py

def count_vowels(s: str) -> int:
    """
    Vrátí počet samohlásek v řetězci.
    """
    vowels = "AEIOUaeiouÁÉÍÓÚáéíóúÄËÏÖÜäëïöü"

    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count
