from flask import Flask, request
from flask_jwt import JWT,jwt_required
from flask_restful import Resource,Api,reqparse

from security import authenticate,identity

app = Flask(__name__)
app.secret_key = "Daniel"
api = Api(app)

jwt = JWT(app,authenticate,identity)

# Declare a list database
items = []

class Item(Resource):
    # the reason we're using the parser here is to avoid redundancy
    # also we're not using self before the parser because we don't want it to belong to a specific item resource
    # parser now belongs to the class Item itself
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field cannot be left blank!'
        )
    
    @jwt_required() # authenticating the method before calling it
    def get(self,name):
        itemElement = next(filter(lambda item: item['name'] == name,items),None)
        return {'item': itemElement}, 200 if itemElement else 404 
    
    def post(self,name):
        if next(filter(lambda item: item['name'] == name, items), None):
            return {'message': 'An item with the name {} already exists.'.format(name)}, 400
        
        data = Item.parser.parse_args()
        item = {'name' :name, 'price' : data['price']}
        items.append(item)
        return item, 201
    
    def delete(self,name):
        global items # this represents the items declared line 14
        items = list(filter(lambda item: item['name'] != name,items))
        return {'item': 'item {} deleted'.format(name)}
    
    def put(self,name):
        # getting the price that we declared in postman
        data = Item.parser.parse_args()
        # getting the item we want to update
        updateItem = next(filter(lambda item: item['name'] == name,items),None)
        if updateItem is None:
            updateItem = {'name': name,'price': data['price']}
            items.append(updateItem)
        else:
            # using the dictionary method update to update the item
            updateItem.update(data)
        return updateItem    

    
class Items(Resource):
    def get(self):
        return {'items' : items}, 200
  
api.add_resource(Items,'/v1/items')     
api.add_resource(Item,'/v1/item/<string:name>')
app.run(port=5000,debug=True)    
