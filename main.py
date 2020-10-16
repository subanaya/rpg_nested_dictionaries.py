# Course: CS 30
# Period: 1
# Date Created: 20/10/14
# Date Last Modified: 20/10/14
# Name: Subanaya Thirunavukkarasu
# Description: Add properties to your characters, locations and
# inventory to your text-based adventure game using nested dictionaries


# Characters and traits
# The dictionary for characters
characters = {
    'Evelyn': {
        'adjective': 'ambitious',
        'skills': 'strength',
        'health_points': '150'
        },
    'Avery': {
        'adjective': 'funny',
        'skills': 'speed',
        'health_points': '100'
        }
  }
# Printing out the character descriptions
for character, description in characters.items():
    Adjective = description['adjective']
    Skills = description['skills']
    Health_points = description['health_points']

    print(f"{character} is {Adjective}.")
    print(f"{character}'s skill is {Skills}.")
    print(f"{character} has {Health_points} health points.")
    print("\n")


# Inventory and characteristics
# Evelyn's Inventory
print("Evelyn's Inventory:")
# The dictionary for Evelyn's inventory
evelyn_inventory = {
    'dagger': {
        'description': 'An old but sharp dagger',
        'damage': '30',
        'healing': '0'
        },
    'rotten apple': {
        'description': 'A commonly found health item',
        'damage': '0',
        'healing': '5'
        },
    'red potion': {
        'description': 'A potion that damages enemies',
        'damage': '40',
        'healing': '0'
        }
  }
# Printing out the inventory
for item, stats in evelyn_inventory.items():
    Description = stats['description']
    Damage = stats['damage']
    Healing = stats['healing']

    print(f"* {item.title()}")
    print(f"Description: {Description}")
    print(f"Damage: {Damage}")
    print(f"Healing: {Healing}")
    print("\n")

# Avery's Inventory
print("Avery's Inventory:")
# The dictionary for Avery's inventory
avery_inventory = {
    'glowstick': {
        'description': 'Releases posion when it breaks through skin',
        'damage': '20',
        'healing': '0'
        },
    'bubble gum': {
        'description': 'Hubba bubba bubble gum',
        'damage': '0',
        'healing': '25'
        },
    'green potion': {
        'description': 'An incredibly rare healing potion',
        'damage': '0',
        'healing': '100'
        }
    }
# Printing out the inventory
for item, stats in avery_inventory.items():
    Description = stats['description']
    Damage = stats['damage']
    Healing = stats['healing']

    print(f"* {item.title()}")
    print(f"Description: {Description}")
    print(f"Damage: {Damage}")
    print(f"Healing: {Healing}")
    print("\n")

# Locations and Descriptions
# The dictionary for locations
locations = {
            "Sewer": "underneath the city",
            "Shopping Centre": "in the middle of the city",
            "Scrap Yard": "in the east of the city",
            "Oxygen Station": {"South of the city", "North of the city"}
            }
# Printing out location statements
for location in locations:
    place = locations[location]
    if location == "Oxygen Station":
        oxygen_location = locations["Oxygen Station"]
        print(f"{location} is located in the:")
        for results in oxygen_location:
            print(f"{results}")
    else:
            print(f"{location} is located {place}")
print("\n")
