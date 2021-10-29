from scrape.module import *
from scrape.unit import *
import os

hierarchy = units_from_file('sample_files/test_home.html')
for unit, modules in hierarchy.items():
    # mkdir for the unit
    for module_name, module_link in modules.items():
        # mkdir for each module using module_name
        # for each page in module
        # define save path
        module_pages = pages_from_file(module_link, path)
        for page in module_pages:
            # save file
            print(page)

# pages_from_url('https://auth.galvanize.com/sign_in')    
