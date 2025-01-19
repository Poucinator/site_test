from player import Player
from weapon import Weapon
from Armor import Armor
from spell import Magic
from item import Item
from spell import Spell
from fight import Combat
from time import sleep
from Dialogue import Dialogue

knife = Weapon("Couteau", 3, 10)
player1 = Player("Philippe Poutoux", 30, 3, 20,"Prolétariat")
sleep(2)
sword = Weapon("Epée", 5, 12)

print("Comme chaque jour dans son usine, entouré de ses camarades, Philippe travaille pour l'amélioration du bien commun")
sleep(3)
print("Quand une odeur de défaite électorale et de guacamol périmé lui parvint")
sleep(2)

# Création d'armures
shield = Armor("Bouclier", 2, 40)
helmet = Armor("Casque", 3, 30)

# Ajout d'objets dans l'inventaire
player1.add_item(Item("Potion de Soin", "heal"), 1)
player1.add_item(Item("Potion de Mana", "mana"), 1)
player1.add_item(Item("Grenade", "damage"), 1)

player1.set_weapon(knife)
player1.set_armor(shield)

player2 = Player("Manuel Lolita Valch", 6, 3, 50,"Populisme")
sleep(2)
player2.set_weapon(sword)
player2.set_armor(helmet)

dialogue = Dialogue(player1, player2)
dialogue.start()

player3 = Player("Jean Michel Darmanouch, le turgescent", 20, 2, 20,"Fascisme")
sleep(2)
combat2 = Combat(player1, player3)
if not combat2.fight():  # Si player1 perd, arrête tout
    exit()
