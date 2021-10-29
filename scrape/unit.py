# get links from entire unit

# standard-card-heading
import os
import requests
from bs4 import BeautifulSoup

def parse_html(html):
    '''
    input: url or file to parse for modules links
    return: module's links
    '''
    soup = BeautifulSoup(html, "html.parser")
    unit_info = {}
    module_info = {}
    for unit in soup.findAll('div', attrs = {'class': 'block-container'}):
        unit_name = unit['id']
        modules = unit.findAll('a', attrs = {'class': 'standard-card'})
        for module in modules:
            page = module.find('div', attrs = {'class': 'standard-card-heading'})['title']
            module_info[page] = module['href']
            unit_info[unit_name] = module_info
    return unit_info
    # return 

    # {
    # "unit name": {"module name" : link }    
    # }

def units_from_url(url):   
    '''
    input: home page url
    return: module's links
    ''' 
    module_info = requests.get(url).content
    return parse_html(module_info)     

def units_from_file(file):
    '''
    input: file handle from module
    return: module's links
    ''' 
    with open(file, 'r') as f:
        contents = f.read()
    return parse_html(contents)

print(units_from_file('sample_files/test_home.html'))
