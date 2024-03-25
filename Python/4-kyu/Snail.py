def snail(snail_map):
    snail_result = []
    while snail_map:
        snail_result.extend(snail_map.pop(0))
        
        for row in snail_map:
            snail_result.append(row.pop(-1))
        
        if snail_map:
            snail_result.extend(snail_map.pop(-1)[::-1])

        for row in reversed(snail_map):
            snail_result.append(row.pop(0))
    
    return snail_result
