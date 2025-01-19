from player import Player
from weapon import Weapon
from Armor import Armor
from spell import Magic
from item import Item
from spell import Spell
from fight import Combat
from time import sleep


class Dialogue:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.scenes = {
            1: {
                'text': "Vous rencontrez Manuel Lolita Valch. Que dites-vous?",
                'choices': [
                    (1, "Tu penses pouvoir viser un mandat électoral à la CGT Manuel ? Le seum qui te ronge t'a t il fait descendre si bas ?"),
                    (2, "La France, l'Espagne... ces voyages doivent t'épuiser, un petit séjour au goulag ne pourra que te reposer")
                ],
                'responses': {
                    1: (None, "Il m'épuise. Laisse moi te rejoindre, te servir et je pourrais être utile."),
                    2: (None, "Tente toujours, je serai élu miss Sibérie et je reviendrai bien plus fort.")
                }
            }
        }

    def start(self):
        scene_id = 1
        while scene_id:
            scene = self.scenes[scene_id]
            print(scene['text'])
            sleep(2)
            for choice in scene['choices']:
                print(f"{choice[0]}: {choice[1]}")
                sleep(2)
            choice_number = int(input("Votre choix : "))
            _, outcome = scene['responses'][choice_number]
            print(outcome)
            sleep(2)

            if choice_number == 1:
                self.player1.add_item(Item("Potion de Soin", "heal"), 1)
                self.player1.add_item(Item("Potion de Mana", "mana"), 1)
                self.player1.add_item(Item("Grenade", "damage"), 1)
                print("Ajoute 1 potion de soin, 1 potion de mana et une grenade à ton équipement")
            elif choice_number == 2:
                combat1 = Combat(self.player1, self.player2)
                if not combat1.fight():  # Si player1 perd, arrête tout
                    print("Game Over")
                    break
                else:
                    # Événements après un combat réussi
                    print("Vous trouvez sur le corps étendu du vieux Catalan, des objets honteusement volés au peuple, ainsi que son épée de social traître")
                    sleep(3)
                    print("Vous trouvez 2 potions de soin, 2 potions de Mana, 2 grenades, une épée et 3L de seum")
                    sleep(3)
                    print("De ce seum, émerge un nouvel être bien plus hérétique à toute imagerie socialiste")
                    sleep(3)
                    self.player1.add_item(Item("Potion de Soin", "heal"), 2)
                    self.player1.add_item(Item("Potion de Mana", "mana"), 2)
                    self.player1.add_item(Item("Grenade", "damage"), 2)
                    self.sword = Weapon("Epée", 5, 12)
                    self.player1.set_weapon(self.sword)
            scene_id = None  # Fin du dialogue