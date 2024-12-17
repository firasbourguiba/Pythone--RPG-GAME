from player_character import Monster
from player_character import Player

import random


class Combat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def run(self):
        """till the death."""
        print(f"A wild {self.monster.name} appears!")
        while self.player.is_alive() and self.monster.is_alive():
            if self.player_turn():
                break  # Exit the combat loop if player escapes
            if self.monster.is_alive():
                self.monster_turn()

        """ Manage the player's turn during the combat. """

    def player_turn(self):
        """Manage the player's turn during the combat."""
        action = input(
            "Choose your action: Attack, Use Item, Power Strike, Healing Wave, Run: "
        ).lower()
        if action == "attack":
            self.player.attack_target(self.monster)
        elif action == "power strike":
            self.player.power_strike(self.monster)
        elif action == "healing wave":
            self.player.healing_wave()
        elif action == "use item":
            item = input("Enter the item to use: ")
            self.player.use_item(item)
        elif action == "run":
            if self.player.attempt_to_escape():
                print("You successfully escaped!")
                return True
            else:
                print("Failed to escape!")
        self.player.end_turn()  # Handle cooldowns and mana regeneration
        return False

    def monster_turn(self):
        """Monster's turn to attack."""
        if random.random() > 0.1:  # 90% chance to hit
            self.monster.attack_target(self.player)
            if not self.player.is_alive():
                print("You have been defeated.")
        else:
            print(f"{self.monster.name} You dodged  the attack.")


# Function to handle random encounters
def random_encounter(player):
    encounter_type = random.choice(["monster", "item"])
    if encounter_type == "monster":
        # Create a monster with random attributes
        monster = Monster("Goblin", health=50, attack=20, defense=10)
        combat = Combat(player, monster)
        combat.run()
    elif encounter_type == "item":
        find_item(player)


# Function to find an item
def find_item(player):
    items = ["health potion", "strength potion", "shield"]
    found_item = random.choice(items)
    print(f"You found a {found_item}!")
    player.add_item(found_item)
