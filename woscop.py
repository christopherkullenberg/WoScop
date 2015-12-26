import csv
import re

#import dataset
#db = dataset.connect('sqlite:///records.db')

scopuscsv = open('scopus.csv','r') # change file-name here
scopusdata = csv.reader(scopuscsv, delimiter=',', quotechar='"')

wostsv = open('wos.tsv', 'r')
wosdata = csv.reader(wostsv, delimiter='\t')

"""
scopustitlelist = []
scopusdoilist = []
wostitlelist =[]
wosdoilist = []
"""
scopuscount = 0
woscount = 0

recordlist = []
therecords = {}


#DOI field in Scopus
for s in scopusdata:
    scopuscount += 1
    #print(s[0])
    stitlelowered = s[1].lower()
    ssplitted = stitlelowered.split()
    sfirstsevenwords = ssplitted[0:6]
    sjoined = ''.join(sfirstsevenwords)
    stitlenonspecialchar = re.sub(r'[^A-Za-z0-9]+',r'',sjoined)
    recordlist.append([stitlenonspecialchar, s[0], s[2], s[1]])


#DOI field in WoS
for w in wosdata:
    woscount += 1
    #print(w)
    #print(w[1])
    titlelowered = w[8].lower()
    splitted = titlelowered.split()
    firstsevenwords = splitted[0:6]
    joined = ''.join(firstsevenwords)
    titlenonspecialchar = re.sub(r'[^A-Za-z0-9]+',r'',joined)
    recordlist.append([titlenonspecialchar, w[1], w[44], w[8]])
    #print(w[8])
    #wostitlelist.append(w[8].lower())
    #wosdoilist.append(w[54])

for r in recordlist:
    therecords.update({r[0]: [r[1], r[2], r[3]]})


result = {}

for key, value in therecords.items():
        if key not in list(result.values()):
            result[key] = value

"""
for key, value in sorted(result.items()):
    print(key, value[0])
"""
with open('output.csv', 'w') as csvfile:
    fieldnames = ['Author', 'Year', 'Title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for key, value in sorted(result.items()):
        #print(value[0])
        writer.writerow({'Author': value[0], 'Year': value[1], 'Title': value[2]})


print("There are originally " + str(scopuscount - 1) + " Scopus records.")
print("There are originally " + str(woscount - 1) + " WoS records.")
print("In total, there are " + str(len(therecords)) + " records.")
print("Length result " + str(len(result)))
