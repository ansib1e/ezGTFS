# Class definitions

"""
To-Do:
    - Ensure class instance variables (zone_id, wheelchair_boarding) are initialized properly  (cleaned)
"""


class Agency:
    def __init__(self, agency_id, agency_name, agency_timezone, agency_lang, agency_phone, agency_url, agency_fare_url):
        self.agency_id = agency_id  # Required
        self.agency_name = agency_name  # Required
        self.agency_url = agency_url  # Required
        self.agency_timezone = agency_timezone  # Required

        if agency_lang is "" or agency_lang is None:
            self.agency_lang = None
        else:
            self.agency_lang = agency_lang

        if agency_phone is "" or agency_lang is None:
            self.agency_phone = None
        else:
            self.agency_phone = agency_phone

        if agency_fare_url is "" or agency_fare_url is None:
            self.agency_fare_url = None
        else:
            self.agency_fare_url = agency_fare_url


class Routes:
    def __init__(self, route_id, agency_id, route_short_name, route_long_name, route_type, route_color, route_text_color):
        self.route_id = route_id  # Required
        self.route_short_name = route_short_name  # Required
        self.route_long_name = route_long_name  # Required
        self.route_type = route_type   # Required

        if agency_id is "" or agency_id is None:
            self.agency_id = None
        else:
            self.agency_id = agency_id

        if route_color is "" or route_color is None:
            self.route_color = None
        else:
            self.route_color = route_color

        if route_text_color is "" or route_text_color is None:
            self.route_text_color = None
        else:
            self.route_text_color = route_text_color


class Stops:
    def __init__(self, stop_id, stop_name, stop_lat, stop_lon, zone_id, location_type, wheelchair_boarding):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon
        self.zone_id = zone_id
        self.location_type = location_type
        self.wheelchair_boarding = wheelchair_boarding


class StopTimes:
    def __init__(self, trip_id, arrival_time, stop_id, stop_headsign, drop_off_type, pickup_type, stop_sequence, departure_time):
        self.trip_id = trip_id
        self.arrival_time = arrival_time
        self.stop_id = stop_id
        self.stop_headsign = stop_headsign
        self.drop_off_type = drop_off_type
        self.pickup_type = pickup_type
        self.stop_sequence = stop_sequence
        self.departure_time = departure_time


class Trips:
    def __init__(self, route_id, service_id, trip_id, trip_headsign, trip_short_name, direction_id, block_id, shape_id, wheelchair_access, bikes_allowed,
                 route_variant):
        self.route_id = route_id
        self.service_id = service_id
        self.trip_id = trip_id
        self.trip_headsign = trip_headsign
        self.trip_short_name = trip_short_name
        self.direction_id = direction_id
        self.block_id = block_id
        self.shape_id = shape_id
        self.wheelchair_access = wheelchair_access
        self.bikes_allowed = bikes_allowed
        self.route_variant = route_variant


class Calendar:
    def __init__(self, service_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday, start_date, end_date):
        self.service_id = service_id
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.start_date = start_date
        self.end_date = end_date


# Conditional Files

class CalendarDates:
    def __init__(self, service_id, date, exception_type):
        self.service_id = service_id
        self.date = date
        self.exception_type = exception_type


class FareAttributes:
    def __init__(self, fare_id, price, currency_type, payment_method, transfers):
        self.fare_id = fare_id
        self.price = price
        self.currency_type = currency_type
        self.payment_method = payment_method
        self.transfers = transfers


class FareRules:
    def __init__(self, fare_id, origin_id, destination_id):
        self.fare_id = fare_id
        self.origin_id = origin_id
        self.destination_id = destination_id


class Shapes:
    def __init__(self, shape_id, shape_pt_sequence, shape_pt_lat, shape_pt_lon):
        self.shape_id = shape_id
        self.shape_pt_sequence = shape_pt_sequence
        self.shape_pt_lat = shape_pt_lat
        self.shape_pt_lon = shape_pt_lon
