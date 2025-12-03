# task_14_remove_zeros.py

def remove_zeros(lst: list[int]) -> list[int]:
    """
    Vrátí seznam bez nulových hodnot.
    """
    return [x for x in lst if x != 0]
