from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Shows:
    db_name = 'StarWars'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.image = db_data['image']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_first_name =db_data['users.first_name']
        self.user_last_name = db_data['users.last_name']
        

    @classmethod
    def save(cls,data):
        query = "INSERT INTO shows (name, description, image, user_id) VALUES (%(name)s,%(description)s,%(image)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def favorite(cls, data):
        query = "INSERT INTO users_shows (show_id, user_id) VALUES (%(show_id)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT shows.*,users.first_name, users.last_name FROM shows LEFT JOIN users ON shows.user_id = users.id;"
        results =connectToMySQL(cls.db_name).query_db(query)
        all_shows = []
        for row in results:
            all_shows.append( cls(row))
        return all_shows
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id WHERE shows.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print (results)
        return cls( results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE shows SET name=%(name)s, description=%(description)s, updated_at=NOW() WHERE shows.id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all_by_user(cls,data):
        query = "SELECT * FROM users JOIN users_shows ON users.id = users_shows.user_id JOIN shows ON shows.id = users_shows.show_id WHERE users.id=%(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users_shows WHERE show_id = %(show_id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
