from pymongo import MongoClient

mongo_uri = "mongo://localhost:27017"


class LocalDatabase:
    def __init__(self):
        self.db = MongoClient().get_database('locality-service')
        self.export_db = MongoClient().get_database('export-service')
        self.country_db = self.db.countries
        self.division_db = self.db.divisions
        self.subdivision_db = self.db.subdivisions

    def write_country(self, country):
        return self.country_db.insert_one(country)

    def write_division(self, country_id, state):
        state['country_id'] = country_id
        return self.division_db.insert_one(state)

    def write_subdivision(self, division_id, subdivision):
        subdivision['division_id'] = division_id
        return self.subdivision_db.insert_one(subdivision)

    def find_country_record(self, id):
        return self.country_db.findOne({'_id': id})

    def write(self, country, data):
        self.export_db.insert_one(data)
