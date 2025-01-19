from player import Player
from weapon import Weapon
from Armor import Armor
from spell import Magic
from item import Item
from spell import Spell
import random

def simulate_combat():
    knife = Weapon("Couteau", 3, 10)
    player1 = Player("Philippe Poutoux", 20, 3, 20)
    sword = Weapon("Epée", 5, 12)

    shield = Armor("Bouclier", 2, 20)
    helmet = Armor("Casque", 1, 10)

    player1.add_item(Item("Potion de Soin", "heal"), 2)
    player1.add_item(Item("Potion de Mana", "mana"), 2)
    player1.add_item(Item("Grenade", "damage"), 2)

    player1.set_weapon(knife)
    player1.set_armor(shield)

    player2 = Player("Jean Castex", 50, 5, 20)
    player2.set_weapon(sword)
    player2.set_armor(helmet)

    while player1.get_health() > 0 and player2.get_health() > 0:
        # Choix aléatoire pour le joueur 1
        choix = random.randint(1, 4)
        if choix == 1:
            player1.attack_player(player2)
        elif choix == 2:
            player1.cast_spell("fireball", player2)
        elif choix == 3:
            player1.cast_spell("heal", player1)
        elif choix == 4:
            if not use_item(player1, player2):
                continue
        player2.attack_player(player1)

    return player1.get_health() > 0

def use_item(player, target):
    available_items = [item_name for item_name, quantity in player.inventory.items() if quantity > 0]
    if not available_items:
        return True  # Sortie de l'inventaire sans attaquer

    item_name = random.choice(available_items)
    player.use_item(item_name, target)
    return False

def main():
    num_simulations = 1000
    player1_wins = 0
    player2_wins = 0

    for _ in range(num_simulations):
        if simulate_combat():
            player1_wins += 1
        else:
            player2_wins += 1

    print(f"Player 1 wins: {player1_wins} out of {num_simulations} simulations")
    print(f"Player 2 wins: {player2_wins} out of {num_simulations} simulations")

if __name__ == "__main__":
    main()
