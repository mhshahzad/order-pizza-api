<p align="center"><img alt= "logo" src="images/logo.png" width="200"></p>
<h1 align="center">Order Pizza REST API</h1>

> A RESTful API as pizza restaurant ordering system.

<h3 align="center">
<a href="https://order-pizza-api.herokuapp.com/api/ui">Documentation </a>
</br>
</br>

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/060895f2f997c9d08e1d#?env%5Bserver%5D=W3sia2V5IjoidXJsIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlfV0=)

</h1>

Built with (but not limited to) :
   * [connexion](https://github.com/zalando/connexion)
   * [Flask](https://github.com/pallets/flask)
   * [flask-marshmallow](https://github.com/marshmallow-code/flask-marshmallow)
   * [marshmallow-sqlalchemy](https://github.com/marshmallow-code/marshmallow-sqlalchemy)
   * [flask_jwt_extended](https://github.com/vimalloc/flask-jwt-extended)
   * [Flask-SQLAlchemy](https://github.com/pallets/flask-sqlalchemy)
   * [tornado](https://github.com/tornadoweb/tornado)


## Setup

1. `git clone https://github.com/muhammadh-s/order-pizza-api`
2. `cd order-pizza-api`
3. `pip install -r requirements.txt` 
   _or place virtual environment and then install_
4. `python server.py`

## Usage

**Example Response**

```bash
curl -s https://order-pizza-api.herokuapp.com/api/orders
```

```json
[
  {
    "Crust": "NORMAL",
    "Flavor": "BEEF-NORMAL",
    "Order_ID": 1,
    "Size": "M",
    "Table_No": 1,
    "Timestamp": "2018-12-12T13:42:13.704148+00:00"
  },
  {
    "Crust": "THIN",
    "Flavor": "CHEESE",
    "Order_ID": 2,
    "Size": "S",
    "Table_No": 5,
    "Timestamp": "2018-12-12T13:42:13.704148+00:00"
  },
  {
    "Crust": "NORMAL",
    "Flavor": "CHICKEN-FAJITA",
    "Order_ID": 3,
    "Size": "L",
    "Table_No": 3,
    "Timestamp": "2018-12-12T13:42:13.720690+00:00"
  }
]
```

**Endpoints**


* POST : `/auth`    

```bash
  curl -X POST -H "Content-Type: application/json" -d '{"username": "test", "password": "test"}'  https://order-pizza-api.herokuapp.com/api/auth
```

* POST : `/orders`  (_Access Token is required_)

```bash
curl 
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer <JWT>" 
  -X POST 
  -d  
 '{
    "Flavor": "ABC", 
    "Crust": "XYZ",
    "Size": "XL", 
    "Table_No: 9"
  }' 
  https://order-pizza-api.herokuapp.com/api/orders
  ```
`Do replace the <JWT> in the above request with the token you have acquired.`


* DELETE : `/orders/{Order_ID}`

```bash
curl -X DELETE https://order-pizza-api.herokuapp.com/api/orders/1
```

## License
MIT