#Program to add city and state to a csv of US zipcodes
#Chris Varney
#5/4/2018

import csv
#$ pip install uszipcode
from uszipcode import ZipcodeSearchEngine

#Takes the name of the source csv and the name of the blank file to output to
#For source csv - first column is lead id, second column is zip codes, third and fourth columns are blank for city and state
def csvReadWrite(filenameIn, filenameOut):
    with open(filenameIn, 'r') as csvfile,open(filenameOut, 'w', newline='') as out:
        w = csv.writer(out)
        r = csv.reader(csvfile)

        headers = next(r, None)
        if headers:
            w.writerow(headers)

        for row in r:
            zipcode = str(row[1])
            city,state = findCityState(zipcode)
            row[2] = str(city)
            row[3] = str(state)
            w.writerow(row)

#Takes zipcode and returns city and state (state as abbreviation)
#Is called by csvReadWrite function for every row in csv
def findCityState(zipcode):
    search = ZipcodeSearchEngine()

    zip = search.by_zipcode(zipcode)

    city = zip.City
    state = zip.State

    return (city,state)

#Defines filepath for source csv and output csv and then runs csvReadWrite function
def main():
    #first column is lead id, second column is zip codes, third and fourth columns are blank for city and state
    #TODO
    #Update file path
    file_path_in = r'C:\Users\......csv'
    file_path_out = r'C:\Users\.....csv'
    csvReadWrite(file_path_in)

main()
