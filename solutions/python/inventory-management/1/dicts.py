def create_inventory(items):
    """
    Create a dict that tracks the amount (count) of each element in items list.
    """
    inventory = {}

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def add_items(inventory, items):
    """
    Add or increment items in inventory using elements from items list.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """
    Remove 1 from an item count for each time it appears in items list.
    Count must not fall below 0.
    """
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    """
    Remove an item and its count entirely from inventory.
    If item not found, return inventory unchanged.
    """
    if item in inventory:
        del inventory[item]

    return inventory


def list_inventory(inventory):
    """
    Return list of (item, quantity) tuples.
    Include only items with quantity > 0.
    Sorted alphabetically by item name.
    """
    result = []

    for item in sorted(inventory):
        if inventory[item] > 0:
            result.append((item, inventory[item]))

    return result