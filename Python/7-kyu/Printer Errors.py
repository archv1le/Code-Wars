def printer_error(s):
    error_count = sum(1 for char in s if char not in 'abcdefghijklm')
    
    error_rate = f"{error_count}/{len(s)}"
    
    return error_rate
