# task_18_factorial.py

def factorial(n: int) -> int:
    """
    Vrátí faktoriál čísla n (n!).
    """

    if n < 0:
        raise ValueError("Only positive numbers")

    result = 1
    for i in range(2, n + 1):  # 0! = 1, 1! = 1
        result *= i

    return result
