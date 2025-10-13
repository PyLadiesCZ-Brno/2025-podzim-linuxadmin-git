# task_10_flatten_list.py

def flatten_list(nested: list[list[int]]) -> list[int]:
    """
    Zploští dvourozměrný seznam do jednoho seznamu.
    """

    final_list = []
    for i in nested:
        if isinstance(i, int):
            final_list.append(i)
        else:
            final_list.extend(flatten_list(i))

    return final_list
