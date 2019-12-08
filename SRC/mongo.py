from pymongo import MongoClient
from SRC.nlp_functions import *
import os
# from getpass import getpass


class CollConection:

    def __init__(self, dbName):
        password = os.getenv("mongo_password")  # getpass()
        connection = "mongodb+srv://Bego:{}@cluster0-y53fk.azure.mongodb.net/test?retryWrites=true&w=majority".format(
            password)
        self.client = MongoClient(connection)
        self.db = self.client[dbName]

    def addUser(self, username, collection="Users"):
        document = {'username': username}
        insert = self.db[collection].insert_one(document)
        print("Inserted user", insert.inserted_id)
        return insert.inserted_id

    def addChat(self, document, collection="Chats"):
        insert = self.db[collection].insert_one(document)
        print("Inserted chat", insert.inserted_id)
        return insert.inserted_id

    def getRecommendation(self, user_id, collection="Chats"):
        return find_similarity(user_id, self.db, collection)

    def getSentiment(self, chat_id, collection="Chats"):
        text = " ".join([chat['text'] for chat in list(
            self.db[collection].find({"idChat": chat_id}))])
        return sentiment_analyzer(text)
