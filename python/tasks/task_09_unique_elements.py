# task_09_unique_elements.py

def unique_elements(lst: list[int]) -> list[int]:
    """
    Vrátí seznam bez duplicitních prvků, zachová původní pořadí.
    """
    list_b = []
    for i in lst:
        if i not in list_b:
            list_b.append(i)
    return list_b
