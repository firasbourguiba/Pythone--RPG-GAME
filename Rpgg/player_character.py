import random

class Character:
    def __init__(self, name, health=100, attack=10, defense=5):
        self.name = name
        self.hp = health  # Health points
        self.attack = attack  # Attack power
        self.defense = defense  # Defense
        self.level = 1  # Initial level
        self.xp = 0  # Initial experience
        self.next_level_xp = 100  # XP required for the next level
        self.alive_status = True  # True if the character is alive

    def display_stats(self):
        print(f"======= Stats of {self.name} =======")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp}/{self.next_level_xp}")
        print("===================================")

    def gain_xp(self, xp_amount):
        self.xp += xp_amount
        print(f"{self.name} gained {xp_amount} XP.")
        self.check_level_up()

    def check_level_up(self):
        while self.xp >= self.next_level_xp:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 25
        self.xp -= self.next_level_xp
        self.next_level_xp += 50
        self.attack += 5
        self.defense += 3
        print(f"{self.name} leveled up to {self.level}!")

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp -= actual_damage
        print(f"{self.name} took {actual_damage} damage.")
        if self.hp <= 0:
            self.alive_status = False
            print(f"{self.name} has been defeated.")

    def is_alive(self):
        return self.hp > 0

    def attack_target(self, target):
        """Attack another character."""
        print(f"{self.name} attacks {target.name} with {self.attack} power.")
        target.take_damage(self.attack)


class Player(Character):
    def __init__(self, name, health=100, attack=10, defense=5):
        super().__init__(name, health, attack, defense)
        self.inventory = []  # Inventory to store items
        self.mana = 100  # Mana points for using special attacks
        self.heal_cooldown = 0  # Cooldown for healing wave ability

    def use_item(self, item):
        if item in self.inventory:
            print(f"{self.name} used {item}")
            self.inventory.remove(item)
        else:
            print(f"{self.name} does not have {item}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} received {item}")

    def power_strike(self, target):
        if self.mana >= 20:
            damage = self.attack * 2
            self.mana -= 20
            target.take_damage(damage)
            print(
                f"{self.name} uses Power Strike on {target.name}, dealing {damage} damage!"
            )
        else:
            print("Not enough mana to perform Power Strike.")

    def healing_wave(self):
        """Heal the player for 50 points, with a cooldown of 5 turns."""
        if self.heal_cooldown == 0:  # Ensure healing wave is off cooldown
            self.hp += 50  # Restore 50 health points
            self.hp = min(self.hp, 100)  # Cap health at max (100 by default)
            self.heal_cooldown = 5  # Set cooldown to 5 turns
            print(
                f"{self.name} uses Healing Wave and restores 50 health points. Current HP: {self.hp}"
            )
        else:
            print(f"Healing Wave is on cooldown for {self.heal_cooldown} more turns.")

    def attempt_to_escape(self):
        """Attempts to escape from combat with a 50% chance of success."""
        success = random.random() < 0.5  # 50% chance to escape
        if success:
            print(f"{self.name} successfully escaped from combat!")
        else:
            print(f"{self.name} failed to escape!")
        return success

    def end_turn(self):
        """Handle end-of-turn effects such as cooldown reduction and mana regeneration."""
        # Reduce cooldown for healing wave if it's active
        if self.heal_cooldown > 0:
            self.heal_cooldown -= 1
        # Regenerate a small amount of mana at the end of each turn
        self.mana = min(100, self.mana + 10)  # Regenerate 10 mana, maxing out at 100
        print(f"{self.name} regenerates 10 mana. Current mana: {self.mana}")


class Monster(Character):
    def __init__(self, name, health, attack, defense, difficulty="easy"):
        super().__init__(name, health, attack, defense)
        self.difficulty = difficulty


# # player_character.py


# class Character:
#     def __init__(self, name, health=100, attack=10, defense=5):
#         self.name = name
#         self.hp = health  # Health points
#         self.attack = attack  # Attack power
#         self.defense = defense  # Defense
#         self.level = 1  # Initial level
#         self.xp = 0  # Initial experience
#         self.next_level_xp = 100  # XP required for the next level
#         self.alive_status = True  # Renamed from is_alive to avoid conflict

#     def display_stats(self):
#         print(f"======= Stats of {self.name} =======")
#         print(f"HP: {self.hp}")
#         print(f"Attack: {self.attack}")
#         print(f"Defense: {self.defense}")
#         print(f"Level: {self.level}")
#         print(f"XP: {self.xp}/{self.next_level_xp}")
#         print("===================================")

#     def gain_xp(self, xp_amount):
#         """Gain XP and check if the level increases."""
#         self.xp += xp_amount
#         print(f"{self.name} gained {xp_amount} XP.")
#         self.check_level_up()

#     def check_alive(self):
#         """Return True if the character is still alive."""
#         return self.hp > 0

#     def level_up(self):
#         """Increase character's level and stats."""
#         self.level += 1
#         self.hp += 25
#         self.xp -= self.next_level_xp
#         self.next_level_xp += 50
#         self.attack += 5
#         self.defense += 3
#         print(f"{self.name} leveled up to {self.level}!")

#     def take_damage(self, damage):
#         """Take damage after reduction by defense."""
#         actual_damage = max(0, damage - self.defense)
#         self.hp -= actual_damage
#         print(f"{self.name} took {actual_damage} damage. Remaining HP: {self.hp}")
#         if self.hp <= 0:
#             self.alive_status = False  # Use the renamed attribute
#             print(f"{self.name} has been defeated.")

#     def attack_target(self, target):
#         """Attack another character."""
#         print(f"{self.name} attacks {target.name} with {self.attack} power.")
#         target.take_damage(self.attack)

#     def is_alive(self):
#         """Return True if the character is still alive."""
#         return self.hp > 0
#     pass
# # class items
# # the hero
# class Player(Character):
#     def __init__(self, name, health=100, attack=10, defense=5):
#         super().__init__(name, health, attack, defense)
#         self.inventory = [] # inventory for stock iteams
#         self.mana = 100  # Mana points for using special attacks
#         self.heal_cooldown = 0  # Cooldown for healing wave

#     def power_strike(self, target):
#         """Perform a power strike that does double damage."""
#         if self.mana >= 20:
#             damage = self.attack * 2
#             print(f"{self.name} uses Power Strike on {target.name}, dealing {damage} damage!")
#             self.mana -= 20
#             target.take_damage(damage)
#         else:
#             print("Not enough mana to perform Power Strike.")
#     def healing_wave(self):
#         """Heal self for 50 points, can only be used every 5 turns."""
#         if self.heal_cooldown == 0:
#             self.hp += 50
#             self.heal_cooldown = 5
#             print(f"{self.name} uses Healing Wave and restores 50 health points.")
#         else:
#             print(f"Healing Wave not available. Cooldown: {self.heal_cooldown} turns.")

#     def end_turn(self):
#         """Reduce cooldowns and regenerate some mana at the end of each turn."""
#         if self.heal_cooldown > 0:
#             self.heal_cooldown -= 1
#         self.mana += 10  # Regenerate 10 mana each turn, can adjust based on balance needs


#     def add_items(self , item):
#         """ ADD object for your inventaire."""
#         self.inventory.append(item)
#         print(f'{self.name}  get {item}')

#     def use_item(self, item):# fix this fonct remove 1 items evry time he use it
#         """ Use your object"""
#         if item in self.inventory :
#             print(f'{self.name} used {item}')
#             self.inventory.remove(item)
#         else:
#             print(f"{item} you don't have it ")

#     def player_turn(self):
#         """Allow player to choose an action including special attacks."""
#         action = input("Choose your action: Attack, Use Item, Power Strike, Healing Wave, Run: ").lower()
#         if action == 'attack':
#             self.attack_target(self.monster)
#         elif action == 'power strike':
#             self.power_strike(self.monster)
#         elif action == 'healing wave':
#             self.healing_wave()
#         elif action == 'use item':
#             item = input("Enter the item to use: ")
#             self.use_item(item)
#         elif action == 'run':
#             self.attempt_to_escape()
#         self.end_turn()  # Handle cooldowns and mana regeneration
#     pass
# # class monster
# class Monster(Character):
#     def __init__(self, name, health, attack, defense, difficulty="easy"):
#         super().__init__(name, health, attack, defense)
#         self.difficulty = difficulty
#         self.reward = "xp"
#     pass

# #Vendor
# class Vedor(Character):
#     def __init__(self, name,):
#         super().__init__(name,)
#         self.items_for_sale = {"Potion": 5, "sword":50 , "shield": 30}

#     def display_items(self):
#         """Give you money to survive"""# show all the items for sales
#         for item, price in self.items_for_sale():
#             print(f"{item}: {price} gold")

#     def sell_item(self, item, player):
#         """thank you for  your money hihihihihihi """
#         if item in self.items_for_sale:#for evry items there is special comment +
#             print(f"nice chose")
#             player.add_item(item)
#         else:
#             print(f"nooooooo but if you have more money tell me ")
#     pass

# #NLC
# class NPC(Character):
#     def __init__(self, name):
#         super().__init__(name, health=100)

#         def talk(self):
#             """Simple interaction with the player"""
#             print(f'{self.name} says: hello , adventure' )
#     pass
