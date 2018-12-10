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
