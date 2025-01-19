from player import Player
from weapon import Weapon
from Armor import Armor
from spell import Magic
from item import Item
from spell import Spell
from fight import Combat
from time import sleep

knife = Weapon("Couteau", 3, 10)
player1 = Player("Philippe Poutoux", 20, 3, 20)
sleep(2)
sword = Weapon("Epée", 5, 12)

print("Comme chaque jour dans son usine, entouré de ses camarades, Philippe travaille pour l'amélioration du bien commun")
sleep(3)
print("Quand une odeur de défaite électoral particulièrement forte lui parvint")
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

player2 = Player("Manuel Lolita Valch", 10, 3, 20)
sleep(2)
player2.set_weapon(sword)
player2.set_armor(helmet)

print("Jean Castex : Tu es délocalisé dans un pays froid et pauvre, tu verras, tu t'y sentiras bien mieux")
sleep(3)
print("Philippe Poutoux : Ne sais tu pas que la lutte des classes n'a pas de frontière ?! ")
sleep(2)
combat1 = Combat(player1, player2)
if not combat1.fight():  # Si player1 perd, arrête tout
    exit()

print("Vous trouvez sur le corps étendu du vieux sudiste, des objets honteusement volés au peuple, ainsi que son épée de social traitre")
sleep(3)
print("Vous trouvez 2 potions de soin, 2 potions de Mana, 2 grenades, une épée et 3L de seum")
sleep(3)
print("De ce seum, émerge un nouvel être bien plus hérétique à toute imagerie socialiste")
sleep(3)
player1.add_item(Item("Potion de Soin", "heal"), 2)
player1.add_item(Item("Potion de Mana", "mana"), 2)
player1.add_item(Item("Grenade", "damage"), 2)
player1.set_weapon(sword)


player3 = Player("Jean Michel Darmanouch, le turgescent", 20, 2, 20)
sleep(2)
combat2 = Combat(player1, player3)
if not combat2.fight():  # Si player1 perd, arrête tout
    exit()