
def ok_result(place, d):
    return """
        Country: {}
        OSM ID: {}
        OSM Type: {}
        Type: {}
        Category: {}
        BBox: {}
        BoundingBox: {}
        Importance: {}
        Latitude: {}
        Longitude: {}
        -------
        """.format(
        d['name'],
        place['osm_id'],
        place['osm_type'],
        place['raw']['type'],
        place['raw']['category'],
        place['bbox'],
        place['raw']['boundingbox'],
        place['raw']['importance'],
        place['lat'],
        place['lng'],
    )


def not_ok_result():
    return """
        OSM ID: {}
        OSM Type: {}
        Type: {}
        Category: {}
        BBox: {}
        BoundingBox: {}
        Importance: {}
        Latitude: {}
        Longitude: {}
        -------
        """.format(
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )