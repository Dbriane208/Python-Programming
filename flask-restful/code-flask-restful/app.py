from flask import Flask, request
from flask_restful import Resource,Api

app = Flask(__name__)
app.secret_key = "Daniel"
api = Api(app)

# Declare a list database
items = []

class Item(Resource):
    def get(self,name):
        itemElement = next(filter(lambda item: item['name'] == name,items),None)
        return {'item': itemElement}, 200 if itemElement else 404 
    
    def post(self,name):
        if next(filter(lambda item: item['name'] == name, items), None):
            return {'message': 'An item with the name {} already exists.'.format(name)}, 400
        
        data = request.get_json()
        item = {'name' :name, 'price' : data['price']}
        items.append(item)
        return item, 201
    
class Items(Resource):
    def get(self):
        return {'items' : items}, 200
  
api.add_resource(Items,'/v1/items')     
api.add_resource(Item,'/v1/item/<string:name>')
app.run(port=5000,debug=True)    
