class Armor:
    def __init__(self, name, defense, durability):
        self.name = name
        self.defense = defense
        self.durability = durability

    def get_name(self):
        return self.name

    def get_defense_amount(self):
        return self.defense

    def take_damage(self, damage):
        if self.durability > 0:
            self.durability -= damage
            if self.durability <= 0:
                print(f"{self.name} est détruite!")
                self.durability = 0

    def get_durability(self):
        return self.durability