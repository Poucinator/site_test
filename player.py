from spell import Magic
import random
from time import sleep


class Player:
    TYPES = {
        "Prolétariat": {"fort": "Fascisme", "faible": "Populisme"},
        "Fascisme": {"fort": "Populisme", "faible": "Prolétariat"},
        "Populisme": {"fort": "Prolétariat", "faible": "Fascisme"},
    }

    def __init__(self, pseudo, health, attack, mana, type_politique):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        self.armor = None
        self.magic = Magic(mana)
        self.type_politique = type_politique
        self.inventory = {
            "Potion de Soin": 1,
            "Potion de Mana": 1,
            "Grenade": 1
        }
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100  # Par exemple, il faut 100 XP pour passer au niveau 2
        self.spells_unlocked = False  # Les sorts sont initialement verrouillés
        print("Bienvenue au joueur", pseudo, "/ Points de vie: ", health, "/ Attaque", attack, "/ Mana:", mana, "/ Type:", type_politique)

    def add_item(self, item, quantity):
        if item.name in self.inventory:
            self.inventory[item.name] += quantity
        else:
            self.inventory[item.name] = quantity

    def use_item(self, item_name, user, target):
        if item_name in self.inventory and self.inventory[item_name] > 0:
            if item_name == "Potion de Soin":
                heal_amount = random.randint(5, 20)
                user.heal(heal_amount)
                print(f"{item_name} utilisé. Soigne {heal_amount} points de vie.")
            elif item_name == "Potion de Mana":
                mana_amount = random.randint(5, 20)
                user.magic.mana += mana_amount
                print(f"{item_name} utilisé. Régénère {mana_amount} points de mana.")
            elif item_name == "Grenade":
                damage_amount = random.randint(5, 20)
                target.damage(damage_amount)
                print(f"{item_name} utilisé. Inflige {damage_amount} points de dégâts.")
            self.inventory[item_name] -= 1
        else:
            print(f"Pas de {item_name} disponible dans l'inventaire.")

    def apply_spell_effect(self, effect):
        if effect < 0:
            self.damage(-effect)  # Si l'effet est négatif, inflige des dégâts
        else:
            self.heal(effect)  # Si l'effet est positif, soigne le joueur

    def heal(self, amount):
        self.health += amount
        print(f"{self.pseudo} récupère {amount} points de vie.")

    # Autres méthodes existantes ...

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.pseudo} gagne {amount} XP.")
        sleep(2)
        self.check_level_up()

    def check_level_up(self):
        while self.experience >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= self.experience_to_next_level
        self.experience_to_next_level = int(self.experience_to_next_level * 1.5)  # Par exemple, augmenter l'XP nécessaire par 50%
        self.attack += 2  # Par exemple, augmenter l'attaque de base de 2 à chaque niveau
        print(f"{self.pseudo} monte au niveau {self.level} ! Attaque augmentée à {self.attack}.")
        sleep(2)

        # Débloquer de nouvelles compétences ou sorts au niveau 2
        if self.level == 2:
            self.unlock_spells()

    def unlock_spells(self):
        self.magic.spells["fireball"] = {"cost": 10, "effect": -10}
        self.magic.spells["heal"] = {"cost": 8, "effect": 10}
        self.spells_unlocked = True
        print(f"{self.pseudo} a débloqué de nouveaux sorts: Fireball et Heal !")
        sleep(2)

    def can_cast_spell(self, spell_name):
        if self.spells_unlocked:
            return spell_name in self.magic.spells
        return False

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        if self.has_weapon():
            return self.attack + self.weapon.get_damage_amount()
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        base_damage = self.get_attack_value()
        damage = self.calculate_damage(base_damage, target_player)
        target_player.damage(damage)
        return damage

    def calculate_damage(self, base_damage, opponent):
        if Player.TYPES[self.type_politique]["fort"] == opponent.type_politique:
            return base_damage * 1.5  # Dégâts augmentés de 50%
        elif Player.TYPES[self.type_politique]["faible"] == opponent.type_politique:
            return base_damage * 0.5  # Dégâts réduits de 50%
        return base_damage

    def cast_spell(self, spell_name, target):
        self.magic.cast_spell(spell_name, target)

    # méthode pour changer l'arme du joueur
    def set_weapon(self, weapon):
        self.weapon = weapon

    # méthode pour vérifier si le joueur a une arme
    def has_weapon(self):
        return self.weapon is not None

    # méthode pour changer l'armure du joueur
    def set_armor(self, armor):
        self.armor = armor

    # méthode pour vérifier si le joueur a une armure
    def has_armor(self):
        return self.armor is not None
