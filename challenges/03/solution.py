def is_narcissistic(number, base=10):
    n = int(number, base)
    digits = len(number)
    return n == sum(map(lambda x: pow(int(x, base), digits), number))
