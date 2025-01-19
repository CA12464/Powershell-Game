import curses
from dungeon import generate_dungeon
from entities import Player, Enemy, Item

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    # Generate dungeon and entities
    dungeon = generate_dungeon(width=20, height=10, num_rooms=3)
    player = Player(1, 1)
    enemies = [Enemy(5, 5), Enemy(10, 8)]
    items = [Item(3, 3, "Potion")]

    # Main game loop
    while not player.is_dead:
        # Render game
        render(stdscr, dungeon, player, enemies, items)

        # Get user input
        key = stdscr.getch()
        if key == ord('q'):  # Quit game
            break

        handle_input(key, player, dungeon, enemies, items)

        # Enemy movement (to be implemented fully)
        for enemy in enemies:
            enemy.move_towards(player, dungeon)

def render(stdscr, dungeon, player, enemies, items):
    stdscr.clear()
    for y, row in enumerate(dungeon):
        for x, tile in enumerate(row):
            if player.x == x and player.y == y:
                stdscr.addch(y, x, player.char)
            elif any(e.x == x and e.y == y for e in enemies):
                stdscr.addch(y, x, 'E')
            elif any(i.x == x and i.y == y for i in items):
                stdscr.addch(y, x, '$')
            else:
                stdscr.addch(y, x, tile)
    stdscr.refresh()

def handle_input(key, player, dungeon, enemies, items):
    if key == curses.KEY_UP:
        player.move(0, -1, dungeon)
    elif key == curses.KEY_DOWN:
        player.move(0, 1, dungeon)
    elif key == curses.KEY_LEFT:
        player.move(-1, 0, dungeon)
    elif key == curses.KEY_RIGHT:
        player.move(1, 0, dungeon)

if __name__ == "__main__":
    curses.wrapper(main)
