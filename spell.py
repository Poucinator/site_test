class Spell:
    def __init__(self, name, effect, mana_cost):
        self.name = name
        self.effect = effect
        self.mana_cost = mana_cost

    def get_name(self):
        return self.name

    def get_effect(self):
        return self.effect

    def get_mana_cost(self):
        return self.mana_cost


class Magic:
    def __init__(self, mana):
        self.mana = mana
        self.spells = {}

    def cast_spell(self, spell_name, target):
        if spell_name in self.spells:
            spell = self.spells[spell_name]
            if self.mana >= spell["cost"]:
                self.mana -= spell["cost"]
                effect = spell["effect"]
                target.apply_spell_effect(effect)
                print(f"{spell_name.capitalize()} lancé avec un effet de {effect}.")
            else:
                print("Pas assez de mana pour lancer ce sort.")
        else:
            print("Le sort n'existe pas.")
