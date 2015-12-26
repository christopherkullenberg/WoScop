import csv

#Open and parse the output file
outputfile = open('output.csv','r') # change file-name here
outputdata = csv.reader(outputfile, delimiter=',', quotechar='"')

#Print a pretty bibliography
for o in outputdata:
    print(o[0] + ", (" + o[1] + ') "' + o[2] + '", ' + o[3] + ", (" + o[4] + ": " + o[5] + ")\n")
