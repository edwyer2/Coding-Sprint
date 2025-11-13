import random

class Player:
    """Represents the player in the adventure game.
    
    Attributes:
        name (str): The player's name.
        location (str): Current location of the player.
        inventory (list): Items collected by the player.
        health (int): Player's health points.
        score (int): Player's score.
    """
    def __init__(self, name, location="starting point"):
        self.name = name
        self.location = location
        self.inventory = []
        self.health = 100
        self.score = 0

    def move(self, new_location):
        """Update player's location."""
        self.location = new_location
        print(f"{self.name} moved to {self.location}.")
    
    def show_status(self):
        """Display player's current stats and inventory."""
        print(f"\nPlayer: {self.name}")
        print(f"Location: {self.location}")
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}\n")
    
    def add_to_inventory(self, item):
        """Add an item to the player's inventory."""
        self.inventory.append(item)
        print(f"{item} added to inventory.")
    
    def remove_from_inventory(self, item):
        """Remove an item from the player's inventory if present."""
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} removed from inventory.")
        else:
            print(f"{item} not found in inventory.")

    def take_damage(self, damage):
        """Reduce player's health by damage amount."""
        self.health -= damage
        print(f"{self.name} took {damage} damage! Health is now {self.health}.")
    
    def heal(self, amount):
        """Increase player's health by heal amount."""
        self.health += amount
        print(f"{self.name} healed {amount} points! Health is now {self.health}.")
    
    def add_score(self, points):
        """Increase player's score by points (can be negative)."""
        self.score += points
        print(f"{points} points added! Score is now {self.score}.")

def random_encounter(player):
    """Randomly selects an encounter: monster, treasure, or ally.
    
    - Monster: Fight or run, affects health and score, may award loot.
    - Treasure: Gain loot and score.
    - Ally: Heal player.
    """
    event = random.choice(["monster", "treasure", "ally"])
    if event == "monster" :
        monster = random.choice(["Goblin", "Troll", "Dragon"])
        print (f"A wild {monster} appears!")
        action = input("Do you [fight] or [run]? ")
        if action.lower() == "fight":
            damage = random.randint(5,20)
            loot = random.choice (["Gold Coin", "Health Potion", "Magic Sword"])
            player.take_damage(damage)
            player.add_to_inventory(loot)
            player.add_score(10)
            print(f"You defeated the {monster} and found a {loot}!")
        elif action.lower() == "run":
            player.add_score(-5)
            player.take_damage(5)
            print("You escaped but lost some health and points.")
        else:
            player.add_score(-10)
            player.take_damage(10)
            print("You hesitated and the monster attacked you!")
    elif event == "treasure":
        treasure = random.choice (["Bag of Gold", "Magic Scroll", "Shield"])
        player.add_to_inventory(treasure)
        player.add_score(20)
        print(f"You found a treasure chest containing a {treasure}!")
    elif event == "ally":
        ally = random.choice (["Wise Old Man", "Brave Warrior", "Mystic Healer"])
        heal = random.randint(10,25)
        player.heal(heal)
        print(f"You met a {ally} who healed you for {heal} health points!") 

def explore_location(player, location):
    """Handles exploration of a specific location.
    
    Each location has unique events:
    - forest/cave: random encounter
    - village: heal and score
    - castle: artifact and score
    """
    player.move(location)
    print (f"You explore the {location}.")
    if location == "forest":
        random_encounter(player)
    elif location == "cave":
        print ("The cave is dark and eerie.")
        random_encounter(player)
    elif location == "village":
        print ("The village is peaceful. You rest and recover.")
        player.heal(10)
        player.add_score(5)
    elif location == "castle":
        print ("The castle is grand. You find a valuable artifact.")
        player.add_to_inventory("Ancient Artifact")
        player.add_score(30)
    else: 
        print ("This location is unfamiliar. Nothing happens.")
    
def show_help():
    """Display valid game commands."""
    print("\nValid commands:")
    print("explore [location] - Explore a location (forest, cave, village, castle)")
    print("status - Show player stats")
    print("inventory add [item] - Add item to inventory")
    print("inventory remove [item] - Remove item from inventory")
    print("help - Show this help message")
    print("quit - Exit the game\n")

def main():
    """Main game loop. Handles user input and game progression."""
    print("Welcome to the Adventure Game!")
    name = input("Enter your player name: ")
    player = Player(name)
    show_help()
    while True:
        command = input("> ").strip().lower()
        if command.startswith("explore"):
            parts = command.split()
            if len(parts) == 2 and parts[1] in ["forest", "cave", "village", "castle"]:
                explore_location(player, parts[1])
            else:
                print("Specify a valid location: forest, cave, village, castle.")
        elif command == "status":
            player.show_status()
        elif command.startswith("inventory add"):
            item = command.replace("inventory add", "").strip().title()
            if item:
                player.add_to_inventory(item)
            else:
                print("Specify an item to add.")
        elif command.startswith("inventory remove"):
            item = command.replace("inventory remove", "").strip().title()
            if item:
                 player.remove_from_inventory(item)
            else:
                print("Specify an item to remove.")
        elif command == "help":
            show_help()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' for a list of valid commands.")

if __name__ == "__main__":
    main()

# ---------------------------
# Usage Examples:
# ---------------------------
# > status
#   Shows your current health, score, location, and inventory.
#
# > explore forest
#   Moves you to the forest and triggers a random encounter.
#
# > inventory add torch
#   Adds "Torch" to your inventory.
#
# > inventory remove torch
#   Removes "Torch" from your inventory.
#
# > help
#   Lists all valid commands.
#
# > quit
#   Exits the game.
#
# ---------------------------
# Example unit test for inventory
def test_inventory_add():
    p = Player("Test")
    p.add_to_inventory("Sword")
    assert "Sword" in p.inventory

def test_take_damage():
    p = Player("Test")
    p.take_damage(10)
    assert p.health == 90
