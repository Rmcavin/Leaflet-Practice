##Purpose: This script processes two data sets from the CIA World Factbook. Two
##independent text files, one for population and one for internet users, are
##merged by country, then a fourth field is added for percentage internet users,
##and finally the percentage of the polulation that uses the internet is
##calculated and input into the new field. This data serves as the basis for my
##leaflet map.
##
##Author: Rachel Cavin
##Date: October 30th, 2016

import argparse
import re
import geojson

#Gets text file arguments, text files are CIA World Book downloads for country population and internet use.
parser = argparse.ArgumentParser(description = 'Calculates percentage of country populations that use the internet.')
parser.add_argument('--I', help = 'Path to Internet Users Text File')
parser.add_argument('--P', help = 'Path to Population Text File')
parser.add_argument('--G', help = 'Path to GeoJSON country boundaries File')
parser.add_argument('--D', help = 'Path to output GeoJSON file to use in Leaflet')
args = parser.parse_args()

#Sets text file variables.
int_users_filename = args.I
population_filename = args.P
country_boundaries_filename = args.G
output_data_filename = args.D

#Create a function getdata that will read multiple file names to increase reusability.
def getdata(lines, dictionary):
    for line in lines:
        split_data = re.split('  +', line.strip())
        country = split_data[1]
        value = split_data[2]
        if country in dictionary:
            dictionary[country].append(value)
        else:
            dictionary[country] = [value]
    return;

def getpercentage(dictionary):
    for key, value in dictionary.viewitems():
        if len(value) == 2:
            percent = float(value[0].replace(',','')) / float(value[1].replace(',','')) * 100
            value.append(str('{0:.2f}'.format(percent)))
        #else:
        #    print key
    return;

#Given dictionary and number of items, find the entries with less than num_items
def findGaps(dictionary, num_items):
    gaps = []
    for key, value in dictionary.viewitems():
        print key, len(value)
        if len(value) != num_items:
            gaps.append(key)
    return gaps

def appendValue(dictionary, geoJson):
    for feature in geoJson["features"]:
        country = feature["properties"]["geounit"]

        if country in dictionary and len(dictionary[country]) == 3:
            feature["properties"].update({"int_percent": dictionary[country][2]})
            #feature["properties"]["int_percent"] = dictionary[country][2]
            #print feature["properties"]
        #else:
            #print country

#Gets the data from two seperate text files, one for population and one for internet users.
combined_data = {}
with open(int_users_filename, 'r') as textfile:
    lines = textfile.read().splitlines()
    getdata(lines, combined_data)
with open(population_filename, 'r') as textfile:
    lines = textfile.read().splitlines()
    getdata(lines, combined_data)

getpercentage(combined_data)

with open(country_boundaries_filename, 'r') as textfile:
    boundaries = geojson.load(textfile)
    appendValue(combined_data, boundaries)
    map_data = geojson.dumps(boundaries)

    with open(output_data_filename, "w") as output:
        output.write(map_data)
    #print boundaries
    #print findGaps(combined_data, 2)


print combined_data
