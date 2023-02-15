import random

def rolldobbelsteen():
    return [random.randint(1, 6) for _ in range(5)]

def rerolldobbelsteen(dice):
    keep = input("Welke dobbelsteen wil je houden? (comma gescheiden) ")
    keep = [int(d) for d in keep.split(",") if d.isdigit()]
    return keep + [random.randint(1, 6) for _ in range(5 - len(keep))]

def scoredobbelsteen(dice):
    score = {}
    for d in dice:
        if d in score:
            score[d] += d
        else:
            score[d] = d
    if len(score) == 5:
        return 50  # Yahtzee!
    if len(score) == 4:
        return sum(dice)
    if len(score) == 3:
        if any(v == 3 for v in score.values()):
            return 25  # Full House
        else:
            return sum(dice)
    if len(score) == 2:
        if any(v == 4 for v in score.values()):
            return sum(dice)  # Four of a Kind
        else:
            return 30  # Small Straight
    if len(score) == 1:
        return sum(dice)  # Chance
    return 0

def play_yahtzee():
    scores = {}
    for i in range(13):
        print(f"\nRound {i+1}")
        dice = rolldobbelsteen()
        print(f"Roll 1: {dice}")
        dice = rerolldobbelsteen(dice)
        print(f"Roll 2: {dice}")
        dice = rerolldobbelsteen(dice)
        print(f"Roll 3: {dice}")
        score = scoredobbelsteen(dice)
        print(f"Score: {score}")
        categorie = input("welke categorie wil je in scoren? ")
        scores[categorie] = score
    print("\nFinal scores:")
    for categorie, score in scores.items():
        print(f"{categorie}: {score}")

play_yahtzee()    
    