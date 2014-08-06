import urllib2
import re
import csv

urls = [['http://www.formula1.com/results/season/2014/914/', 'Melbourne'],
        ['http://www.formula1.com/results/season/2014/915/', 'Kuala Lumpur'],
        ['http://www.formula1.com/results/season/2014/916/', 'Sakhir'],
        ['http://www.formula1.com/results/season/2014/917/', 'Shanghai'],
        ['http://www.formula1.com/results/season/2014/919/', 'Catalunya'],
        ['http://www.formula1.com/results/season/2014/920/', 'Monte Carlo'],
        ['http://www.formula1.com/results/season/2014/922/', 'Montreal'],
        ['http://www.formula1.com/results/season/2014/923/', 'Spielberg'],
        ['http://www.formula1.com/results/season/2014/924/', 'Silerstone'],
        ['http://www.formula1.com/results/season/2014/925/', 'Hockenhein'],
        ['http://www.formula1.com/results/season/2014/926/', 'Budapest'],
        ['http://www.formula1.com/results/season/2014/927/', 'Spa-Francorchamps'],
        ['http://www.formula1.com/results/season/2014/928/', 'Monza'],
        ['http://www.formula1.com/results/season/2014/929/', 'Singapore'],
        ['http://www.formula1.com/results/season/2014/930/', 'Suzuka'],
        ['http://www.formula1.com/results/season/2014/931/', 'Sochi'],
        ['http://www.formula1.com/results/season/2014/932/', 'Austin']]

urlobjlist = []

for url in urls:
    result_object_list = []
    response = urllib2.urlopen(url[0])
    response_list = response.readlines()
    for index, line in enumerate(response_list):
        if line.find('Results for this session are not yet available') > 0:
            break
        if line.find('<a href="/results/driver/') > 0:
            stripped = re.sub('<[^>]*>', '', line)
            clean = stripped.strip()
            if clean != 'DRIVER':
                event = url[1]
                first_name, last_name = clean.split()
                place = re.sub('<[^>]*>', '', response_list[index-2].strip())
                laps = re.sub('<[^>]*>', '', response_list[index+4].strip())
                time_or_ret = re.sub('<[^>]*>', '', response_list[index+7].strip())
                grid = re.sub('<[^>]*>', '', response_list[index+11].strip())
                points = re.sub('<[^>]*>', '', response_list[index+12].strip())
                urlobjlist.append([event, first_name, last_name, place, laps, time_or_ret, grid, points])


with open("results.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(urlobjlist)
	driver_input_string = "    Driver(first_name='%s',last_name='%s',team='%s',number=%s,current_driver=%s).save()\n"
	event_input_string = "    Event(name='%s',location='%s',start_time='%s').save()\n"
	results_input_string = "    Results(event=%s,driver=%s,place='%s',laps='%s',time_or_retired='%s',grid=%s, points=%s).save()\n"
	get_event_string = "    e = Event.objects.get(location='%s')\n"
	get_driver_string = "    d = Driver.objects.get(last_name='%s')\n"

	f = open('output_scirpt.py', 'w')

	f.write("from game.models import Driver, Events, Results\n\n\n")
	f.write("def insert_data():\n")

	item_selector = 1
	for line in open('results.csv'):
	    if line == '<split>\n':
	        item_selector += 1
	    elif item_selector == 1:
	        first_name, last_name, team, number, current_driver = line.split(',')
	        python_string = driver_input_string % (first_name.strip(), last_name.strip(), team.strip(), number.strip(), current_driver.strip())
	        f.write(python_string)
	    elif item_selector == 2:
	        name, location, start_time = line.split(',')
	        python_string = event_input_string % (name.strip(), location.strip(), start_time.strip())
	        f.write(python_string)
	    elif item_selector == 3:
	        event_location, driver_first_name, driver_last_name, place, laps, time, grid, points = line.split(',')
	        if points.strip() == '':
	            points = '0'
	        python_string = get_event_string % location
	        f.write(python_string)
	        python_string = get_driver_string % driver_last_name
	        f.write(python_string)
	        python_string = results_input_string % ('e', 'd', place.strip(), laps.strip(), time.strip(), grid.strip(), points.strip())
	        f.write(python_string)
	f.close()
