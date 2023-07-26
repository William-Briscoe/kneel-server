import sqlite3
import json
from models import Order, Metal, Style, Size

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
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            m.metal metal_name,
            m.price metal_price,
            o.size_id,
            si.carets,
            si.price size_price,
            o.styles_id,
            st.style,
            st.price style_price
        FROM Orders AS o
        INNER JOIN Metals AS m ON m.id = o.metal_id
        INNER JOIN Sizes AS si ON si.id = o.size_id
        INNER join Styles AS st ON st.id = o.styles_id
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row['id'], row['metal_id'], row['size_id'], row['styles_id'])

            metal = Metal(row['metal_id'], row['metal_name'], row['metal_price'])
            order.metal = metal.__dict__
            size = Size(row['size_id'], row['carets'], row['size_price'])
            order.size = size.__dict__
            style = Style(row['styles_id'], row['style'], row['style_price'])
            order.style=style.__dict__

            orders.append(order.__dict__)
    return orders




def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.styles_id
        FROM Orders AS o
        WHERE o.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        order = Order(data['id'], data['metal_id'], data['size_id'], data['styles_id'])

        return order.__dict__

def place_order(order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            (metal_id, size_id, styles_id)
        VALUES
            (?, ?, ?);
        """, (order['metal_id'], order['size_id'], order['styles_id']))

        id = db_cursor.lastrowid

        order['id'] = id
    
    return order


def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor= conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break