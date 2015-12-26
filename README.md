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
- An exported tsv file from Thomson-Reuters Web of Science (saved as "Macintosh Unicode")

### Output
The output is a regular csv file with the fields:
- Author (AU)
- Year (PY)
- Title (TI)
- Journal (SO)
- Volume (VL)
- Issue (IS)

To include more information here, just fill up the script with the respective fields from the Scopus and WoS data.

### Description of the deduplication algorithm
To find duplicates, this script removes identical titles. Due to formatting inconsistencies in the Scopus and Web of Science databases, a few steps are taken to simplify the titles. The procedure works like this:

1. Titles are converted to lower case letters only (Python's lower() method).
2. Only the first seven words of the title are included for further processing (to avoid long titles in multiple languages).
3. A regular expression - `[^A-Za-z0-9]+` - is applied to only allow letters and numbers (removing all special characters and spaces).
4. The result is a string like this: `aphotogrammetricapproachforassessingpositionalaccuracy`, which is used as an unique identifier to avoid adding the same article twice to the final merging of the datasets.  


### Known sources of error
- Fails to find duplicates if an extra letter is in the title [A-Z-a-z]. For example, `car` and `cars`.
- Because the title strings are split and joined before special characters are removed with regular expressions, the following false positive (duplicate) appears:


    Geospatial Metadata 2.0 - An approach for Volunteered Geographic
    
    Geospatial Metadata 2.0-An approach for Volunteered Geographic

- There is no function (yet) to sort out empty records. So there can be one or two half-empty rows in the final csv output file. Weed our manually if needed.
