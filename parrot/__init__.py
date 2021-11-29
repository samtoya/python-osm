import csv
import json
import os

from database import LocalDatabase
from hummingbird import HummingBird
from owl import Owl
from pangolin import Pangolin
from sparrow import Sparrow
from woodpecker import WoodPecker

f = open('/Users/snoocode/Code/PythonProjects/potr/data/global_data.json')
directory_path = '/Users/snoocode/Code/PythonProjects/potr/localized_countries'


def dd(data):
    print(data)
    raise SystemExit


db_writer = LocalDatabase()


class Parrot:
    def __init__(self):
        self.version = 'v1.0.0'
        self.w = WoodPecker()
        self.p = Pangolin()
        self.h = HummingBird()
        self.data = {
            'version_number': self.w.versionize(self.version),
            'countries': {},
        }

    def begin_process(self, country_input):
        data = {
            'version_number': self.w.versionize(self.version),
            'countries': {},
        }
        countries = data.get('countries')
        country = Sparrow.country(country_input.title())
        country_name = country.address
        # .encode('ascii', 'ignore').decode('utf-8')
        localized_country = self.w.localize_country(country_name)
        countries[country_name] = localized_country
        states = Sparrow.children(identifier=country.geonames_id)
        if len(states) > 0:
            print(f'Found {len(states)} states in {country_name}')
            for state in states:
                state_properties = state.get('properties')
                state_name = state_properties.get('address')
                state_identifier = state_properties.get('geonames_id')
                localized_state = self.w.localize_state(state=state_name, country=country_name)
                countries.get(country_name)['divisions'][state_name] = {}
                if localized_state is not None:
                    countries.get(country_name)['divisions'][state_name] = localized_state
                    cities = Sparrow.children(state_identifier, method='children')
                    if len(cities) > 0:
                        print(f'Found {len(cities)} cities in {state_name}, {country_name}')
                        for ct in cities:
                            city_properties = ct.get('properties')
                            city_name = city_properties.get('address')
                            city = self.w.localize_city(city=city_name, state=state_name, country=country_name)
                            countries.get(country_name)['divisions'][state_name]['sub_divisions'][city_name] = {}
                            if city is not None:
                                countries.get(country_name)['divisions'][state_name]['sub_divisions'][
                                    city_name] = city
        return country_name, data

    def save_data_to_file(self, country, data, directory='localized_countries'):
        Owl.save_country_to_file(filename=country, data=data, directory=directory)
        print('\n---------------------- END --------------------------')

    def chirp(self):
        identifier = self.w.ask_for_process_identifier()
        if identifier == '1':
            country_input = self.w.ask_for_country_name()
            country, data = self.begin_process(country_input)
            identifier = self.w.ask_for_where_to_save_data()
            self.handle_saving_data(identifier=identifier, country=country, data=data)
        elif identifier == '2':
            self.chip_with_data()
        elif identifier == '3':
            self.chip_with_local_data()
        elif identifier == '4':
            poly_option = self.w.generate_polygon_questions()
            self.handle_polygon_answer(poly_option)
        else:
            country_input = self.w.ask_for_country_name()
            country, data = self.begin_process(country_input)
            identifier = self.w.ask_for_where_to_save_data()
            self.handle_saving_data(identifier=identifier, country=country, data=data)
            exit(0)

    def chip_with_data(self):
        global_data = json.load(f)
        for country in list(global_data.get('countries').keys()):
            # print(f'----- Begin at: {country} ----- ')
            try:
                if os.path.exists(f'/Users/snoocode/Code/PythonProjects/SnooCODE/potr/output/{country}.json'):
                    continue
                self.begin_process(country)
            except TypeError:
                continue

    def chip_with_local_data(self):
        with open('/Users/snoocode/Code/PythonProjects/SnooCODE/potr/data/ghana.json') as f:
            data = {
                'version_number': self.w.versionize(self.version),
                'countries': {},
            }
            file_loaded = json.load(f)
            countries = data.get('countries')
            for country in file_loaded.get("data"):
                country_name = country['name'].title()
                localized_country = self.w.localize_country(country_name)
                countries[country_name] = localized_country
                for state in country['states']:
                    state_name = state['name'].title()
                    localized_state = self.w.localize_state(state=state['name'], country=country_name)
                    countries.get(country_name)['divisions'][state_name] = localized_state
                    if len(state['cities']) > 0:
                        for city in state['cities']:
                            city_name = city['name'].title()
                            localized_city = self.w.localize_city(city_name, country=country_name, state=state_name)
                            if localized_city is not None:
                                print(f'::::::::::::::::::::::::::: {localized_city} :::::::::::::::::::::::::::')
                                countries.get(country_name)['divisions'][state_name]['sub_divisions'][
                                    city_name] = localized_city
        f.close()
        self.save_data_to_file(country=country_name, data=data)
        identifier = self.w.ask_for_where_to_save_data()
        self.handle_saving_data(identifier=identifier, country=country_name, data=data)

    def handle_saving_data(self, identifier, country, data, directory='output'):
        if identifier == '1':  # JSON
            self.save_as_json(country, data, directory=directory)
        elif identifier == '2':  # CSV
            self.save_as_csv(country, data)
        elif identifier == '3':  # Database
            print('TODO: Setup for that selection isn\'t implemented yet.')
        else:
            self.save_as_json(country, data, directory=directory)

    def save_as_csv(self, country, data):
        with open(f'{directory_path}/{country}.csv', 'w', newline='') as csv_file:
            fieldnames = ['name', 'iso2', 'latitude', 'longitude', 'division_type', 'coordinates']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
            writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
            writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    def save_as_json(self, country, data, directory):
        self.save_data_to_file(country=country, data=data, directory=directory)

    def save_to_database(self):
        # data = localized_country
        # country_inserted_id = db_writer.write_country(localized_country).inserted_id
        # data.get('divisions[state_name] = localized_state
        # divisions[state_name] = localized_state
        # division_inserted_id = None
        # if localized_state is not None:
        # division_inserted_id = db_writer.write_division(country_inserted_id,
        # localized_state).inserted_id
        pass

    def handle_polygon_answer(self, option):
        if option == '1':
            self.retrieve_polygons_for_single_country()
        elif option == '2':
            self.retrieve_polygons_for_global_data()
        elif option == '3':
            self.retrieve_polygons_for_a_place()
        elif option == '4':
            self.retrieve_polygons_for_global_data_and_append()

    def retrieve_polygons_for_single_country(self):
        country_input = self.w.ask_for_country_name().title()
        country_geo = Sparrow.country(country_input.title())
        data = self.h._geocode(country_input)
        if data is not None:
            osm_id = data['osm_id']
            print('-- Getting polygon for : {}, with OSM ID : {}'.format(country_input, osm_id))
            bounds = self.p.generate_boundary_for_place(osm_id)
            data = {
                'boundary': bounds
            }
            self.handle_saving_data(
                identifier='1',
                country=country_input.replace('/', ' '),
                data=data,
                directory=f'polygons/{country_input}'
            )
        states = Sparrow.children(identifier=country_geo.geonames_id)
        if len(states) > 0:
            for state in states:
                state_properties = state.get('properties')
                state_name = state_properties.get('address')
                geo = self.h._geocode(f'{state_name}, {country_input}')
                data = {}
                if geo is not None:
                    osm_id = geo['osm_id']
                    print('-- Getting polygon for : {}, {} with OSM ID : {}'.format(state_name, country_input, osm_id))
                    bounds = self.p.generate_boundary_for_place(osm_id)
                    data['boundary'] = bounds
                    filename = f'{country_input}${state_name}'.replace('/', ' ')
                    self.handle_saving_data(
                        identifier="1",
                        country=filename,
                        data=data,
                        directory=f'polygons/{country_input}'
                    )
                state_identifier = state_properties.get('geonames_id')
                cities = Sparrow.children(state_identifier, method='children')
                if len(cities) > 0:
                    print(f'Found {len(cities)} cities in {state_name}, {country_input}')
                    for ct in cities:
                        city_properties = ct.get('properties')
                        city_name = city_properties.get('address')
                        geo = self.h._geocode(f'{state_name}, {country_input}')
                        data = {}
                        if geo is not None:
                            osm_id = geo['osm_id']
                            print('-- Getting polygon for : {}, {}, {} with OSM ID : {}'.format(city_name, state_name,
                                                                                                country_input, osm_id))
                            bounds = self.p.generate_boundary_for_place(osm_id)
                            data['boundary'] = bounds
                            filename = f'{country_input}${state_name}${city_name}'.replace('/', ' ')
                            self.handle_saving_data(
                                identifier="1",
                                country=filename,
                                data=data,
                                directory=f'polygons/{country_input}'
                            )

    def retrieve_polygons_for_global_data(self):
        global_data = json.load(f)
        for country in list(global_data.get('countries').keys()):
            country_name = country.title()
            data = self.h._geocode(country_name)
            if data is not None:
                osm_id = data['osm_id']
                print('-- Getting polygon for : {}, with OSM ID : {}'.format(country_name, osm_id))
                bounds = self.p.generate_boundary_for_place(osm_id)
                data = {
                    'boundary': bounds
                }
                self.handle_saving_data(
                    identifier='1',
                    country=country_name.replace('/', ' '),
                    data=data,
                    directory=f'polygons/{country_name}'
                )
            states = list(global_data.get('countries').get(country).get('divisions').keys())
            if len(states) > 0:
                for state in states:
                    state_name = state.title()
                    geo = self.h._geocode(f'{state_name}, {country_name}')
                    data = {}
                    if geo is not None:
                        osm_id = geo['osm_id']
                        print('-- Getting polygon for : {}, {} with OSM ID : {}'.format(state_name, country_name,
                                                                                        osm_id))
                        bounds = self.p.generate_boundary_for_place(osm_id)
                        data['boundary'] = bounds
                        filename = f'{country_name}${state_name}'.replace('/', ' ')
                        self.handle_saving_data(
                            identifier="1",
                            country=filename,
                            data=data,
                            directory=f'polygons/{country_name}'
                        )
                    cities = list(global_data.get('countries').get(country).get('divisions').get(state).get(
                        'sub_divisions').keys())
                    if len(cities) > 0:
                        for city_name in cities:
                            geo = self.h._geocode(f'{state_name}, {country_name}')
                            data = {}
                            if geo is not None:
                                osm_id = geo['osm_id']
                                print('-- Getting polygon for : {}, {}, {} with OSM ID : {}'.format(city_name,
                                                                                                    state_name,
                                                                                                    country_name,
                                                                                                    osm_id))
                                bounds = self.p.generate_boundary_for_place(osm_id)
                                data['boundary'] = bounds
                                filename = f'{country_name}${state_name}${city_name}'.replace('/', ' ')
                                self.handle_saving_data(
                                    identifier="1",
                                    country=filename,
                                    data=data,
                                    directory=f'polygons/{country_name}'
                                )

    def retrieve_polygons_for_a_place(self):
        pass

    def retrieve_polygons_for_global_data_and_append(self):
        global_data = json.load(f)
        data = global_data
        for country in list(global_data.get('countries').keys()):
            try:
                country_data = data.get("countries").get(country)
                if 'boundary_polygon' in country_data:
                    continue
                country_name = country.title()
                geocoded_country = self.h._geocode(country_name)
                if geocoded_country is not None:
                    osm_id = geocoded_country['osm_id']
                    print(f'-- Getting polygon for : {country_name}, with OSM ID : {osm_id}')
                    bounds = self.p.generate_boundary_for_place(osm_id)
                    country_data['boundary_polygon'] = bounds
                divisions = list(global_data.get('countries').get(country).get('divisions').keys())
                if len(divisions) > 0:
                    for division in divisions:
                        try:
                            division_data = data.get("countries").get(country).get('divisions').get(division)
                            if 'boundary_polygon' in division_data:
                                continue
                            state_name = division.title()
                            geocoded_state = self.h._geocode(f'{state_name}, {country_name}')
                            if geocoded_state is not None:
                                osm_id = geocoded_state['osm_id']
                                print(f'-- Getting polygon for : {state_name}, {country_name}, with OSM ID : {osm_id}')
                                bounds = self.p.generate_boundary_for_place(osm_id)
                                division_data['boundary_polygon'] = bounds
                            sub_divisions = list(
                                global_data.get('countries').get(country).get('divisions').get(division).get(
                                    'sub_divisions').keys())
                            if len(sub_divisions) > 0:
                                for sub_division in sub_divisions:
                                    try:
                                        sub_division_data = data.get("countries").get(country).get('divisions').get(
                                            division).get(
                                            'sub_divisions').get(sub_division)
                                        if 'boundary_polygon' in sub_division_data:
                                            continue
                                        city_name = division.title()
                                        geocoded_city = self.h._geocode(f'{city_name}, {state_name}, {country_name}')
                                        if geocoded_city is not None:
                                            osm_id = geocoded_city['osm_id']
                                            print(
                                                f"-- Getting polygon for : {city_name}, {state_name}, {country_name}, with OSM ID : {osm_id}")
                                            bounds = self.p.generate_boundary_for_place(osm_id)
                                            sub_division_data['boundary_polygon'] = bounds
                                    except KeyError:
                                        continue
                        except KeyError:
                            continue
            except KeyError:
                print(f"Couldn't find data for: {country}")
                continue
            except:
                print(f"Couldn't find data for: {country}")
                continue
        self.handle_saving_data(
            identifier="1",
            country='global_data',
            data=data,
            directory='global'
        )
