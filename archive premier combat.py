def attack1vs2():
    player1.attack_player(player2)
    print(player1.get_pseudo(), "attaque", player2.get_pseudo())

def attack2vs1():
    player2.attack_player(player1)
    print(player2.get_pseudo(), "attaque", player1.get_pseudo())

def use_item(player, target):
    while True:
        print("Choisir un objet à utiliser :")
        for idx, (item_name, quantity) in enumerate(player.inventory.items(), 1):
            print(f"{idx}. {item_name} (x{quantity})")
        print("4. Sortir de l'inventaire")

        choix_item = int(input("Saisir le numéro : "))
        if 1 <= choix_item <= len(player.inventory):
            item_name = list(player.inventory.keys())[choix_item - 1]
            player.use_item(item_name, target)
            break
        elif choix_item == 4:
            print("Sortie de l'inventaire.")
            return True  # Sortie de l'inventaire sans attaquer
        else:
            print("Choix invalide, veuillez réessayer.")
    return False  # Action effectuée

print("Nouveau combat entre : " + player1.get_pseudo() + " et " + player2.get_pseudo())

while player1.get_health() > 0 and player2.get_health() > 0:
    print("Choix 1 : attaque de " + player1.get_pseudo())
    print("Choix 2 : sort de flamme de a justice de " + player1.get_pseudo())
    print("Choix 3 : sort de lecture du manifeste du PC de " + player1.get_pseudo())
    print("Choix 4 : utiliser un objet de l'inventaire de " + player1.get_pseudo())

    choix = int(input("Saisir le numéro : "))
    if choix == 1:
        attack1vs2()
        attack2vs1()
    elif choix == 2:
        player1.cast_spell("fireball", player2)
        print("Hypocrite!")
        attack2vs1()
    elif choix == 3:
        player1.cast_spell("heal", player1)
        print("La guérison par l'instruction socialiste ! ")
        attack2vs1()
    elif choix == 4:
        if use_item(player1, player2):
            continue  # Si l'utilisateur choisit de sortir de l'inventaire, continuer sans attaquer
        attack2vs1()
    else:
        exit()

    print(player1.get_pseudo(), "/ Points de vie:", player1.get_health(), "/ Attaque:", player1.get_attack_value(),
          "/ Arme:", player1.weapon.get_name() if player1.has_weapon() else "Aucune", "/ Armure:",
          player1.armor.get_name() if player1.has_armor() else "Aucune", "/ Mana:", player1.magic.mana)
    print(player2.get_pseudo(), "/ Points de vie:", player2.get_health(), "/ Attaque:", player2.get_attack_value(),
          "/ Arme:", player2.weapon.get_name() if player2.has_weapon() else "Aucune", "/ Armure:",
          player2.armor.get_name() if player2.has_armor() else "Aucune")

    if player1.get_health() <= 0:
        print(player1.get_pseudo(), "a été vaincu!")
    if player2.get_health() <= 0:
        print(player2.get_pseudo(), "a été vaincu!")