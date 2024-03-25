def enough(cap, on, wait):
    remaining_capacity = cap - on
    
    if remaining_capacity >= wait:
        return 0
    else:
        return wait - remaining_capacity
