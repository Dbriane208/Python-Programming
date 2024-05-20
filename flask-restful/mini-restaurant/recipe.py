import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class Recipe(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('ingredients',
        type=str,
        required=True,
        help="The field cannot be blank")
    parser.add_argument('amount',
        type=str,
        required=True,
        help="The field cannot be blank")
    
    @jwt_required()
    def get(self,name):
        recipe_item = Recipe.find_by_name(name=name)
        if recipe_item:
            return {'recipe': recipe_item},200
        else:
            return {'message': 'recipe item {} does not exist.'.format(name)}, 404
        
    @classmethod
    def find_by_name(cls,name):
        # Establish the connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Query the results
        query = "SELECT * FROM recipes WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()

        # close the connection
        connection.close()

        if row:
            return {
                'id': row[0],
                'name': row[1],
                'ingredients': row[2],
                'amount': row[3]
            }    

    def post(self,name):
        if Recipe.find_by_name(name=name):
            return {'message': 'recipe item {} already exists.'.format(name)}, 200

        data = Recipe.parser.parse_args()
        recipeItem = {
            'name': name,
            'ingredients': data['ingredients'],
            'amount': data['amount']
        } 

        try:
            Recipe.insert(recipeItem=recipeItem)
        except sqlite3.Error as e:
            return {"message":"Error {} occurred while posting the item".format(str(e))}, 500
            
        return recipeItem, 201  
    
    @classmethod
    def insert(cls,recipeItem):
        # Establish connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Query the results
        query = "INSERT INTO recipes(name,ingredients,amount) VALUES(?,?,?)"
        cursor.execute(query,(
            recipeItem['name'],
            recipeItem['ingredients'],
            recipeItem['amount']
        ))

        # close the connection
        connection.commit()
        connection.close()

    def delete(self,name):
        # Establish a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Query the results
        query = "DELETE FROM recipes WHERE name=?"
        cursor.execute(query,(name,))

        # close connection
        connection.commit()
        connection.close()
        
        return {'message': 'recipe item {} deleted successfully.'.format(name)}, 200 
    
    def put(self,name):
        data = Recipe.parser.parse_args()
        recipe = Recipe.find_by_name(name=name)
        updRecipe = {
             'name': name,
             'ingredients': data['ingredients'],
             'amount': data['amount']
            }
        if recipe is None:
            try:
                self.insert(recipeItem=updRecipe)
            except sqlite3.Error as e:
                return {"message":"Error {} occurred while inserting the item".format(str(e))}    
        else:
            try:
                self.update(recipeItem=updRecipe)
            except sqlite3.Error as e:
                return {"message":"Error {} occurred while updating the item".format(str(e))} 
               
        return updRecipe, 200
    
    @classmethod
    def update(cls,recipeItem):
        # Establish the connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Query the results
        query = "UPDATE recipes SET ingredients=?,amount=? WHERE name=?"
        cursor.execute(query,(
            recipeItem['ingredients'],
            recipeItem['amount'],
            recipeItem['name']
        ))

        # close the connection
        connection.commit()
        connection.close()

class Recipes(Resource):
    def get(self):
        #Establish a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # query the results
        query = "SELECT * FROM recipes"
        result = cursor.execute(query)
        rows = result.fetchall()

        recipes = []
        if rows:
            try:
                for row in rows:
                    recipes.append({
                        'id':row[0],
                        'name':row[1],
                        'ingredients':row[2],
                        'amount':row[3]
                    })
                    connection.close()
                return {'recipes': recipes}, 200   
            except sqlite3.Error as e:
                return {"message":"Error {} occurred while trying to retrieve items".format(str(e))}, 500         

