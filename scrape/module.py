import os
import requests
from bs4 import BeautifulSoup

def parse_html(html):
    '''
    input: url or file to parse for modules links
    return: page's links
    '''
    soup = BeautifulSoup(html, "html.parser")
    links = [result['href'] for result in soup.findAll('a', attrs = {'class': 'lesson'})]
    return links

def pdf_from_url(url):   
    '''
    input: url from module
    return: page's links
    ''' 
    module_info = requests.get(url).content
    return parse_html(module_info)    

def pdf_from_file(file):
    '''
    input: file handle from module
    return: page's links
    ''' 
    with open(file, 'r') as f:
        contents = f.read()
    return parse_html(contents)