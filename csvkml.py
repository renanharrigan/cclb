import simplekml
import csv
import xml.dom.minidom
import sys
from csv import DictReader

inputfile = csv.reader(open('cclb.csv', 'r'))
kml=simplekml.Kml()

for row in inputfile:
    kml.newpoint(name=row[1], coords=[(row[9],row[8])], address=row[2], cryout=row[6]) 


kml.save('cclb.kml')