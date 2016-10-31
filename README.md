# Leaflet-Practice
Practicing python data processing and mapping with Leaflet in javascript

# Where can I find the data?
You can download the data on the following links:

[Number of Internet Users per Country in order](https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2153.txt)

[Population per Country in order](https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2119.txt)

# How to prepare the data?
You just change the data above if you need to show a specific country (in this case just delete lines with other countrys). Because the execution with the original data results in the percentage of internet users per country of each country in the file.

# How to use the program
Suppose the name of file with the  Number of Internet Users per Country is named as "internet\_users.txt" and the name of Population per Country is named as "population.txt".

You execute will execute:  python internetpercentage.py --I internet\_users.txt --P population.txt

#How understant the result of the execution?

The execution will show the result as a json and for each country you will have sometihng like this:
'Country':['internet\_users','population','percentage of internet users']

For example, Brasil case result:
'Brazil': ['108,200,000', '205,823,665', '52.57']
