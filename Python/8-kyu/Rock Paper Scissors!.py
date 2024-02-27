def rps(p1, p2):
    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if p1 == p2:
        return "Draw!"
    elif winning_combinations[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
