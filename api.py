from bottle import route, run, get, post, request
from SRC.mongo import CollConection
import bson
import os

# User endpoints
@post('/user/create')
def add_user():
    username = request.forms.get("username")
    return {
        "inserted_doc": str(coll.addUser(username))}


@get("/user/<user_id>/recommend")
def recommend(user_id):
    result = coll.getRecommendation(user_id)
    return result


# Chat endpoints
@post('/chat/create')
def add_chat():
    fields = ["idUser", "userName", "idMessage", "idChat", "datetime", "text"]
    document = {e: request.forms.get(e) for e in fields}
    return {"inserted_doc": str(coll.addChat(document))}


@get("/chat/<chat_id>/get_sentiment")
def get_sentiment(chat_id):
    # hacer lo mismo para users y para users/chats
    result = coll.getSentiment(chat_id)
    return result


coll = CollConection('Chats')

port = int(os.getenv("PORT", 8080))
print(f"Running server {port}....")

run(host='0.0.0.0', port=port)
