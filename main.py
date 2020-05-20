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
    while logic_loop is True:
        # Individual new agency class
        for field_name in session_fields:

            user_input = input("\tPlease enter the '{}' field value:".format(field_name))



        # Exit point of logic loop (main)
        if user_input == "!exit" or user_input == "!Exit":
            break
    # Start of Parsing loop (Agency class -> list of Pandas Series -> Pandas Dataframe
def generateRawGTFSdata_Basic():
    print('Generating raw GTFS data...')


def main():
    generate_raw_agency()


if __name__ == '__main__':
    main()
