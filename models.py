from datetime import datetime
from config import db, ma


class Orders(db.Model):
    __tablename__ = "orders"
    Table_No = db.Column(db.Integer)
    Order_ID = db.Column(db.Integer, primary_key=True)
    Flavor = db.Column(db.String(32))
    Crust = db.Column(db.String(32))
    Size = db.Column(db.String(32))
    Timestamp = db.Column(
        db.DateTime, default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Orders
        ordered = True
sqla_session = db.session
