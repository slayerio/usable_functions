def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    if x <= 3:
        return True # for 2, 3
    if x % 2 == 0 or x % 3 == 0:
        return False # for x > 3 divided by 2 or 3
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False # for x >= 25 that divided by prime numbers
        i += 6
    return True # for 3 < x < 25 that are prime \ numbers that passed the while loop