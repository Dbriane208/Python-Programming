import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Order(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('description',
        type=str,
        required=True,
        help="This field cannot be blank")
    parser.add_argument('amount',
        type=str,
        required=True,
        help="This field cannot be blank")
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be blank")
    
    @jwt_required()
    def get(self,name):
        order_item = Order.find_by_name(name=name)
        if order_item:
            return {'order': order_item}, 200 
        else:
            return {'message': 'Order item {} does not exist'.format(name)}, 404
    
    @classmethod
    def find_by_name(cls,name):
        # Establish connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Query the results
        query = "SELECT * FROM orders WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()

        # Close the connection
        connection.close()

        if row:
            return {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'amount': row[3],
                'price': row[4]
            }
    
    def post(self,name):
        if Order.find_by_name(name=name):
            return {'item': 'order {} already exists'.format(name)}, 400 # bad request

        data = Order.parser.parse_args()
        order = {
            'name': name,
            'description': data['description'],
            'amount': data['amount'],
            'price': data['price']
        }  

        try:
            self.insert(order=order)
        except sqlite3.Error as e: 
            return {"message":"Error {} occurred while posting the item".format(str(e))}, 500 
          
        return order, 201 # order created
    
    @classmethod
    def insert(cls,order):
        # Establish the connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Query for result
        query = "INSERT INTO orders(name,description,amount,price) VALUES(?,?,?,?)"
        cursor.execute(query,(
            order['name'],
            order['description'],
            order['amount'],
            order['price']
        ))

        # close the connection
        connection.commit()
        connection.close()
    
    def delete(self,name):
        # Establish connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Query the result
        query = "DELETE FROM orders WHERE name=?"
        cursor.execute(query,(name,))

        # close the connection
        connection.commit()
        connection.cursor()

        return {'message': 'order {} item has been deleted successfully'.format(name)}, 200
    
    def put(self,name):
        data = Order.parser.parse_args()
        update_order = Order.find_by_name(name=name)
        updateOrder = {
               'name': name,
               'description': data['description'],
               'amount': data['amount'],
               'price': data['price']
            }
        
        if update_order is None:
            try:
                self.insert(order=updateOrder)
            except sqlite3.Error as e:
                return {"message":"Error {} occurred while inserting the item".format(str(e))} ,500   
        else:
            try:   
                self.update(order=updateOrder)
            except sqlite3.Error as e:
                return {"message":"Error {} occurred while updating the item".format(str(e))} ,500   
             
        return updateOrder, 200 

    @classmethod
    def update(cls,order):
        # Establish connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Query the results
        query = "UPDATE orders SET description=?,amount=?,price=? WHERE name=?"
        cursor.execute(query,(
            order['description'],
            order['amount'],
            order['price'],
            order['name']
        )) 

        # close the connection
        connection.commit()
        connection.close()

class Orders(Resource):
    def get(self):
        # Establish the connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Query the results
        query = "SELECT * FROM orders"
        result = cursor.execute(query)
        rows = result.fetchall()

        orders = []

        if rows:
            try:
                for row in rows:
                    orders.append({
                        'id': row[0],
                        'name': row[1],
                        'description': row[2],
                        'amount': row[3],
                        'price': row[4]
                    })
                    # close the connection
                    connection.close()
                return {'orders': orders},200 # request is ok   
            except sqlite3.Error as e:
                return {"message":"Error {} occurred while retrieving orders".format(str(e))}, 500  
