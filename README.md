Odds-and-Ends
=============

Misc. tools


BaseX.py
- Method to convert a base10 number to a base anything.
- can be imported into another python module or used as a cmd line utility in the following format
- python BaseX.py (base10 to convert from) (baseX to convert to)
- anything above base36 is pretty much useless because a single place can be represented by multiple characters



F1_results_scraper.py
-script that gets all the race results for the 2014 Formula 1 Season
-outputs data into a csv file named "results.csv" 
-data in is the following format... event_location, first_name, last_name, place, laps, time, grid, points
-event location can be changed by changing the second list item next to the urls, event location is just what i needed specifically
-events with results that have not been posted yet will be ignored
