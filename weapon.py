class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

    def get_name(self):
        return self.name

    def get_damage_amount(self):
        return self.damage

    def use_weapon(self):
        if self.durability > 0:
            self.durability -= 1
            if self.durability == 0:
                print(f"{self.name} s'est cassé!")
                return False
            return True
        return False

    def get_durability(self):
        return self.durability