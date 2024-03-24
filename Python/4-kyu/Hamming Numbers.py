def hamming(n):
    p2, p3, p5 = 0, 0, 0
    hamming_numbers = [1]
    
    for _ in range(1, n):
        next_hamming_number = min(hamming_numbers[p2] * 2, hamming_numbers[p3] * 3, hamming_numbers[p5] * 5)
        
        hamming_numbers.append(next_hamming_number)
        
        if next_hamming_number == hamming_numbers[p2] * 2:
            p2 += 1
        if next_hamming_number == hamming_numbers[p3] * 3:
            p3 += 1
        if next_hamming_number == hamming_numbers[p5] * 5:
            p5 += 1
    
    return hamming_numbers[-1]
