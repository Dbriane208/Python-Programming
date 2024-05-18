import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

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
        item = Item.find_by_name(name)
        if item:
            return item
        return {'message':'item not found'}, 404
    
    # method that filters the name
    @classmethod
    def find_by_name(cls,name):
        # Establish the connection
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # querying the name that matches name from db
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': row[0],'price': row[1]}

    
    def post(self,name):
        # the function could have also been writen as Item.find_by_name because its a class
        # method
        if self.find_by_name(name): 
            return {'message': 'An item with the name {} already exists.'.format(name)}, 400
        
        data = Item.parser.parse_args()
        item = {'name' :name, 'price' : data['price']}

        try:
            self.insert(item=item)
        except:
            return {"message":"An error occurred inserting the item"},500    

        return item, 201
    
    
    @classmethod
    def insert(cls,item):
        # create a connection to insert to the database
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # Inserting the query
        query = "INSERT INTO items VALUES(?,?)"
        cursor.execute(query,(item['name'],item['price']))

        # closing and commiting the query
        connection.commit()
        connection.close()

    
    def delete(self,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query,(name,))

        connection.commit()
        connection.close()

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