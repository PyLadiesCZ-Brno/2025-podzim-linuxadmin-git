# task_23_remove_vowels.py

def remove_vowels(s: str) -> str:
    """
    Vrátí řetězec bez samohlásek (a, e, i, o, u).
    """

    vowels = "aieouAEIOUáéíóúůÁÉÍÓÚŮ"
    letters = []

    for char in s:
        if char not in vowels:
            letters.append(char)

    new_word = "".join(letters)

    return new_word
