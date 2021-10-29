# get each unit in unit.py
# use unit title as folder

# get each module 
# use module name as subfolder
# export files as pdf 

from scrape.module import *
from scrape.unit import *
import os

print(units_from_file('sample_files/test_home.html'))
# loop through units
    # mkdir for the unit
    # get links to modules 
    # mkdir for each module
    # for each page in module
        # save file

#pdf_from_url('https://auth.galvanize.com/sign_in')    
# pdf_from_file('sample_files/test_page.html')
# module_files('https://learn-2.galvanize.com/cohorts/2836/blocks/1310/content_files/update-and-delete/update-and-delete.md')
