# task_12_even_numbers.py

def even_numbers(lst: list[int]) -> list[int]:
    """
    Vrátí seznam pouze sudých čísel.
    """
    return [number for number in lst if number % 2 == 0]
