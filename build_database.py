import os
from config import db
from models import Orders

# Data to initialize database with
ORDERS = [
    {
        "Flavor": "BEEF-NORMAL",
        "Crust":"NORMAL",
        "Size":"M"
    },
    {
        "Flavor": "CHEESE",
        "Crust":"NORMAL",
        "Size":"S"
    },
    {
        "Flavor": "CHICKEN-FAJITA",
        "Crust":"NORMAL",
        "Size":"L"
    },

]

# Delete database file if it exists currently
if os.path.exists("orders.db"):
    os.remove("orders.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for pizza in ORDERS:
    p = Orders(flavor=pizza.get("Flavor"),
    crust=pizza.get("Crust"), size=pizza.get("Size"))
    db.session.add(p)

db.session.commit()
