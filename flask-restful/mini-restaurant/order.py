from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required

# databases
orders = []

class Order(Resource):
    @jwt_required()
    def get(self,name):
        order_item = next(filter(lambda order: order['name'] == name,orders),None)
        return {'order': order_item}, 200 if order_item else 404 # not found
    
    def post(self,name):
        if next(filter(lambda order: order['name'] == name,orders),None):
            return {'item': 'order {} already exists'.format(name)}, 400 # bad request

        data = request.get_json()
        order = {
            'name': name,
            'description': data['description'],
            'amount': data['amount'],
            'price': data['price'],
            'message': data['message']
        }   
        orders.append(order)
        return order, 201 # order created
    
    def delete(self,name):
        global orders
        orders = list(filter(lambda order: order['name'] != name,orders))
        return {'message': 'order {} item has been deleted successfully'.format(name)}, 200
    
    def put(self,name):
        data = request.get_json()
        updateOrder = next(filter(lambda order: order['name'] == name,orders),None)
        if updateOrder is None:
            updateOrder = {
               'name': name,
               'description': data['description'],
               'amount': data['amount'],
               'price': data['price'],
               'message': data['message']
            }
            orders.append(updateOrder)
        else:
            updateOrder.update(data)  
        return updateOrder, 200  

class Orders(Resource):
    def get(self):
        return {'orders': orders},200 # request is ok    
