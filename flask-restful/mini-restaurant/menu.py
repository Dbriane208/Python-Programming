import sqlite3
from flask import request
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required


class Menu(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('category',
        type=str,
        required=True,
        help="This field cannot be blank")
    
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be blank")
    
    @jwt_required()
    def get(self,name):
        menu_item = Menu.find_by_name(name=name)
        if menu_item is None:
            return {'message': 'menu item {} does not exist.'.format(name)}, 404
        else:
            return {'menu item': menu_item},200

    @classmethod
    def find_by_name(cls,name):
        # Establish a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor() 

        # query the results
        query = "SELECT * FROM menus WHERE name=?"
        result = cursor.execute(query,(name,)) 
        row = result.fetchone()

        # close the connection
        connection.close()

        # response
        if row:
            return {
                'id':row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
           
        
    def post(self,name):
        if Menu.find_by_name(name=name):
            return {'message': 'A menu item with the name {} already exists'.format(name)}
        
        data = Menu.parser.parse_args()
        updMenu = {
            'name': name,
            'category': data['category'],
            'price': data['price']
        }
      
        try:
            self.insert(updMenu=updMenu)
        except sqlite3.Error as e:
            return {"message": "Error {} occurred while posting the item".format(str(e))}, 500
              
        return updMenu, 201
    
    @classmethod
    def insert(cls,updMenu):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        query = "INSERT INTO menus(name,category,price) VALUES(?,?,?)"
        cursor.execute(query,(
            updMenu['name'],
            updMenu['category'],
            updMenu['price']
        ))
   
        connection.commit()
        connection.close()
    
    def delete(self,name):
        # Establish the connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # query result
        query = "DELETE FROM menus WHERE name=?"
        cursor.execute(query,(name,))

        # close the connection
        connection.commit()
        connection.close()

        return {'message': 'menu item {} deleted successfully.'.format(name)}, 200

    def put(self,name): 
        data = Menu.parser.parse_args()
        update_menu = Menu.find_by_name(name=name)
        updMenu = {
                'name':name,
                'category': data['category'],
                'price': data['price']
            } 
        
        if update_menu is None:
            try:
                self.insert(updMenu=updMenu)
            except sqlite3.Error as e:
                return {"message":"Error {} occurred while inserting the item".format(str(e))}, 500    
        else:
            try:
                self.update(updMenu=updMenu)
            except sqlite3.Error as e:
                return {"message":"Error {} occurred while updating the item".format(str(e))}, 500
                
        return updMenu, 200
    
    @classmethod
    def update(cls,updMenu):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        query = "UPDATE menus SET category=?, price=? WHERE name=?"
        cursor.execute(query,(
            updMenu['category'],
            updMenu['price'],
            updMenu['name']
        ))

        connection.commit()
        connection.close()
        
class Menus(Resource):
    def get(self):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        query = "SELECT * FROM menus"
        result = cursor.execute(query)
        rows = result.fetchall()

        menus = []
        if rows:
            try:
                for row in rows:
                    menus.append({
                        'id':row[0],
                        'name':row[1],
                        'category': row[2],
                        'price': row[3]
                    })
                    connection.close()
                return {'menus': menus}, 200    
            except sqlite3.Error as e:
                return {"message":"Error {} occurred while retrieving the menus".format(str(e))}, 500    