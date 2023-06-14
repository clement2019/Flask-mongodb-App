from flask import Flask, jsonify
import pymongo 
from pymongo import MongoClient

app=Flask(__name__)

def get_db():
    client = MongoClient(host='python_mongo',
                         port=27017, 
                         username='ayeni', 
                         password='password', 
                        authSource="admin")
    db = client["hunger_db"]
    return db


@app.route("/")

def ping_server():
    return 'Welcome to Ayenis website; server running well.....'

@app.route('/food')
def get_food_stock():
    db=""
    try:
        db = get_db()
        _food_type = db.hunger_db.find()
        foods = [{"id": food["id"], "name": food["name"], "type": food["type"]} for food in _food_type]
        return jsonify({"_food_type": foods})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=="__main__":
    app.run(debug=True, port=5001,host="0.0.0.0")
