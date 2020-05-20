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


basic_GTFSagency = Agency('ONTLN', 'Metrolinx', 'http://www.metrolinx.com/en/', 'America/Toronto')



def buildAgency():
    print("")