from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required

# database
foods = []

class Food(Resource):
    @jwt_required()
    def get(self,name):
        food_item = next(filter(lambda food: food['name'] == name,foods),None)
        if food_item is None:
            return {'message': 'item {} does not exist'.format(name)}, 404
        else:
            return {'food': food_item}, 200
        
    def post(self,name):
        if next(filter(lambda food: food['name'] == name,foods),None):
            return {'message': 'item {} already exists'.format(name)}
        
        data = request.get_json()
        foodItem = {
            'name': name,
            'type': data['type'],
            'ingredient': data['ingredient'],
            'amount': data['amount']
        }
        foods.append(foodItem)
        return foodItem, 201
    
    def delete(self,name):
        global foods
        foods = list(filter(lambda food: food['name'] != name,foods))
        return {'message': 'food item {} deleted'.format(name)}

    def put(self,name):
        data = request.get_json()
        updateFood = next(filter(lambda food: food['name'] == name,foods),None)
        if updateFood is None:
            updateFood = {
               'name': name,
               'type': data['type'],
               'ingredient': data['ingredient'],
               'amount': data['amount']
            }
            foods.append(updateFood)
        else:
            updateFood.update(data)
        return updateFood, 200

class Foods(Resource):
    def get(self):
        return {'foods': foods}, 200            

