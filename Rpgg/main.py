import os
import json
from player_character import Player
from map import Map

class Game:
    def __init__(self):
        self.player = None
        self.map = None  # La carte sera initialisée après la création du joueur
        self.save_file = "savegame.json"

    def display_menu(self):
        print("=======++Menu PRINCIPAL++=========")
        print("1. New Game")
        print("2. Load Game")
        print("3. Quit")
        print("=================================")

    def start_new_game(self):
        player_name = input("Entrez votre nom: ")
        self.player = Player(player_name)
        self.map = Map(self.player)  # Passer l'instance de Player à Map
        print(f"Bienvenue dans le jeu, {player_name}!")
        self.map.describe_location()
        self.save_game()
        self.game_loop()

    def game_loop(self):
        while self.player.is_alive():
            action = input("\nChoisissez votre direction (Go North, Go South, Go East, Go West, Quit, P pour la carte): ").lower()
            if action.startswith("go"):
                direction = action.split()[-1]
                if self.map.move(direction):
                    print(f"Vous avez déplacé vers le {direction}.")
                else:
                    print("Vous ne pouvez pas aller dans cette direction.")
            elif action == "p":
                self.map.display_ascii_map()
            elif action == "quit":
                self.quit_game()
                break
            else:
                print("Action non reconnue, veuillez réessayer.")

    def load_game(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, "r") as file:
                save = json.load(file)
                self.player = Player(save["player_name"])
                self.map = Map(self.player)
                self.map.current_location = save["current_location"]
                print(f"Bon retour, {save['player_name']}!")
                self.map.describe_location()
                self.game_loop()
        else:
            print("Aucun fichier de sauvegarde trouvé.")

    def save_game(self):
        data = {
            "player_name": self.player.name,
            "current_location": self.map.current_location
        }
        with open(self.save_file, "w") as file:
            json.dump(data, file)
        print("Jeu sauvegardé avec succès.")

    def quit_game(self):
        print("Au revoir!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Entrez votre choix: ")
            if choice == "1":
                self.start_new_game()
            elif choice == "2":
                self.load_game()
            elif choice == "3":
                self.quit_game()
                break
            else:
                print("Choix invalide. Veuillez sélectionner à nouveau.")

if __name__ == "__main__":
    game = Game()
    game.run()
































# import os
# import json
# from player_character import  Player 
# from map import Map

# print("Player class can be imported and used!")
# #player_instance = Player("Test")
# #print(player_instance)
# class Game:
#     def __init__(self):
#         self.player = None
#         self.map = Map()  # Initialize the game map
#         self.save_file = "savegame.json"

#     def display_menu(self):
#         print("=======++Menu PRINCIPAL++=========")
#         print("1. New Game")
#         print("2. Load Game")
#         print("3. Quit")
#         print("=================================")

#     def start_new_game(self):
#         player_name = input("Enter your name: ")
#         self.player = Player(player_name)  # Assuming Player inherits from Character
#         print(f"Welcome to the game, {player_name}!")
#         self.map.describe_location()
#         self.save_game()
#         self.game_loop()

#     def game_loop(self):
#         while self.player.is_alive():
#             action = input("\n§§ Choisissez votre direction §§ (Go North, Go South, Go East, Go West, Quit, P pour la carte): ").lower()
#             if action.startswith("go"):
#                 direction = action.split()[-1]
#                 if self.map.move(direction):
#                     print(f"Moving e {direction.capitalize()}.")
#                     self.map.check_events()
#                 else:
#                     print("You cannot go that way.")
#             elif action == "p":
#                 self.map.display_ascii_map()
#             elif action == "quit":
#                 self.quit_game()
#                 break
#             else:
#                 print("Action non reconnue, veuillez essayer à nouveau.")

#     def load_game(self):
#         if os.path.exists(self.save_file):
#             with open(self.save_file, "r") as file:
#                 save = json.load(file)
#                 self.player = Player(save["player_name"], save["player_health"], save["player_attack"], save["player_defense"])
#                 self.player.inventory = save.get("inventory", [])
#                 self.map.current_location = save["current_location"]
#                 print(f"Welcome back, {save['player_name']}!")
#                 self.map.describe_location()
#                 self.game_loop()
#         else:
#             print("No save file found.")

#     def save_game(self):
#         data = {
#             "player_name": self.player.name,
#             "player_health": self.player.hp,
#             "player_attack": self.player.attack,
#             "player_defense": self.player.defense,
#             "current_location": self.map.current_location,
#             "inventory": self.player.inventory
#         }
#         with open(self.save_file, "w") as file:
#             json.dump(data, file)
#         print("Game saved successfully.")

#     def quit_game(self):
#         print("Goodbye!")

#     def run(self):
#         while True:
#             self.display_menu()
#             choice = input("Enter your choice: ")
#             if choice == "1":
#                 self.start_new_game()
#             elif choice == "2":
#                 self.load_game()
#             elif choice == "3":
#                 self.quit_game()
#                 break
#             else:
#                 print("Choix invalide. Veuillez sélectionner à nouveau.")

# if __name__ == "__main__":
#     game = Game()
#     game.run()
