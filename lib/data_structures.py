# List of spicy foods (as given in the instructions)
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

# 1. get_names()
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# 2. get_spiciest_foods()
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# 3. print_spicy_foods()
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# 4. get_spicy_food_by_cuisine()
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)

# 5. print_spiciest_foods()
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

# 6. get_average_heat_level()
def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

# 7. create_spicy_food()
def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods

# Test Cases (for checking functionality)
if __name__ == "__main__":
    # Testing get_names
    print(get_names(spicy_foods))  # Expected output: ["Green Curry", "Buffalo Wings", "Mapo Tofu"]
    
    # Testing get_spiciest_foods
    print(get_spiciest_foods(spicy_foods))  # Expected output: [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}]
    
    # Testing print_spicy_foods
    print_spicy_foods(spicy_foods)
    # Expected output:
    # Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
    # Buffalo Wings (American) | Heat Level: 🌶🌶🌶
    # Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

    # Testing get_spicy_food_by_cuisine
    print(get_spicy_food_by_cuisine(spicy_foods, "American"))  # Expected output: {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3}
    print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))      # Expected output: {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}
    
    # Testing print_spiciest_foods
    print_spiciest_foods(spicy_foods)
    # Expected output:
    # Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
    # Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

    # Testing get_average_heat_level
    print(get_average_heat_level(spicy_foods))  # Expected output: 6

    # Testing create_spicy_food
    new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
    print(updated_spicy_foods)
    # Expected output:
    # [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}, {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}]
