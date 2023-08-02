# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class Users:
    DB = "users"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # Create a classmethod that queries the input, how do i put the value? Do I use an f string with self.first_name ...
    @classmethod
    def inputUser(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL(cls.DB).query_db(query, data)
        



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user))
        return users
            



    @classmethod
    def update(cls, data):
        query = """UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s; """
        return connectToMySQL(cls.DB).query_db(query,data)



    @classmethod
    def getOne(cls, id):
        query = """SELECT * FROM users WHERE id = %(id)s;"""
        data = {'id': id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def delete(cls, id):
        query = """DELETE FROM users WHERE id = %(id)s;"""
        data = {'id': id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
