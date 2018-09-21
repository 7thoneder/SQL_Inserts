import sqlite3
import shutil
import os
import subprocess
import tkinter as tk
from tkinter import filedialog
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
from my_module import move_file, web_test

root = tk.Tk()
root.withdraw()

connection = sqlite3.connect("voodoo.db")
cursor = connection.cursor()

drop_table = """Drop Table businessrulez;"""
cursor.execute(drop_table)
create_table = """Create Table businessrulez(OfferCode varchar(100), ProviderID varchar(5));"""
cursor.execute(create_table)

#Here you are asked for the csv file with the drivers for your insert statements and insert statements are created
csv_file_loc = filedialog.askopenfilename()
with open(csv_file_loc, 'r') as fz:
  reader = csv.reader(fz)
  your_list = list(reader)
filename = input('SQL Filename?:')
f = open(filename + '.txt','a')
for p in your_list:
    format_str = """INSERT INTO businessrulez (OfferCode, ProviderID)
    VALUES ("{OfferCode}", "{ProviderID}");\n"""

    sql_command = format_str.format(OfferCode=p[0], ProviderID=p[1])
    cursor.execute(sql_command)
    f.write(sql_command)
connection.commit()
connection.close()
f.close()

#Here you will be asked for the folder where you want to save the insert statements file for your records
move_file(filename)

#Gets you the TransID of the qual
web_test()

print('Done!')