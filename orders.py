from flask import make_response, abort
from config import db
from models import Orders, OrderSchema


def read_all():
    """
    This function responds to a request for /api/orders
    with the complete lists of orders
    :return:        json string of list of orders
    """
    # Create the list of orders from our data
    orders = Orders.query.order_by(Orders.Order_ID).all()

    # Serialize the data for the response
    order_schema = OrderSchema(many=True)
    data = order_schema.dump(orders).data
    return data


def create(order):
    """
    This function creates a new order in the orders structure
    based on the data passed as order
    :param order:  order to create in orders structure
    :return:        201 on success, 406 on order exists
    """
    table_no = order.get("Table_No")
    flavor = order.get("Flavor")
    crust = order.get("Crust")
    size = order.get("Size")

    existing_order = (
        Orders.query.filter(Orders.Table_No == table_no)
        .filter(Orders.Flavor == flavor)
        .filter(Orders.Crust == crust)
        .filter(Orders.Size == size)
        .one_or_none()
    )

    # Can we insert this order?
    if existing_order is None:

        # Create an order instance using the schema and the passed in order
        schema = OrderSchema()
        new_order = schema.load(order, session=db.session).data

        # Add the order to the database
        db.session.add(new_order)
        db.session.commit()

        # Serialize and return the newly created order in the response
        data = schema.dump(new_order).data

        return data, 201

    # Otherwise, nope, order exists already
    else:
        abort(
            409,
            "Order for Table No. {table_no} exists already ".format(
                table_no=table_no
            ),
)
