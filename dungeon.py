import random

def generate_dungeon(width=20, height=10, num_rooms=5):
    dungeon = [["#" for _ in range(width)] for _ in range(height)]
    
    for _ in range(num_rooms):
        room_width = random.randint(3, 6)
        room_height = random.randint(3, 6)
        x = random.randint(1, width - room_width - 1)
        y = random.randint(1, height - room_height - 1)
        
        for i in range(y, y + room_height):
            for j in range(x, x + room_width):
                dungeon[i][j] = "."
    
    return dungeon
