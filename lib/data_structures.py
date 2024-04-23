spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [dictionary['name'] for dictionary in spicy_foods if 'name' in dictionary]
    return food_names

def get_spiciest_foods(spicy_foods):
    spicy_names = [dictionary for dictionary in spicy_foods if 'name' in dictionary and dictionary['heat_level'] > 5]
    return spicy_names

def print_spicy_foods(spicy_foods):
    for dictionary in spicy_foods:
        heat = dictionary["heat_level"]
        emoji = "🌶" * heat
        print(f"{dictionary['name']} ({dictionary['cuisine']}) | Heat Level: {emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return(food)

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat = food["heat_level"]
        emoji = "🌶" * heat
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    num_foods = len(spicy_foods)
    for food in spicy_foods:
        total_heat += food["heat_level"]
    avg_heat = total_heat/num_foods
    return avg_heat

def create_spicy_food(spicy_foods, spicy_food):
    new_food ={
         'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }

    spicy_foods.append(new_food)
    return spicy_foods
