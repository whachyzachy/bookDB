from isbnlib import *
import sys
import csv

isbns = []

with open('/home/jgibbs/PycharmProjects/isbn_organizer/history-1494170264404.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        try:
            #print(row[0])
            #print(meta(row[0]))
            isbns.append(row[0])
        except NotValidISBNError:
            print("Not valid isbn error")


setIsbns = set(isbns)
print(setIsbns)
#print(isbns)

with open('/home/jgibbs/PycharmProjects/isbn_organizer/python_output.csv', 'w', newline='') as csvfile:
    outwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
    for val in setIsbns:
        try:
            themeta = meta(val)

            #print(themeta)
            authorstring = ' AND '.join(map(str, themeta["Authors"]))

            #print( authorstring + "," +  themeta["Title"] + ", , , " + themeta["ISBN-13"])

            temp = [authorstring,themeta["Title"],"","","",themeta["ISBN-13"]]
            print(temp)
            outwriter.writerow(temp)
        except:
            themeta = {}


val = meta('9781465456335')
print(val)
print(isbn_from_words('Inside Out Junior'))