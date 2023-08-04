# Imports the connection to mySQL database
from flask_app.config.mysqlconnection import connectToMySQL

# Create a class for a ninja to be created
class Ninja:
    DB = "dojos_and_ninjas"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    # Function to send in query and data to database (adding a new ninja to the list)
    @classmethod
    def new_ninja(cls, data):
        query = "INSERT INTO users (first_name, last_name, age) VALUES (%(first_name)s, %(last_name)s, %(age)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all_ninjas(cls, id):
        # query here needs to join the tables so I can get the ninjas where dojo.id match the id in the route
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        data = {"id": id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results:
            ninjas = []
            for ninja in results:
                ninjas.append(cls(ninja))
            return ninjas
        else:
            return []
        
    @classmethod
    def inputUser(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL(cls.DB).query_db(query, data)

