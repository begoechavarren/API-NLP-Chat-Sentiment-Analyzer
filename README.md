![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# API NLP - Chat Sentiment Analysis Service
Example API deployed in Heroku for the Ironhack Data & Analytics Oct 2019 bootcamp students.

## Overview

The API, which can be consumed from https://api-nlp-bego.herokuapp.com/, serves data extracted from a MongoDB Atlas database and processed using nltk NLP library.

## API Documentation

It serves to analyze the public chat messages (like slack public channels) of your team and create sentiment metrics, as well as recommend users to other users based on their similarity.

- Index: `@get("/")`
- User endpoints:
    - Create a new user: `@post('/user/create')`
    - Recommend a user to another user (based on nlp words similarity): `@get("/user/<user_id>/recommend")`
- Chat endpoints:
    - Create a new chat document: `@post('/chat/create')`
    - Extract sentiment from a certain chat: `@get("/chat/<chat_id>/get_sentiment")`

​
