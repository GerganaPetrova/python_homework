from functools import reduce

def square_sum(number):
    return sum(int(i)**2 for i in str(number))

HAPPY_SEQUENCE = set()

def is_happy(number):
    square = square_sum(number)
    if square == 1:
        HAPPY_SEQUENCE.clear()
        return True
    elif square in HAPPY_SEQUENCE:
        HAPPY_SEQUENCE.clear()
        return False
    else:
        HAPPY_SEQUENCE.add(square)
        return is_happy(square)

def is_prime(number):
    n = abs(number)
    return reduce((lambda x,y: x*y), range(1, n)) % n == n - 1

def happy_primes(interval):
    return [x for x in interval if is_happy(x) and is_prime(x)]

