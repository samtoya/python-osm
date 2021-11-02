import geocoder

key = 'samtoya'
key1 = 'jakitoye'
key2 = 'j.akitoye'


class Sparrow:
    @staticmethod
    def country(country):
        try:
            g = geocoder.geonames(location=country, key=key)
            return geocoder.geonames(location=g.geonames_id, key=key, method='details')
        except:
            try:
                return geocoder.geonames(location=g.geonames_id, key=key1, method='details')
            except:
                return geocoder.geonames(location=g.geonames_id, key=key2, method='details')

    @classmethod
    def children(cls, identifier, method='children'):
        try:
            data = geocoder.geonames(location=identifier, key=key, method=method).geojson
            return data.get('features')
        except:
            try:
                data = geocoder.geonames(location=identifier, key=key1, method=method).geojson
                return data.get('features')
            except:
                data = geocoder.geonames(location=identifier, key=key2, method=method).geojson
                return data.get('features')

    @staticmethod
    def get_detail(geonames_id):
        try:
            return geocoder.geonames(geonames_id, key=key, method='details').geojson
        except:
            try:
                return geocoder.geonames(geonames_id, key=key1, method='details').geojson
            except:
                return geocoder.geonames(geonames_id, key=key2, method='details').geojson
