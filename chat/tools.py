from .models import Item


def get_item(item_name: str):
    """Get the quantity and price of an inventory item."""

    item = Item.objects.filter(name__iexact=item_name.strip()).first()

    if item is None:
        item = Item.objects.filter(name__icontains=item_name.strip()).first()

    if item is None:
        return {
            "found": False,
            "message": "Item not found in inventory."
        }

    return {
        "found": True,
        "name": item.name,
        "quantity": item.quantity,
        "price": float(item.price),
    }