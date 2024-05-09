def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


def is_prime2(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
