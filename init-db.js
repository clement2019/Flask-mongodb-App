db = db.getSiblingDB("hunger_db");
db.hunger_db.drop();

db.hunger_db.insertMany([
    {
        "id": 1,
        "name": "bread",
        "type": "local"
    },
    {
        "id": 2,
        "name": "Cornflakes",
        "type": "modern"
    },
    {
        "id": 3,
        "name": "indolmie",
        "type": "modern"
    },
    {
        "id": 4,
        "name": "gari",
        "type": "local"
    },
    {
        "id": 5,
        "name": "chicken",
        "type": "good"
    },
    {
        "id": 6,
        "name": "goat",
        "type": "local_animal"
    },
]);
