# GTFS_generator
------------------------------

Python application that manages and creates public transit schedules data in static GTFS format.

To-Do:
  - Front End (decide framework)
  - Get clear list of data that can be inputed vs data that should be automated 
  - Finish testing print function

May 25, 2020 Update:
  - finished code for creation of 'stops.txt' and 'tripsp.txt'
  - refactored steps in conversion process from input -> DB -> Class -> DB
    - decided against removing class step entirely for clealiness sake and for it to catch improper input
  - moved 80% of functions/class code to seperate python files from main for readability and organization
  - working on 'stop_times.txt' 
    - figure out calculation for travel times between stops and extracting said information from 'GTFS_input_stops'
    
