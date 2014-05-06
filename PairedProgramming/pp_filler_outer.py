#!/usr/bin/env python2
# Requires fdfgen, which can be installed from pip
# This is my lazy requirements.txt

# Also requires the pdftk utility, a generic awesome PDF utility
from fdfgen import forge_fdf
import csv
import os

fields = []
reader = csv.reader(open('pp_data.csv'), delimiter=',', quotechar='"')
for row in reader:
	fields.append((row[0], row[1]))

fdf = forge_fdf("",fields,[],[],[])
fdf_file = open("data.fdf","w")
fdf_file.write(fdf)
fdf_file.close()

os.system("pdftk pp_generic.pdf fill_form data.fdf output output.pdf flatten")
