from src.repositories.repositories import PlanetRepository


class MongoPlanetRepository(PlanetRepository):
    def __init__(self, mongo_client, database_name: str):
        self.mongo_client = mongo_client
        self.database = self.mongo_client.get_database(database_name)
        self.collection = self.database.get_collection("planets")
        self.collection.create_index("name", unique=True)

    def get_all(self):
        planets = self.collection.find({}, {"_id": 0})
        return list(planets)

    def get_by_name(self, planet_name: str):
        return self.collection.find_one({"name": planet_name}, {"_id": 0})

    def add(self, planet):
        self.collection.insert_one(planet.model_dump())

    def update(self, planet):
        self.collection.update_one(
            {"name": planet.name},
            {
                "$set": {
                    "climate": planet.climate,
                    "terrain": planet.terrain,
                    "count_films": planet.count_films,
                }
            },
        )

    def delete(self, planet_name: str):
        self.collection.delete_one({"name": planet_name})
