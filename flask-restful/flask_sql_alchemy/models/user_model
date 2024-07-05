import sqlite3

class UserModel:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        # Establishing a connection
        connection = sqlite3.connect("data.db")  
        cursor = connection.cursor() 

        # creating a username query
        query = "SELECT * FROM users WHERE username =?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()

        # print the details of the result
        if row:
            user = cls(*row)
        else:
            user = None
            connection.close()
        return user        

    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query,(_id,))
        # returns the only row with the result from the query
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
            connection.close()
        return user    
