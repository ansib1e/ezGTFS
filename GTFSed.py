# Main script
# ansib1e - May 15, 2020 to ....
# Python 3.7

# Basic GTFS (only 6 required files)
from gtfs_definitions import Agency
from gtfs_definitions import Calendar
from gtfs_definitions import Routes
from gtfs_definitions import Stops
from gtfs_definitions import StopTimes
from gtfs_definitions import Trips

import pandas
import array
import time
import os

basicGTFS_agency = Agency('ONTLN', 'Metrolinx', 'http://www.metrolinx.com/en/', 'America/Toronto',None,None,None)

# Functions

# Print clean Dictionary


def print_dictionary(dictionary):
    print("_"*37)
    for x, y in dictionary.items():
        print("| {:15} | {:15} |".format(str(x), str(y)))
    print("="*37)
    return


def generate_raw_agency():
    """
    genera_raw_agency() returns a Pandas DataFrame containing all agency information for a public transit network. This gets fed into another function that
        generates an 'agency.csv' file from this data.
    """
    # Initialize loop
    # Redundant, but more for memory
    required = ["agency_id", "agency_name", "agency_url", "agency_timezone"]
    optional = ["agency_lang", "agency_phone", "agency_fare_url"]
    user_input = ""
    agency_list = []
    req_fields = "\t"
    opt_fields = "\t"

    # Check for choice of optional inputs (IN CONSOLE/TEMPORARY)
    input_loop = True
    session_fields = required.copy()
    print("Step: Generate/input 'agency.txt' data")
    print("The REQUIRED Fields are: ")
    for field_name in required:
        print("\t - "+field_name)
    print("\n")

    while input_loop is True:
        print("Please enter Y/N or y/n for each OPTIONAL field that you would like to add to this GTFS dataset")
        print("The OPTIONAL Fields are: ")
        for field_name in optional:
            while input_loop is True:
                user_input = input("\t [{}] : Please enter Y/N or y/n for whether or not to include this field in 'address.csv':\n".format(field_name))
                if user_input == "Y" or user_input == "y":
                    session_fields.append(field_name)
                    break
                elif user_input == "N" or user_input == "n":
                    break
        print("\n\n")
        # Confirm selection of fields
        print("'agency.csv' fields to be used are: ")
        for field_name in session_fields:
            print("\t - "+field_name)
        print("\n")
        while input_loop is True:
            user_input = input("Please enter Y/N or y/n to Confirm selection of fields to be used:\n".format(field_name))
            if user_input == "Y" or user_input == "y":
                input_loop = False
            elif user_input == "N" or user_input == "n":
                session_fields.clear()
                session_fields = required.copy()
                print("\n\n")
                break

        if input_loop is False:
            break

    # Start of User Input loop (determines size of array)
    logic_loop = True
    print("...Starting INPUT loop...")
    print("\t To Exit at, enter (!Exit) or (!exit) when prompted in the user input")
    temp_agency = {
        "agency_id": "",
        "agency_name": "",
        "agency_url": "",
        "agency_timezone": "",
        "agency_lang": "",
        "agency_phone": "",
        "agency_fare_url": ""
    }
    while logic_loop is True:
        # Individual new agency class
        for field_name in session_fields:
            user_input = str(input("\tPlease enter the '{}' field value:\n".format(field_name)))
            temp_agency[field_name] = user_input
        # Clean empty fields
        for field_name in temp_agency:
            if temp_agency[field_name] == "":
                temp_agency[field_name] = None

        # Test print
        print("\n")
        print_dictionary(temp_agency)



        # Exit point of logic loop (main)
        if user_input == "!exit" or user_input == "!Exit":
            break



    # Start of Parsing loop (Agency class -> list of Pandas Series -> Pandas Dataframe




# ================ CREATE NEW GTFS ===============================================================================================


# ================ Step 1. CSV => General Pandas DataFrame ===============================================================================================

def parse_input_csv(filepath):
    print("Parsing {} for required field inputs...".format(filepath))
    dataframe = pandas.read_csv(filepath)
    print("[+] Successfully extracted .csv data from {}".format(filepath))
    print(dataframe)
    return dataframe

# ================ Step 2. General Pandas DataFrame => Class Objects (indv ROW) => Inividual DataFrames ===============================================================================================
# ================ Step 2.b Class Objects => Pandas DataFrame (add Row to DF)  ===============================================================================================
# START agency.txt -------------------------------------------------------------------------------------------------------------------------------------------------------
def parse_agencyDF_fromClass(agency_obj):
    data = {'agency_id': [agency_obj.agency_id],
            'agency_name': [agency_obj.agency_name],
            'agency_url': [agency_obj.agency_url],
            'agency_timezone': [agency_obj.agency_timezone],
            'agency_lang': [agency_obj.agency_lang],
            'agency_phone': [agency_obj.agency_phone],
            'agency_fare_url': [agency_obj.agency_fare_url]}
    parsed_df = pandas.DataFrame(data, columns=["agency_id", "agency_name", "agency_url", "agency_timezone", "agency_lang", "agency_phone", "agency_fare_url"])
    print('[+] Successfully parsed (cleaned) Agency class object to a Pandas DataFrame')
    return parsed_df
# END agency.txt -------------------------------------------------------------------------------------------------------------------------------------------------------

# START calendar.txt -------------------------------------------------------------------------------------------------------------------------------------------------------
def parse_calendarDF_fromClass(calendar_obj):
    data = {'service_id': [calendar_obj.service_id],
            'monday': [calendar_obj.monday],
            'tuesday': [calendar_obj.tuesday],
            'wednesday': [calendar_obj.wednesday],
            'thursday': [calendar_obj.thursday],
            'friday': [calendar_obj.friday],
            'saturday': [calendar_obj.saturday],
            'sunday': [calendar_obj.sunday],
            'start_date': [calendar_obj.start_date],
            'end_date': [calendar_obj.end_date]}
    parsed_df = pandas.DataFrame(data, columns=["service_id", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "start_date", "end_date"])
    print('[+] Successfully parsed (cleaned) Calendar class object to a Pandas DataFrame')
    return parsed_df
# END calendar.txt -------------------------------------------------------------------------------------------------------------------------------------------------------



# ================ Step 2.a GENERAL DF -> Class Object(s) -> INDV DFs  ===============================================================================================
# START agency.txt -------------------------------------------------------------------------------------------------------------------------------------------------------
def parse_agency_fromGDF(general_input_dataframe):
    # Parses a Pandas DataFrame containing information for 'agency.txt' into an Agency class object
    agency_id = general_input_dataframe['agency_id'][0]
    agency_name = general_input_dataframe['agency_name'][0]
    agency_url = general_input_dataframe['agency_url'][0]
    agency_timezone = general_input_dataframe['agency_timezone'][0]
    agency_lang = None
    agency_phone = None
    agency_fare_url = None
    new_agency = Agency(agency_id, agency_name, agency_url, agency_timezone, agency_lang, agency_phone, agency_fare_url)
    print("[+] Successfully parsed 'agency.txt' data from DataFrame...")
    print(new_agency)
    return parse_agencyDF_fromClass(new_agency)
# END agency.txt -------------------------------------------------------------------------------------------------------------------------------------------------------

# START calendar.txt -----------------------------------------------------------------------------------------------------------------------------------------------------
def parse_calendar_fromGDF(general_input_dataframe):
    # Parses a Pandas DataFrame containing information for 'calendar.txt' into an Calendar class object
    service_id = general_input_dataframe['service_id'][0]
    monday = general_input_dataframe['monday'][0]
    tuesday = general_input_dataframe['tuesday'][0]
    wednesday = general_input_dataframe['wednesday'][0]
    thursday = general_input_dataframe['thursday'][0]
    friday = general_input_dataframe['friday'][0]
    saturday = general_input_dataframe['saturday'][0]
    sunday = general_input_dataframe['sunday'][0]
    start_date = general_input_dataframe['start_date'][0]
    end_date = general_input_dataframe['end_date'][0]
    new_calendar = Calendar(service_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday, start_date, end_date)
    print("[+] Successfully parsed 'calendar.txt' data from DataFrame...")
    print(new_calendar)
    return parse_calendarDF_fromClass(new_calendar) # Output DF containing cleaned Calendar class object
# END calendar.txt -------------------------------------------------------------------------------------------------------------------------------------------------------





# =============== Main CREATE function / logic loop =========================================================================================================


def create_GTFS_files(general_input_filepath, stops_filepath):
    # (!) Assumes that there is only 1 route (!)
    # Initiate output filepaths
    output_agency_path = 'C:/Users/longc/Documents/GTFSed/GTFS Data/test/agency.csv'
    output_calendar_path = 'C:/Users/longc/Documents/GTFSed/GTFS Data/test/calendar.csv'
    output_routes_path = 'C:/Users/longc/Documents/GTFSed/GTFS Data/test/routes.csv'
    output_stops_path = 'C:/Users/longc/Documents/GTFSed/GTFS Data/test/stops.csv'

    # Initiate final DataFrames to be outputted to CSV
    empty_agency_df = pandas.DataFrame(columns=["agency_id", "agency_name", "agency_url", "agency_timezone", "agency_lang", "agency_phone", "agency_fare_url"])
    empty_calendar_df = pandas.DataFrame(columns=["service_id", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "start_date", "end_date"])


    # Step 1. Parse input.csv files to General Pandas DataFrames
    general_dataframe = parse_input_csv(general_input_filepath)
    stops_input_dataframe = parse_input_csv(stops_filepath)

    # Step 2. General DataFrame -> Agency class object
    parsed_agency_DF = parse_agency_fromGDF(general_dataframe)  # Extracted a COMPLETED 'agency.txt' in the form of a DF from the General DataFrame
    parsed_calendar_DF = parse_calendar_fromGDF(general_dataframe) # Extracted a COMPLETED 'calendar.txt' in the form of a DF from the General DataFrame

    # Step 3. Append Agency class object to agency_df
    # ---------------------------------- 'agency'.txt----------------------------------
    cleaned_agency_df = empty_agency_df.append(parsed_agency_DF)
    print("[+] Successfully Merged cleaned Pandas DataFrame to empty, final 'agency.txt' DF")
    print(cleaned_agency_df)
    print('[*] Writing final output to: {} ...'.format(output_agency_path))
    cleaned_agency_df.to_csv(output_agency_path, index=False)
    print("[+] SUCCESFULLY WRITTEN to: {} ...\n[!] Created 'test_agency.csv'...".format(output_agency_path))

    # ---------------------------------- 'calendar'.txt----------------------------------
    cleaned_calendar_df = empty_calendar_df.append(parsed_calendar_DF)
    print("[+] Successfully Merged cleaned Pandas DataFrame to empty, final 'calendar.txt' DF")
    print(cleaned_agency_df)
    print('[*] Writing final output to: {} ...'.format(output_calendar_path))
    cleaned_calendar_df.to_csv(output_calendar_path, index=False)
    print("[+] SUCCESFULLY WRITTEN to: {} ...\n[!] Created 'calendar.csv'...".format(output_calendar_path))


def main():
    # generate_raw_agency()
    create_GTFS_files('GTFS_input.csv', 'GTFS_stops_input.csv')


if __name__ == '__main__':
    main()
