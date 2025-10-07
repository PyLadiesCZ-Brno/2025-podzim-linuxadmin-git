# task_13_max_in_list.py

def max_in_list(lst: list[int]) -> int:
    """
    Vrátí největší číslo v seznamu.
    """
    if not lst:
        raise ValueError("Seznam je prázdný")
    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num
    return max_value
