# Class definitions

"""
To-Do:
    - Ensure class instance variables (zone_id, wheelchair_boarding) are initialized properly  (cleaned)
"""


class Agency:
    def __init__(self, agency_id, agency_name, agency_url, agency_timezone, agency_lang, agency_phone, agency_fare_url):
        self.agency_id = agency_id  # Required
        self.agency_name = agency_name  # Required
        self.agency_url = agency_url  # Required
        self.agency_timezone = agency_timezone  # Required

        if agency_lang is "" or agency_lang is None:
            self.agency_lang = None
        else:
            self.agency_lang = agency_lang

        if agency_phone is "" or agency_phone is None:
            self.agency_phone = None
        else:
            self.agency_phone = agency_phone

        if agency_fare_url is "" or agency_fare_url is None:
            self.agency_fare_url = None
        else:
            self.agency_fare_url = agency_fare_url

    def __str__(self):
        return " [+] NEW 'agency' Class Object ->\n\t[agency_id : {}, agency_name : {}, agency_url, : {}, agency_timezone : {}, agency_lang, : {}, agency_phone : {}, agency_fare_url : {}]".format(
            self.agency_id, self.agency_name, self.agency_url, self.agency_timezone, self.agency_lang, self.agency_phone, self.agency_fare_url)



class Routes:
    def __init__(self, route_id, route_short_name, route_long_name, route_type, agency_id, route_color, route_text_color):
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
        self.stop_id = stop_id  # Required
        self.stop_name = stop_name  # Required
        self.stop_lat = stop_lat  # Required
        self.stop_lon = stop_lon  # Required

        if zone_id is "" or zone_id is None:
            self.zone_id = None
        else:
            self.zone_id = zone_id

        if location_type is "" or location_type is None:
            self.location_type = None
        else:
            self.location_type = location_type

        if wheelchair_boarding is "" or wheelchair_boarding is None:
            self.wheelchair_boarding = None
        else:
            self.wheelchair_boarding = wheelchair_boarding


class StopTimes:
    def __init__(self, stop_id, trip_id, arrival_time, departure_time, stop_sequence, stop_headsign, drop_off_type, pickup_type):
        self.stop_id = stop_id  # Required
        self.trip_id = trip_id  # Required
        self.arrival_time = arrival_time  # Required
        self.departure_time = departure_time  # Required
        self.stop_sequence = stop_sequence  # Required

        if stop_headsign is "" or stop_headsign is None:
            self.stop_headsign = None
        else:
            self.stop_headsign = stop_headsign

        if drop_off_type is "" or drop_off_type is None:
            self.drop_off_type = None
        else:
            self.drop_off_type = drop_off_type

        if pickup_type is "" or pickup_type is None:
            self.pickup_type = None
        else:
            self.pickup_type = pickup_type


class Trips:
    def __init__(self, trip_id, route_id, service_id,  direction_id, trip_headsign, trip_short_name, block_id, shape_id, wheelchair_access, bikes_allowed,
                 route_variant):
        self.trip_id = trip_id  # Required
        self.route_id = route_id  # Required
        self.service_id = service_id  # Required
        self.direction_id = direction_id  # Required
        self.trip_headsign = trip_headsign  # Required

        if trip_short_name is "" or trip_short_name is None:
            self.trip_short_name = None
        else:
            self.trip_short_name = trip_short_name

        if block_id is "" or block_id is None:
            self.block_id = None
        else:
            self.block_id = block_id

        if shape_id is "" or shape_id is None:
            self.shape_id = None
        else:
            self.shape_id = shape_id

        if wheelchair_access is "" or wheelchair_access is None:
            self.wheelchair_access = None
        else:
            self.wheelchair_access = wheelchair_access

        if bikes_allowed is "" or bikes_allowed is None:
            self.bikes_allowed = None
        else:
            self.bikes_allowed = bikes_allowed

        if route_variant is "" or route_variant is None:
            self.route_variant = None
        else:
            self.route_variant = route_variant


class Calendar:
    def __init__(self, service_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday, start_date, end_date):
        self.service_id = service_id   # Required
        self.monday = int(monday)  # Required
        self.tuesday = int(tuesday)  # Required
        self.wednesday = int(wednesday)  # Required
        self.thursday = int(thursday)  # Required
        self.friday = int(friday)  # Required
        self.saturday = int(saturday)  # Required
        self.sunday = int(sunday)  # Required
        self.start_date = start_date  # Required
        self.end_date = end_date  # Required


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
