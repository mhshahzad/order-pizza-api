<img src="logo.png" alt="drawing" width="200"/>

# Order Pizza API
> A RESTful API as pizza restaurant ordering system.


Built with (but not limited to) :
   * [connexion](https://github.com/zalando/connexion)
   * [Flask](https://github.com/pallets/flask)
   * [flask-marshmallow](https://github.com/marshmallow-code/flask-marshmallow)
   * [marshmallow-sqlalchemy](https://github.com/marshmallow-code/marshmallow-sqlalchemy)
   * [flask_jwt_extended](https://github.com/vimalloc/flask-jwt-extended)
   * [Flask-SQLAlchemy](https://github.com/pallets/flask-sqlalchemy)
   * [tornado](https://github.com/tornadoweb/tornado)

## Setup

1. `git clone https://github.com/muhammadh-s/order-pizza-API`
2. `cd order-pizza-api`
3. `pip install -r requirements.txt` _or place virtual environment and then install_
4. `python server.py`

or visit : <https://order-pizza-api.herokuapp.com/>

Documentation : <https://order-pizza-api.herokuapp.com/ui>

### Endpoints :

* Base Path : `/api`

* POST : `/auth`    
  
![](auth.png?raw=true)

* GET : `/orders`

![](screenshot.png?raw=true)

* POST : `/orders`  (_Access Token is required_)

![](post.png?raw=true)

* DELETE : `/order/{Order_ID}`

![](del.png?raw=true)

## License
MIT