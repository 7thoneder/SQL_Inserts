import os
import subprocess
import csv

csv_file_loc = 'offercodes.csv'
with open(csv_file_loc, 'r') as fz:
  reader = csv.reader(fz)
  your_list = list(reader)
filename = 'PSO134'
f = open(filename + '.txt','a')
for p in your_list:
    format_str = """INSERT INTO businessrulez (OfferCode, ProviderID)
    VALUES ("{OfferCode}", "{ProviderID}");\n"""

    sql_command = format_str.format(OfferCode=p[0], ProviderID=p[1])
    f.write(sql_command)

f.close()

print('Done!')