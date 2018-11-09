#sort images into directories for processing

import csv
import subprocess

DIRECTORIES = ["one_star","two_star","three_star","four_star","five_star"]
with open("books.csv",'r') as books:
    reader = csv.reader(books)
    next(reader) #skip header

    for index, row in enumerate(reader):
        if(index % 1000 == 0):
            print(index)
        stars = int(row[0])
        directory = DIRECTORIES[stars - 1] # ArRaYs ArE zErO-iNdExEd
        title = row[1].replace(" ","")
        url   = row[2]
        # ignore default photos
        if(url != "https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png"):
            subprocess.call(["curl", url, "-o", f'{directory}/{title}.jpg'])
        
        
# Function used to make spongebob cased comment on line 15
def spongebob_case(my_string):
    def _sponge_char(upper, char):
        if(upper):
            return char.upper()
        return char.lower()
    return ''.join([_sponge_char(i%2 == 0,char) for i, char in enumerate(my_string)])