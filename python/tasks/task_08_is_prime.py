# task_08_is_prime.py

def is_prime(n: int) -> bool:
    """
    Vrátí True, pokud je číslo prvočíslo.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
