import geocoder

from woodpecker import WoodPecker

cities_not_found = []
cities_found = []

key = 'samtoya'

w = WoodPecker()


def playground1():
    st = w.localize_state('Imārat Umm al Qaywayn', 'United Arab Emirates')
    print(st)


def playground():
    g = geocoder.geonames('Nicaragua', key=key)
    d = geocoder.geonames(g.geonames_id, method='children', key=key)
    features = d.geojson['features']
    for feature in features[9:]:
        if feature['properties']['address'] == 'Departamento de Managua':
            # print(f"{feature['properties']['country']}, {feature['properties']['address']}")
            c = geocoder.geonames(feature['properties']['geonames_id'], method='children', key=key)
            cities = c.geojson['features']
            for city in cities:
                print('--------------------- BEGIN --------------------- ')
                print(city['properties']['address'])
            print('--------------------- END --------------------- ')


if __name__ == '__main__':
    try:
        playground1()
    except KeyboardInterrupt:
        print('You cancelled the operation!')
    finally:
        pass
