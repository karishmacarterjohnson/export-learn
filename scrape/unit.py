import os
import requests
from bs4 import BeautifulSoup

def parse_html(html):
    '''
    input: home page info
    return: dict with unit title, module title, and link to module
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

def units_from_url(url):   
    '''
    input: home page url
    return: dictionary of all units
    ''' 
    module_info = requests.get(url).content
    return parse_html(module_info)     

def units_from_file(file):
    '''
    input: home page file
    return: dictionary of all units
    ''' 
    with open(file, 'r') as f:
        contents = f.read()
    return parse_html(contents)