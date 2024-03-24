def product_fib(_prod):
    fib1, fib2 = 0, 1
    
    while fib1 * fib2 < _prod:
        fib1, fib2 = fib2, fib1 + fib2

    return [fib1, fib2, fib1 * fib2 == _prod]
