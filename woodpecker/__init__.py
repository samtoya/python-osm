from hummingbird import HummingBird
from libs import TableIt


class WoodPecker:
    state = {}
    city = {}

    def __init__(self):
        self._humming_bird = HummingBird()

    def localize_state(self, state, country):
        return self._humming_bird.localize_state(state, country)

    def localize_country(self, country):
        return self._humming_bird.localize_country(country)

    def localize_city(self, city, state, country):
        return self._humming_bird.localize_city(city, state, country)

    def print_ascii_art(self):
        print("""
                                                           .___       
          ______  ____    ____    ____    ____   ____    __| _/ ____  
         /  ___/ /    \  /  _ \  /  _ \ _/ ___\ /  _ \  / __ |_/ __ \ 
         \___ \ |   |  \(  <_> )(  <_> )\  \___(  <_> )/ /_/ |\  ___/ 
        /____  >|___|  / \____/  \____/  \___  >\____/ \____ | \___  >
             \/      \/                      \/             \/     \/ :
                """)

    def ask_for_country_name(self):
        return input('Which country do you want to localize:? ')

    def ask_for_process_identifier(self):
        self.print_ascii_art()
        table_data = [
            [1, "Ask user for country name (Default)"],
            [2, "Use default global_data.json"],
            [3, "Use local database file"],
            [4, "Generate polygon"],
        ]
        TableIt.printTable(table_data)
        return input("Choose from the options above:? ")

    def ask_for_where_to_save_data(self):
        table_data = [
            [1, "JSON file (Default)"],
            [2, "CSV"],
            [3, "Database"],
        ]
        TableIt.printTable(table_data)
        return input("Where would you like to save the data:? ")

    def versionize(self, version):
        return version

    def generate_polygon_questions(self):
        table_data = [
            [1, "Generate polygons for a single country (Default)"],
            [2, "Generate polygons for global data"],
            [3, "Generate polygons for a place"],
        ]
        TableIt.printTable(table_data)
        return input("Choose from the options above:? ")
