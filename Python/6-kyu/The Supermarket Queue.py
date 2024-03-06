def queue_time(customers, n):
    if n == 1:
        return sum(customers)

    tills = [0] * n
    for time in customers:
        min_till_index = tills.index(min(tills))
        tills[min_till_index] += time 

    return max(tills)
