from time import sleep
import random

class Combat:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def fight(self):
        print(f"Nouveau combat entre : {self.player1.get_pseudo()} et {self.player2.get_pseudo()}")
        sleep(0.5)
        while self.player1.get_health() > 0 and self.player2.get_health() > 0:
            # Continue le tour du joueur tant qu'aucune action finale n'a été prise
            action_taken = False
            while not action_taken:
                action_taken = self.player_turn(self.player1, self.player2)
            if self.player2.get_health() > 0:
                self.enemy_turn(self.player2, self.player1)
            self.display_status()

        if self.declare_winner():
            self.player1.gain_experience(100)  # Par exemple, le joueur gagne 100 XP par combat gagné
            return True
        else:
            return False

    def player_turn(self, player, opponent):
        print("Choix 1 : Attaque")
        sleep(0.3)
        print("Choix 2 : Utiliser un sort")
        sleep(0.3)
        print("Choix 3 : Utiliser un objet de l'inventaire")
        sleep(0.3)

        choice = int(input("Saisir le numéro de votre action : "))
        if choice == 1:
            damage = player.attack_player(opponent)
            print(f"{player.get_pseudo()} attaque {opponent.get_pseudo()} et inflige {damage} points de dégâts.")
            return True
        elif choice == 2:
            return self.use_spell(player, opponent)
        elif choice == 3:
            return self.use_item(player, opponent)
        return False

    def use_spell(self, player, opponent):
        available_spells = {1: "fireball", 2: "heal"}
        print("Choisir un sort à utiliser :")
        if not player.spells_unlocked:
            print("Aucun sort disponible.")
            sleep(2)
            return False
        print("Choix 1 : Sort de flamme de la justice" if player.can_cast_spell("fireball") else "Choix 1 : Sort indisponible")
        sleep(0.3)
        print("Choix 2 : Sort de lecture du manifeste du PC" if player.can_cast_spell("heal") else "Choix 2 : Sort indisponible")
        sleep(0.3)
        print("Choix 3 : Sortir du choix des sorts")
        sleep(0.3)

        spell_choice = int(input("Saisir le numéro de votre action : "))
        if spell_choice == 1 and player.can_cast_spell("fireball"):
            player.cast_spell("fireball", opponent)
            return True
        elif spell_choice == 2 and player.can_cast_spell("heal"):
            player.cast_spell("heal", player)
            return True
        elif spell_choice == 3:
            return False
        print("Choix invalide.")
        return False

    def enemy_turn(self, enemy, target):
        damage = enemy.get_attack_value()
        target.damage(damage)
        sleep(0.5)
        print(f"{enemy.get_pseudo()} attaque {target.get_pseudo()} et inflige {damage} points de dégâts.")
        sleep(1)

    def use_item(self, player, target):
        print("Choisir un objet à utiliser :")
        items_count = len(player.inventory.items())
        for idx, (item_name, quantity) in enumerate(player.inventory.items(), 1):
            print(f"{idx}. {item_name} (x{quantity})")
            sleep(0.3)
        print(f"{items_count + 1}. Sortir de l'inventaire")
        sleep(0.3)

        choix_item = int(input("Saisir le numéro : "))
        if 1 <= choix_item <= items_count:
            item_name = list(player.inventory.keys())[choix_item - 1]
            player.use_item(item_name, player, target)  # Passe le joueur comme utilisateur
            return True
        elif choix_item == items_count + 1:
            print("Sortie de l'inventaire.")
            return False
        return False

    def display_status(self):
        sleep(0.5)
        print(f"{self.player1.get_pseudo()} / Points de vie: {self.player1.get_health()}, Mana: {self.player1.magic.mana}")
        sleep(0.5)
        print(f"{self.player2.get_pseudo()} / Points de vie: {self.player2.get_health()}, Mana: {self.player2.magic.mana}")

    def declare_winner(self):
        if self.player1.get_health() > 0:
            print(f"{self.player1.get_pseudo()} a gagné le combat!, La lutte des classes continue")
            sleep(2)
            return True
        else:
            print(f"{self.player2.get_pseudo()} a gagné le combat! La lutte continue, mais sans toi, Philippe...")
            print("Game Over")
            return False
