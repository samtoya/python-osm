import geocoder

from pangolin import Pangolin

pang = Pangolin()


def distance_tester():
    home = 5.70541720, -0.21805469
    office = 5.560635659441462, -0.2970749812889153
    distance = geocoder.distance(home, office)
    print(f"Distance from origin to target is: {distance}km")


def geocode(country):
    g = geocoder.osm(country.capitalize())
    print(f'G: {g.json}')
    # if g.geojson is not None:
    #     osm = g.json
    # print(f'OSM: {osm}')
    # if osm['ok']:
    #     print(osm['osm_id'])


def polygon_generator(osm_id):
    boundary = pang.get_polygon(osm_id)
    print(boundary)
    print(f'Boundaries Length : {len(boundary)}')


if __name__ == '__main__':
    g = geocoder.geonames(location='1382494', key='samtoya', method='children').geojson
    print(g)
    # country_input = input("Generate polygon for what country?: ")
    # geocode('Tel Aviv, Israel')
    # polygon_generator(192800)
