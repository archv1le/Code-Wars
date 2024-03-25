def sum_digits(number):
    number = abs(number)
    
    digit_sum = 0
    
    while number > 0:
        digit = number % 10
        
        digit_sum += digit
        
        number //= 10
    
    return digit_sum
