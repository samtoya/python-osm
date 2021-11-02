import math

import geocoder

from pangolin import Pangolin

pangolin = Pangolin()


class HummingBird:
    def localize_country(self, v):
        print('--------------- Country : {} --------------'.format(v))
        osm = self._geocode(v)
        if osm is not None:
            return {
                # 'country': osm,
                'name': v,
                'iso2': osm['country_code'].upper(),
                # 'latitude': float(osm['lat']),
                # 'longitude': float(osm['lng']),
                'division_type': 'State',
                'coordinates': self._get_country_coordinates(osm['bbox']),
                # 'osm_id': osm['osm_id'],
                # 'polygon': pangolin.generate_boundary_for_place(osm['osm_id']),
                'divisions': {}
            }
        return osm

    def localize_state(self, state, country):
        print('-- Localizing State : {}, {}'.format(state, country))
        osm = self._geocode('{}, {}'.format(state, country))
        if osm is not None and len(osm) > 0:
            return {
                # 'division': osm,
                'name': state,
                # 'country': country,
                # 'latitude': float(osm['lat']),
                # 'longitude': float(osm['lng']),
                'coordinates': self._get_division_coordinates(osm['bbox']),
                # 'polygon': pangolin.generate_boundary_for_place(osm['osm_id']),
                'sub_divisions': {}
            }
        return osm

    def localize_city(self, city, state, country):
        print('---- Localizing City : {}, {}, {}'.format(city, state, country))
        osm = self._geocode('{}, {}, {}'.format(city, state, country))
        if osm is not None and len(osm) > 0:
            north_east = osm['bbox'].get('northeast')
            south_west = osm['bbox'].get('southwest')
            south_latitude = float(south_west[0])
            north_latitude = float(north_east[0])
            west_longitude = float(south_west[1])
            east_longitude = float(north_east[1])
            data = {
                # 'sub_division': osm
                'name': city,
                'type': 'city',
                # 'state': state,
                # 'country': country,
                # 'latitude': float(osm['lat']),
                # 'longitude': float(osm['lng']),
                # 'north_latitude': north_latitude,
                # 'south_latitude': south_latitude,
                # 'west_longitude': west_longitude,
                # 'east_longitude': east_longitude,
                'coordinates': self._coordinates(
                    north_latitude, south_latitude, west_longitude, east_longitude
                ),
            }
            # if 'osm_id' in osm:
            #     data['osm_id'] = osm['osm_id']
            #     data['polygon'] = pangolin.generate_boundary_for_place(osm['osm_id'])
            # else:
            #     print(f'City with issue: {city}')
            #     print(f'City with issue: {osm}')
            return data
        return {}

    def _geocode(self, country):
        g = geocoder.osm(country)
        if g.ok and g.json is not None:
            osm = g.json
            if osm['ok']:
                return osm
        return None

    def _get_country_coordinates(self, bbox):
        north_east = bbox.get('northeast')
        south_west = bbox.get('southwest')

        extra = 0.003

        west_longitude = float(south_west[1]) - extra
        east_longitude = float(north_east[1]) + extra
        south_latitude = float(south_west[0]) - extra
        north_latitude = float(north_east[0]) + extra

        return [
            west_longitude, east_longitude, south_latitude, north_latitude
        ]

    def _get_division_coordinates(self, bbox):
        north_east = bbox.get('northeast')
        south_west = bbox.get('southwest')

        extra = 0.001

        west_longitude = float(south_west[1]) - extra
        east_longitude = float(north_east[1]) + extra
        south_latitude = float(south_west[0]) - extra
        north_latitude = float(north_east[0]) + extra

        return [
            west_longitude, east_longitude, south_latitude, north_latitude
        ]

    def _get_center_coordinates(self, bbox):
        # Find the center latitude
        north_east = bbox.get('northeast')
        south_west = bbox.get('southwest')

        south_latitude = float(south_west[0])
        north_latitude = float(north_east[0])

        center_latitude = (north_latitude + south_latitude) / 2
        # Find the center longitude
        center_longitude = self._get_center_longitude(bbox)
        # Calculate the radius
        radius = self._get_radius(north_latitude, center_latitude)

        return [
            center_latitude, center_longitude, radius
        ]

    def _get_center_longitude(self, bbox):
        # Find the center latitude
        north_east = bbox.get('northeast')
        south_west = bbox.get('southwest')
        west_longitude = float(south_west[1])
        east_longitude = float(north_east[1])

        mid_longitude = (west_longitude + east_longitude) / 2

        if 0 < west_longitude < 180 and -180 < east_longitude < 0:
            half_angle = (abs(east_longitude) + abs(180 - west_longitude)) / 2
            mid_angle = west_longitude + half_angle
            if mid_angle > 180:
                mid_longitude = 180 - mid_angle
            else:
                mid_longitude = mid_angle

        return mid_longitude

    def _get_radius(self, north_latitude, center_latitude):
        circumference_of_earth = 40075000
        return (((north_latitude - center_latitude) * circumference_of_earth) / 360.0) + 2000

    def _coordinates(self, north_latitude, south_latitude, west_longitude, east_longitude):
        center_latitude = (north_latitude + south_latitude) / 2
        latitude_span = north_latitude - south_latitude

        if -180 < east_longitude < west_longitude < 180:
            start_angle = 180 - west_longitude
            end_angle = east_longitude - 180
            longitude_span = start_angle + end_angle

            mid_longitude = longitude_span / 2
            center_longitude = west_longitude + mid_longitude - 180

        else:
            longitude_span = east_longitude - west_longitude
            center_longitude = (west_longitude + east_longitude) / 2

        if south_latitude < 0 and north_latitude > 0:
            base_latitude = 0
        else:
            if north_latitude > south_latitude:
                base_latitude = north_latitude
            else:
                base_latitude = south_latitude

        if longitude_span > latitude_span:
            base_latitude_circumference = 2 * math.pi * 6371000 * math.cos(base_latitude * math.pi / 180)
            radius = base_latitude_circumference * longitude_span / 360
        else:
            radius = (latitude_span * 40075000 / 360) + 2000

        return [center_latitude, center_longitude, radius]
