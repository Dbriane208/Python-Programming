from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from security import authenticate,identity

from order import Order, Orders
from food import Food,Foods
from menu import Menu,Menus
from recipe import Recipe,Recipes

app = Flask(__name__)
app.secret_key = 'mini-restaurant'
api = Api(app) 

jwt = JWT(app,authenticate,identity)

# orders endpoints
api.add_resource(Order,'/v1/order/<string:name>')
api.add_resource(Orders,'/v1/orders')

# foods endpoints
api.add_resource(Food,'/v1/food/<string:name>')
api.add_resource(Foods,'/v1/foods')

# menus endpoints
api.add_resource(Menu,'/v1/menu/<string:name>')
api.add_resource(Menus,'/v1/menus')

# recipes endpoints
api.add_resource(Recipe,'/v1/recipe/<string:name>')
api.add_resource(Recipes,'/v1/recipes')

app.run(port=5000,debug=True)    

        
