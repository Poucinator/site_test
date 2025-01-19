import random

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, player):
        effect_value = random.randint(5, 20)  # Lancer de dé à 20 faces pour déterminer l'effet
        if self.effect == "heal":
            player.heal(effect_value)
        elif self.effect == "mana":
            player.magic.mana += effect_value
        elif self.effect == "damage":
            return effect_value
        return effect_value
