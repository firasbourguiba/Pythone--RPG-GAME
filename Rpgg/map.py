from player_character import Monster
from combat import Combat

class Map:
    def __init__(self, player):
        self.player = player
        self.locations = {
            "Forest Entrance": {"description": "Entrée de la forêt", "north": "Deep Forest", "events": ["monster_encounter"]},
            "Deep Forest": {"description": "Forêt profonde", "south": "Forest Entrance", "east": "Lake", "west": "Mountain Path", "events": ["monster_encounter"]},
            "Lake": {"description": "Lac calme", "west": "Deep Forest", "events": ["special_event"]},
            "Mountain Path": {"description": "Sentier de montagne", "east": "Deep Forest", "north": "Mountain Peak", "events": []},
            "Mountain Peak": {"description": "Sommet de la montagne", "south": "Mountain Path", "events": ["boss_fight"]}
        }
        self.current_location = "Forest Entrance"

    def move(self, direction):
        if direction in self.locations[self.current_location]:
            self.current_location = self.locations[self.current_location][direction]
            self.describe_location()
            self.display_ascii_map()
            self.check_events()
            return True
        else:
            return False

    def describe_location(self):
        location = self.locations[self.current_location]
        print(f"\nVous êtes maintenant à : {self.current_location}")
        print(location["description"])

    def display_ascii_map(self):
        map_ascii = {
            "Mountain Peak": "       [Mountain Peak]",
            "Mountain Path": "             |",
            "Forest Entrance": "[Forest Entrance] - [Deep Forest] - [Lake]",
            "Deep Forest": "                  |",
            "Lake": "           [Lake]"
        }
        print("\n=== Carte ===")
        for location, line in map_ascii.items():
            if location == self.current_location:
                print(f"{line} <- Vous êtes ici")
            else:
                print(line)
        print("=============\n")

    def check_events(self):
        events = self.locations[self.current_location].get("events", [])
        for event in events:
            if event == "monster_encounter":
                self.encounter_monster()
            elif event == "special_event":
                self.special_event()
            elif event == "boss_fight":
                self.boss_fight()

    def encounter_monster(self):
        monster = Monster("Orc", health=100, attack=15, defense=5)
        combat = Combat(self.player, monster)
        combat.run()

    def special_event(self):
        print("Un événement spécial a été déclenché!")

    def boss_fight(self):
        boss = Monster("Dragon", health=300, attack=40, defense=20)
        combat = Combat(self.player, boss)
        combat.run()


























# from player_character import Monster
# from combat import Combat


# class Map:
#     def __init__(self):
#         self.locations = {
#             "Forest Entrance": {
#                 "description": "Entrée de la forêt",
#                 "north": "Deep Forest",
#                 "events": ["monster_encounter"]
#             },
#             "Deep Forest": {
#                 "description": "Forêt profonde",
#                 "south": "Forest Entrance",
#                 "east": "Lake",
#                 "west": "Mountain Path",
#                 "events": [ "monster_encounter"]
#             },
#             "Lake": {
#                 "description": "Lac calme",
#                 "west": "Deep Forest",
#                 "events": ["special_event"]
#             },
#             "Mountain Path": {
#                 "description": "Sentier de montagne",
#                 "east": "Deep Forest",
#                 "north": "Mountain Peak",
#                 "events": []
#             },
#             "Mountain Peak": {
#                 "description": "Sommet de la montagne",
#                 "south": "Mountain Path",
#                 "events": ["boss_fight"]
#             }
#         }
#         self.current_location = "Forest Entrance"

#     def display_ascii_map(self):
#         # Carte ASCII représentant la position actuelle du joueur
#         map_ascii = {
#             "Mountain Peak": "       [Mountain Peak]",
#             "Mountain Path": "             |",
#             "Forest Entrance": "[Forest Entrance] - [Deep Forest] - [Lake]",
#             "Deep Forest": "                  |",
#             "Lake": "           [Lake]"
#         }

#         print("\n=== Carte ===")
#         for location, line in map_ascii.items():
#             if location == self.current_location:
#                 print(f"{line} <- Vous êtes ici")
#             else:
#                 print(line)
#         print("=============\n")

#     def move(self, direction):
#         if direction in self.locations[self.current_location]:
#             self.current_location = self.locations[self.current_location][direction]
#             print(f"Vous vous déplacez vers le {direction}.")
#             self.describe_location()
#             self.display_ascii_map()  # Affiche la carte ASCII après chaque déplacement
#             self.check_events()
#         else:
#             print("Vous ne pouvez pas aller dans cette direction.")

#     def describe_location(self):
#         location = self.locations[self.current_location]
#         print(f"\nVous êtes maintenant à : {self.current_location}")
#         print(location["description"])


#     # events
#     def check_events(self):
#         print("check for events")
#         # Get events for the current location
        
#         events = self.locations[self.current_location].get("events", [])
#         for event in events:
#             if event == "monster_encounter":
#                 self.encounter_monster()
#             elif event == "special_event":
#                 self.special_event()
#             elif event == "boss_fight":
#                 self.boss_fight()


 

    

#     def special_event(self):
#         print("You've triggered a special event!")

#     def boss_fight(self):
#         print("You face the boss of the mountain peak!")
 
#  # exemple event monster 
# def encounter_monster(self):
        
#         monster = Monster("Orc", health=100, attack=15, defense=10)
        
#         player = self.get_player() 
#         combat = Combat(player, monster)
#         combat.start()
#         if not player.is_alive():
#             print("Game Over! You were defeated by the monster.")
#         else:
#             print("You defeated the monster and continue your adventure.")
#find_item
#class Item:
 #   def __init__(self, name, effect, rarity):
  #      self.name = name
   #     self.effect = effect
    #    self.rarity = rarity
    

#items_available = [
 #   Item("Épée de flamme", "augmente l'attaque de 10 points", "rare"),
  #  Item("Potion de soin", "restaure 50 points de vie", "commun"),
   # Item("Bouclier ancien", "augmente la défense de 5 points", "peu commun"),
    #Item("Amulette de chance", "augmente la chance de coup critique", "rare")
#]

#def choose_random_item(items):
 #   weights = {'commun': 70, 'peu commun': 20, 'rare': 10}
  #  total_weight = sum(weights[item.rarity] for item in items)
   # chosen = random.choices(items, weights=[weights[item.rarity] for item in items], k=1)
    #return chosen[0]

#def find_item(self):
 #   found_item = choose_random_item(items_available)
  #  self.player.add_item(found_item)
   # print(f"Vous avez trouvé un objet caché : {found_item.name} qui {found_item.effect}!")


# ---------------------------------------------------------------------------------------------------


