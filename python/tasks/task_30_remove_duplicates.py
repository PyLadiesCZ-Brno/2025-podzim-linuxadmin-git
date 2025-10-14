# task_30_remove_duplicates.py

def remove_duplicates(nums: list[int]) -> list[int]:
    """
    Odstraní duplikáty ze seznamu a zachová pořadí.
    """
    if not isinstance(nums, list):
        raise TypeError("Argument musí být seznam (list).")

    new_list = []

    for x in nums:
        if x not in new_list:
            new_list.append(x)

    return new_list
