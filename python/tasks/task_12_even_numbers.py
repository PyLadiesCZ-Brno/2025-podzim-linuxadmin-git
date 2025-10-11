# task_12_even_numbers.py

def even_numbers(lst: list[int]) -> list[int]:
    """
    Vrátí seznam pouze sudých čísel.
    """
    even = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
    return even
