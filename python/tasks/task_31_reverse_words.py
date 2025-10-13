# task_31_reverse_words.py

def reverse_words(s: str) -> str:
    """
    Otočí pořadí slov ve větě.
    """
    list_s = s.split()
    list_s.reverse()
    return ' '.join(list_s)
