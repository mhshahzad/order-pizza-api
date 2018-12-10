from datetime import datetime
from config import db, ma


class Orders(db.Model):
    __tablename__ = "orders"
    order_id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String(32))
    crust = db.Column(db.String(32))
    size = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Orders
sqla_session = db.session
