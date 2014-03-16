def is_perfect(number):
    return number == sum([i for i in range(1, number//2 + 1) if number % i == 0])
