import os
import requests
from owl import Owl

key = 'samtoya'


class Hawfinch:
    @classmethod
    def get(cls, amenity, country, should_save=False):
        folder_name = amenity.get('save_as') if amenity.get('save_as') is not None else amenity.get('name')
        folder_path = 'output/Categories/{}/{}.json'.format(country.get('name'), folder_name)
        if os.path.exists(folder_path):
            return
        print('---------------- Fetching {} in {} ----------------'.format(amenity.get('name'), country.get('name')))
        params = cls.build_parameters(amenity, country)
        r = requests.get('https://overpass-api.de/api/interpreter', params=params)
        out = r.json()
        elements = out.get('elements')
        if len(elements) > 0 and should_save:
            print('Found {} {} items to save'.format(len(elements), amenity.get('name')))
            Owl.save_output(elements, folder_path)
        return r.json()

    @staticmethod
    def build_parameters(amenity, country):
        return {"data": f"""
                                        <osm-script output="json" output-config="" timeout="3000">
                                        <query into="searchArea" type="area">
                                            <id-query type="area" ref="{country.get('ref')}" into="searchArea"/>
                                        </query>
                                        <union into="_">
                                            <query into="_" type="node">
                                                <has-kv k="{amenity.get('type')}" modv="" v="{amenity.get('name')}"/>
                                                <area-query from="searchArea"/>
                                                <area-query from="searchArea"/>
                                            </query>
                                            <query into="_" type="way">
                                                <has-kv k="{amenity.get('type')}" modv="" v="{amenity.get('name')}"/>
                                                <area-query from="searchArea"/>
                                                <area-query from="searchArea"/>
                                            </query>
                                            <query into="_" type="relation">
                                                <has-kv k="{amenity.get('type')}" modv="" v="{amenity.get('name')}"/>
                                                <area-query from="searchArea"/>
                                                <area-query from="searchArea"/>
                                            </query>
                                        </union>
                                        <print e="" from="_" geometry="skeleton" ids="yes" limit="" mode="body" n="" order="id" s="" w=""/>
                                        <recurse from="_" into="_" type="down"/>
                                        <print e="" from="_" geometry="skeleton" ids="yes" limit="" mode="skeleton" n="" order="quadtile" s="" w=""/>
                                    </osm-script>
                                """}
