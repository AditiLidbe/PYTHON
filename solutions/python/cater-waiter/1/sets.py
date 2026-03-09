from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`."""
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append 'Cocktail' or 'Mocktail' to drink_name."""
    ingredients_set = set(drink_ingredients)

    if ingredients_set & ALCOHOLS:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize dish based on ingredient set."""
    if dish_ingredients.issubset(VEGAN):
        category = "VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        category = "VEGETARIAN"
    elif dish_ingredients.issubset(PALEO):
        category = "PALEO"
    elif dish_ingredients.issubset(KETO):
        category = "KETO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    """Return dish name and special ingredients."""
    dish_name, ingredients = dish
    ingredients_set = set(ingredients)

    special = ingredients_set & SPECIAL_INGREDIENTS

    return (dish_name, special)


def compile_ingredients(dishes):
    """Return master ingredient set from all dishes."""
    master_set = set()

    for dish in dishes:
        master_set |= dish

    return master_set


def separate_appetizers(dishes, appetizers):
    """Remove appetizer dishes from dishes list."""
    dishes_set = set(dishes)
    appetizers_set = set(appetizers)

    remaining = dishes_set - appetizers_set

    return list(remaining)


def singleton_ingredients(dishes, intersection):
    """Return ingredients that appear in only one dish."""
    all_ingredients = set()

    for dish in dishes:
        all_ingredients |= dish

    # Singleton ingredients = all ingredients - intersection ingredients
    return all_ingredients - intersection