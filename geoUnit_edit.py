##purpose: This script edits the geounit value in a geoJson of countries,
##country attributes, and country geometries. The names must be edited to match
##an existing python dictionary.
##
#Author: Rachel Cavin
##Date: 11/25/2016

import argparse
import re
import geojson

parser = argparse.ArgumentParser(description = "Edits the names of countries in a geojson file")
parser.add_argument('--G', help = 'Path to GeoJSON file')
parser.add_argument('--E', help = 'Path to the new edited GeoJSON file')
args = parser.parse_args()

country_Filename = args.G
edited_Filename = args.E

def nameChange(geoJson):
    for feature in geoJson["features"]:
        country = feature["properties"]["geounit"]

        if country == "The Bahamas":
            feature["properties"]["geounit"] = "Bahamas, The"
        if country == "United States of America":
            feature["properties"]["geounit"] = "United States"
        if country == "Northern Cyprus":
            feature["properties"]["geounit"] = "Cyprus"
        if country == "South Korea":
            feature["properties"]["geounit"] = "Korea, South"
        if country == "East Timor":
            feature["properties"]["geounit"] = "Timor-Leste"
        if country == "Ivory Coast":
            feature["properties"]["geounit"] = "Cote d'Ivoire"
        if country == "Democratic Republic of the Congo":
            feature["properties"]["geounit"] = "Congo, Democratic Republic of the"
        if country == "Republic of Congo":
            feature["properties"]["geounit"] = "Congo, Republic of the"
        if country == "Cape Verde":
            feature["properties"]["geounit"] = "Cabo Verde"
        if country == "Gambia":
            feature["properties"]["geounit"] = "Gambia, The"
        if country == "Guinea Bissau":
            feature["properties"]["geounit"] = "Guinea-Bissau"
        if country == "United Republic of Tanzania":
            feature["properties"]["geounit"] = "Tanzania"
        if country == "Czech Republic":
            feature["properties"]["geounit"] = "Czechia"
        if country == "Republic of Serbia":
            feature["properties"]["geounit"] = "Serbia"
        if country == "Federated States of Micronesia":
            feature["properties"]["geounit"] = "Micronesia, Federated States of"

with open(country_Filename, "r") as textfile:
    countries = geojson.load(textfile)
    nameChange(countries)
    fixed_countries = geojson.dumps(countries)

    with open(edited_Filename, "w") as output:
        output.write(fixed_countries)
