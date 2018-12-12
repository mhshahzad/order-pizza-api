import os
from config import db
from models import Orders

# Data to initialize database with
ORDERS = [
    {
        "Table_No": 1,
        "Flavor": "BEEF-NORMAL",
        "Crust":"NORMAL",
        "Size":"M"
    },
    {
        "Table_No": 5,
        "Flavor": "CHEESE",
        "Crust":"THIN",
        "Size":"S"
    },
    {
        "Table_No": 3,
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

# iterate over the ORDERS structure and populate the database
for pizza in ORDERS:
    p = Orders(
    Table_No=pizza.get("Table_No"),
    Flavor=pizza.get("Flavor"),
    Crust=pizza.get("Crust"),
    Size=pizza.get("Size"))

    db.session.add(p)

db.session.commit()
