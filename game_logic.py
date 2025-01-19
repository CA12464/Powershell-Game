def attack(attacker, defender):
    defender.hp -= 1
    if defender.hp <= 0:
        return True  # Defender died
    return False
