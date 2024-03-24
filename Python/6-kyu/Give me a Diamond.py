def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    
    diamond_string = ''
    middle = n // 2 + 1 
    
    for i in range(1, n + 1):
        spaces = abs(middle - i) 
        stars = n - 2 * spaces 
        
        diamond_string += ' ' * spaces + '*' * stars + '\n'
    
    return diamond_string
