import sqlite3
import shutil
import os
import subprocess
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Here you are asked for the csv file with the drivers for your insert statements and insert statements are created
csv_file_loc = 'offercodes.csv'
with open(csv_file_loc, 'r') as fz:
  reader = csv.reader(fz)
  your_list = list(reader)
filename = 'SQL'
f = open(filename + '.txt','a')
for p in your_list:
    format_str = """INSERT INTO businessrulez (OfferCode, ProviderID)
    VALUES ("{OfferCode}", "{ProviderID}");\n"""

    sql_command = format_str.format(OfferCode=p[0], ProviderID=p[1])
    f.write(sql_command)

f.close()

print('Done!')