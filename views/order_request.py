ORDERS = [
    {
        "metalId": 1,
        "sizeId": 3,
        "styleId": 1,
        "id": 1
    },
    {
        "metalId": 5,
        "sizeId": 1,
        "styleId": 1,
        "id": 2
    },
    {
        "metalId": 1,
        "sizeId": 1,
        "styleId": 1,
        "id": 3
    }
]

def get_all_orders():
    return ORDERS

def get_single_order(id):
    requested_order = None

    for order in ORDERS:
        if order["id"] == id:
            requested_order = order
    
    return requested_order

def place_order(order):
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order


def delete_order(id):
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Iterate the ORDERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)


def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break