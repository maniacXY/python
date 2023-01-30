from csvtopdf.csv_reader import CSV_Reader
from pprint import pprint
reader = CSV_Reader()


#output = reader.readFile("220814_33_Berichtsheft.txt")
#pprint(output)
#reader.readFile()
#reader.readFolder()

#reader.namingReportHeader("220814_33_Berichtsheft.txt")


reader.readFolder()