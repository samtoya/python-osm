import json

import requests


class Pangolin:
    def __init__(self):
        self.base_url = 'https://polygons.openstreetmap.fr/get_geojson.py?id'
        self.requests = requests

    def make_request(self, url):
        r = self.requests.get(url)
        if r.status_code == 200:
            data = r.text.lstrip().rstrip().strip()
            if data != 'None' or data != "b'None'":
                return r.json()
            return None
        return None

    def get_simplified_polygons(self, osm_id):
        url = f'{self.base_url}={osm_id}&params=0.020000-0.005000-0.005000'
        return self.make_request(url)

    def get_complex_polygons(self, osm_id):
        url = f'{self.base_url}={osm_id}'
        return self.make_request(url)

    def get_polygon(self, osm_id):
        polygons = []
        poly_type = -1  # Not found
        try:
            polys = self.get_simplified_polygons(osm_id)
            if polys is not None:
                polygons = polys
                poly_type = 0  # simplified polygon
        except json.decoder.JSONDecodeError:
            try:
                polys = self.get_complex_polygons(osm_id)
                if polys is not None:
                    polygons = polys
                    poly_type = 1  # complex polygon
            except json.decoder.JSONDecodeError:
                polygons = []
                poly_type = -1
        finally:
            return poly_type, polygons

    def generate_boundary_for_place(self, osm_id):
        boundary = []
        poly_type, boundaries = self.get_polygon(osm_id)
        if poly_type == 0:
            polygon_type = "Found simplified polygon data"
        elif poly_type == 1:
            polygon_type = "Found complex polygon data"
        else:
            polygon_type = "Could not get polygon"
        # print(f'{polygon_type} : {poly_type}')
        # counter = 0
        if poly_type != -1 and boundaries is not None and isinstance(boundaries, dict):
            if "geometries" in boundaries:
                geometries = boundaries['geometries'][0]
                if 'coordinates' in geometries:
                    coordinates = geometries['coordinates']
                    boundary = coordinates
                    # for coordinate in coordinates:
                    #     for bound in coordinate:
                    #         for b in bound:
                    #             d = [b[0], b[1]]
                    #             boundary.append(d)
                    #         counter += 1
            elif 'coordinates' in boundaries:
                coordinates = boundaries['coordinates']
                boundary = coordinates
                # for coordinate in coordinates:
                #     for bound in coordinate:
                #         for b in bound:
                #             d = [b[0], b[1]]
                #             boundary.append(d)
                #         counter += 1
        else:
            boundary = []
        return boundary
