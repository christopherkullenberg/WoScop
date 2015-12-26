# WoScop
Merge Scopus and Web of Science datasets. Removes duplicates according to Titles, then write a new csv-file.

This is just a Proof of Concept. Please read through the code properly before using it in production / research.  

**Note**: This repository has been tested two datasets with less than 2000 records each, used only for the purpose of testing the duplicate removal algorithm. Download the [Scopus csv file](http://scientometrics.flov.gu.se/files/scopus.csv) and the [Web of Science tsv file](http://scientometrics.flov.gu.se/files/wos.tsv). 

### Usage

    python3 woscop.py scopus.csv wos.tsv

To print out the new file created (output.csv):

    python3 printoutput.py



### Input
- An exported csv file from the Scopus database.
- An exported tsv file from Thomson-Reuters Web of Science (saved as "Macintos Unicode")

### Output
The output is a regular csv file with the fields:
- Author (AU)
- Year (PY)
- Title (TI)
- Journal (SO)
- Volume (VL)
- Issue (IS)

To include more information here, just fill up the script with the respective fields from the Scopus and WoS data.

### Known sources of error
- Fails to find duplicates if an extra letter is in the title [A-Z-a-z]. For example, `car` and `cars`.
