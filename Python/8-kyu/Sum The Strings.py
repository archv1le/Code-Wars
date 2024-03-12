def sum_str(a, b):
    if not a:
        a = "0"
    if not b:
        b = "0"
    
    result = int(a) + int(b)
    return str(result)
