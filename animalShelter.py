# Quintin B. Rozelle

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB"""
    
    
    def __init__(self, username='aacuser', password='password'):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30455
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print('Connection successful')
    
    
    # Create new document and add to database
    # data: new document to add to database. Needs to be a Python dictionary
    # returns: boolean; true if successful, false if failure
    def create(self, data: dict) -> bool:
        try:
            if data is not None:
                insertSuccess = self.database.animals.insert_one(data)
                return insertSuccess.acknowledged
            else:
                raise Exception('Nothing to save, because data parameter is empty')
        except Exception as e:
            print(repr(e))
            return False
    
    
    # Searches for and returns list of documents from database
    # data: document to search for in database. Needs to be a Python dictionary
    # returns: list of documents found
    def read(self, data: dict) -> list:
        try:
            if data is not None:
                return list(self.database.animals.find(data))
            else:
                raise Exception('Nothing to search for, because data parameter is empty')
        except Exception as e:
            print(repr(e))
            return list()
        
    
    # Search for and update document(s) in the database
    # searchData: document to search for in database. Needs to be a Python dictionary
    # updateData: key/value pairs to update in found documents. Needs to be a Python dictionary
    # returns: the number of documents updated
    def update(self, searchData: dict, updateData: dict) -> int:
        try:
            if searchData is not None or updateData is not None:
                return self.database.animals.update_many(searchData, updateData).modified_count
            else:
                raise Exception('Nothing to search for, because searchData or updataData parameter is empty')
        except Exception as e:
            print(repr(e))
            return 0
        
        
    # Deletes document(s) in the database
    # data: document to search for in database. Needs to be a Python dictionary
    # returns: the number of documents deleted
    def delete(self, data: dict) -> int:
        try:
            if data is not None:
                return self.database.animals.delete_many(data).deleted_count
            else:
                raise Exception('Nothing to search for, because data parameter is empty')
        except Exception as e:
            print(repr(e))
            return 0