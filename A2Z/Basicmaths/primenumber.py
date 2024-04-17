num = 6


def check_prime(num: int) -> bool:
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True


print(check_prime(num))
