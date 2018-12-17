## Order Pizza API

A Rest-ful API for pizza ordering.

This API can be integrated as Back-end in POS (point-of-sale) terminal 
of pizza restaurant.

GET, POST and DELETE methods can be used on list of orders.

### Getting Started

_Through your terminal/command prompt:_

1. Clone this repository

`git clone https://github.com/muhammadh-s/pizza_order-RESTful-API.git`

2. Install dependencies

`pip install -r requirements.txt`

3. Finally, start the app

`python server.py`

Try GET method in your browser: `localhost:5000/api/orders` 

To read the documentation: `localhost:5000/api/ui`

### Implementation

This application is built using: Flask, connexion, marshmallow and
SQLAlchemy, hence uses Python-3.7.1

Tested through: Postman
