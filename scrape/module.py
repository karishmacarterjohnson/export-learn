import os
import requests
from bs4 import BeautifulSoup
import pdfkit

def parse_html(html):
    '''
    input: url or file to parse for modules links
    return: page's links
    '''
    soup = BeautifulSoup(html, "html.parser")
    return soup.findAll('a', attrs = {'class': 'lesson'})

def pages_from_url(url, path):   
    '''
    input: url from module
    return: page's links
    ''' 
    module_info = requests.get(url).content
    return parse_html(module_info)    

def pages_from_file(file, path):
    '''
    input: file handle from module
    return: page's links
    ''' 
    with open(file, 'r') as f:
        contents = f.read()
   
    for page in parse_html(contents):
        # print(page['title'],page['href'])
        '''
        page_title = page['title']
        pdfkit.from_url(page['href'], 'out.pdf')
        '''