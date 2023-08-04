# Imports the connection to mySQL database
from flask_app.config.mysqlconnection import connectToMySQL

# Create a class for a dojo to be created
class Dojo:
    DB = "dojos_and_ninjas"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Function to send in query and data to database (adding a new dojo to the list)
    @classmethod
    def new_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_one_dojo(cls, id):
        query = """SELECT * FROM dojos WHERE id = %(id)s;"""
        data = {'id': id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])















    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM users;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL(cls.DB).query_db(query)
    #     # Create an empty list to append our instances of friends
    #     users = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for user in results:
    #         users.append(cls(user))
    #     return users
            



    # @classmethod
    # def update(cls, data):
    #     query = """UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s; """
    #     return connectToMySQL(cls.DB).query_db(query,data)



    # @classmethod
    # def getOne(cls, id):
    #     query = """SELECT * FROM users WHERE id = %(id)s;"""
    #     data = {'id': id}
    #     result = connectToMySQL(cls.DB).query_db(query, data)
    #     return cls(result[0])

    # @classmethod
    # def delete(cls, id):
    #     query = """DELETE FROM users WHERE id = %(id)s;"""
    #     data = {'id': id}
    #     result = connectToMySQL(cls.DB).query_db(query, data)
    #     return result
