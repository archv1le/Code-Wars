def combat(health, damage):
    new_health = health - damage
    
    if new_health < 0:
        return 0
    
    return new_health
