class Entity:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

class Entity:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, '@')
        self.hp = 10
        self.is_dead = False  # Added attribute

    def move(self, dx, dy, dungeon):
        if dungeon[self.y + dy][self.x + dx] == ".":
            self.x += dx
            self.y += dy

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.is_dead = True


class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'E')
        self.hp = 5

class Item(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, '$')
        self.name = name
