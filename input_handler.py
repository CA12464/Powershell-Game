import curses

def get_input():
    key = curses.wrapper(lambda stdscr: stdscr.getch())
    return key

def handle_input(action, player, dungeon, enemies, items):
    if action == ord('w'):
        player.move(0, -1, dungeon)
    elif action == ord('s'):
        player.move(0, 1, dungeon)
    elif action == ord('a'):
        player.move(-1, 0, dungeon)
    elif action == ord('d'):
        player.move(1, 0, dungeon)
