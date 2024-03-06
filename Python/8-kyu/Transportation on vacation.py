def rental_car_cost(d):
    daily_cost = 40

    if d >= 7:
        total_cost = d * daily_cost - 50
    elif d >= 3:
        total_cost = d * daily_cost - 20
    else:
        total_cost = d * daily_cost

    return total_cost
