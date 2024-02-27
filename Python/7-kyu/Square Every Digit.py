def square_digits(num):
    digits = [int(digit) for digit in str(num)]
    
    squared_result = int(''.join(str(digit**2) for digit in digits))
    
    return squared_result
