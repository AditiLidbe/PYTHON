def add_item(current_cart, items_to_add):
    """
    Add items to shopping cart.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1

    return current_cart


def read_notes(notes):
    """
    Create user cart from iterable notes.
    """
    cart = {}

    for item in notes:
        cart[item] = 1

    return cart


def update_recipes(ideas, recipe_updates):
    """
    Update the recipe ideas dictionary.
    """
    for recipe_name, ingredients in recipe_updates:
        ideas[recipe_name] = ingredients

    return ideas


def sort_entries(cart):
    """
    Return new cart sorted alphabetically.
    """
    sorted_cart = {}

    for item in sorted(cart):
        sorted_cart[item] = cart[item]

    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """
    Combine cart with aisle and refrigeration info.
    Sort in reverse alphabetical order.
    """
    fulfillment = {}

    for item in sorted(cart, reverse=True):
        quantity = cart[item]
        aisle = aisle_mapping[item][0]
        refrigeration = aisle_mapping[item][1]

        fulfillment[item] = [quantity, aisle, refrigeration]

    return fulfillment


def update_store_inventory(fulfillment_cart, store_inventory):
    """
    Reduce store inventory based on fulfillment cart.
    Replace quantity with 'Out of Stock' if reaches 0.
    """
    for item in fulfillment_cart:
        ordered_quantity = fulfillment_cart[item][0]
        store_quantity = store_inventory[item][0]

        if isinstance(store_quantity, int):
            new_quantity = store_quantity - ordered_quantity

            if new_quantity <= 0:
                store_inventory[item][0] = 'Out of Stock'
            else:
                store_inventory[item][0] = new_quantity

    return store_inventory