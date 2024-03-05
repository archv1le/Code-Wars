def tribonacci(signature, n):
    if n == 0:
        return []
    
    if n <= len(signature):
        return signature[:n]
    
    for _ in range(n - len(signature)):
        signature.append(sum(signature[-3:]))
    
    return signature
