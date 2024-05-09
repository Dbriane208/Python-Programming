from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required

# create a recipe database
recipes = []

class Recipe(Resource):
    @jwt_required()
    def get(self,name):
        recipe_item = next(filter(lambda recipe: recipe['name'] == name,recipes),None)
        if recipe_item:
            return {'recipe': recipe_item},200
        else:
            return {'message': 'recipe item {} does not exist.'.format(name)}, 404

    def post(self,name):
        if next(filter(lambda recipe: recipe['name'] == name,recipes),None):
            return {'message': 'recipe item {} already exists.'.format(name)}, 200

        data = request.get_json()
        recipeItem = {
            'name': name,
            'ingredients': data['ingredients'],
            'amount': data['amount'],
            'message': data['message']
        } 
        recipes.append(recipeItem)
        return recipeItem, 201  

    def delete(self,name):
        global recipes
        recipes = list(filter(lambda recipe: recipe['name'] != name, recipes))
        return {'message': 'recipe item {} deleted successfully.'.format(name)}, 200 
    
    def put(self,name):
        data = request.get_json()
        updRecipe = next(filter(lambda recipe: recipe['name'] != name,recipes),None)
        if updRecipe is None:
            updRecipe = {
             'name': name,
             'ingredients': data['ingredients'],
             'amount': data['amount'],
             'message': data['message']
            }
            recipes.append(updRecipe)
        else:
            updRecipe.update(data)
        return updRecipe, 200

class Recipes(Resource):
    def get(self):
        return {'recipes': recipes}, 200        

