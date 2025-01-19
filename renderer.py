def render(dungeon, player, enemies, items):
    for y, row in enumerate(dungeon):
        for x, tile in enumerate(row):
            if player.x == x and player.y == y:
                print(player.char, end="")
            elif any(e.x == x and e.y == y for e in enemies):
                print("E", end="")
            elif any(i.x == x and i.y == y for i in items):
                print("$", end="")
            else:
                print(tile, end="")
        print()  # Newline after each row
