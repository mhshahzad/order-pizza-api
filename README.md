<h2 align="center">
<b> Order Pizza API</b></h1>
<p align="center">
<img width="500" height="auto" src="rest-api-min.png"/>
</p>

<p align="center">
This API can be used as back-end on POS (point-of-sale) terminal
of pizza restaurant.
</p>

### Getting Started
<hr>

_Through your terminal/command prompt:_

1. Clone this repository

`git clone https://github.com/muhammadh-s/pizza_order-RESTful-API.git`

2. Install dependencies

`pip install -r requirements.txt`

3. Finally, start the app

`python server.py`

#### Endpoints

`/api` Basepath

`/auth` POST method, returns an access token

`/orders` GET method, returns list of orders

`/orders` POST method, to add an order

`/orders/{Order_ID}` DELETE method, to delete an order through Order ID

`/ui` renders a documentation webpage

### Implementation
<hr>

This application is built using: Flask, connexion, marshmallow and
SQLAlchemy, hence uses Python-3.7.1

Tested through: Postman
