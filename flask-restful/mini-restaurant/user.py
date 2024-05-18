import sqlite3
from flask_restful import Resource,reqparse

class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        # Establish a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Retrieving username from database
        username_query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(username_query,(username,)) 
        # returns the only row with the result from the query
        row = result.fetchone()

        if row:
            user =  cls(*row)
        else:
            user = None
            # We haven't commited because we haven't added anything to the database
            connection.close()
        return user   

    @classmethod
    def find_by_id(cls,_id):
        # Establishing a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Retrieving username from database
        id_query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(id_query,(_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
            connection.close()
        return user        

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
    parser.add_argument('password',
            type=str,
            required=True,
            help="This field cannot be blank"
        )
    
    def post(self):
        # Establish a connection
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        # Getting the user from the user
        data = UserRegister.parser.parse_args()

        # check for duplication
        if User.find_by_username(data['username']):
            return {"message":"A user with the same name already exists!"}, 400

        # Insert a new user
        register = "INSERT INTO users VALUES(NULL,?,?)"
        cursor.execute(register,(data['username'],data['password']))

        # close the connection
        connection.commit()
        connection.close()
        return {"message": "User successfully registered!"}
