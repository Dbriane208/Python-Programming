import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class Food(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('type',
        type=str,
        required=True,
        help='This field cannot be left blank'
        )
    parser.add_argument('ingredient',
        type=str,
        required=True,
        help='This field cannot be left blank'
        )
    parser.add_argument('amount',
        type=str,
        required=True,
        help='This field cannot be left blank'
        )
    
    @jwt_required()
    def get(self,name):
        food_item = Food.find_by_name(name=name)
        if food_item is None:
            return {'message': 'item {} does not exist'.format(name)}, 404
        else:
            return {'food_item':food_item}, 200

    @classmethod
    def find_by_name(cls,name):
        # Establish a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # perform the query
        query = "SELECT * FROM foods WHERE name=?"
        result = cursor.execute(query,(name,)) 
        row = result.fetchone()
        connection.close()

        if row:
            return {
                'id':row[0],
                'name': row[1],
                'type':row[2],
                'ingredient':row[3],
                'amount':row[4]
            }   
        
    def post(self,name):
        if Food.find_by_name(name=name):
            return {'message': 'An item with the name {} already exists.'.format(name)}, 400
        
        data = Food.parser.parse_args()
        foodItem = {
            'name': name,
            'type': data['type'],
            'ingredient': data['ingredient'],
            'amount': data['amount']
        }

        try:
          self.insert(foodItem)
        except:
            return {"message": "An error occurred posting the item"}, 500
          
        return foodItem, 201
    
    # we create a class method to insert to be used in both the update and post method
    @classmethod
    def insert(cls,foodItem):
        # Establish a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Inserting to the database
        insert_query = "INSERT INTO foods(name,type,ingredient,amount) VALUES(?,?,?,?)"
        cursor.execute(insert_query,(
            foodItem['name'],
            foodItem['type'],
            foodItem['ingredient'],
            foodItem['amount']
        )) 
        
        # closing and commiting the query
        connection.commit()
        connection.close()
                
    
    def delete(self,name):
        # Establish a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        query = "DELETE FROM foods WHERE name=?"
        cursor.execute(query,(name,))

        # close connection
        connection.commit()
        connection.close()

        
        return {'message': 'food item {} deleted successfully.'.format(name)},200
        

    def put(self,name):
        data = Food.parser.parse_args()
        food_item = Food.find_by_name(name=name)
        updateFood = {
               'name': name,
               'type': data['type'],
               'ingredient': data['ingredient'],
               'amount': data['amount']
            }
        
        if food_item is None:
            try:
                self.insert(updateFood)
            except:
                return {"message":"An error occurred inserting the item"}, 500    
        else:
            try:    
                self.update(updateFood)
            except:
                return {"message":"An error occurred updating the item"}, 500
        return updateFood, 200
    
    @classmethod
    def update(cls,updateFood):
        # Establish connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        query = "UPDATE foods SET type=?, ingredient=? ,amount=? WHERE name=?"
        cursor.execute(query,(
            updateFood['type'],
            updateFood['ingredient'],
            updateFood['amount'],
            updateFood['name']
        ))

        connection.commit()
        connection.close()
    

class Foods(Resource):
    def get(self):
        # Establish a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # query the results
        all_foods = "SELECT * FROM foods"
        result = cursor.execute(all_foods)
        rows = result.fetchall()

        foods = []
        if rows:
            try:
                for row in rows:
                    foods.append({
                        'id':row[0],
                        'name':row[1],
                        'type':row[2],
                        'ingredient':row[3],
                        'amount':row[4]
                    })
                    connection.close()
                return {'foods': foods}, 200
            except:
                return {"message":"An error occurred retrieving the foods"}, 500          

