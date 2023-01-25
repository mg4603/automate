'''
1) get url from clipboard or as argument
2) get links on page
3) download every downloadable page and print broken links
'''
from sys import exit
from argparse import ArgumentParser
from pathlib import Path
from re import sub
from urllib.parse import urlparse
from logging import debug, DEBUG, CRITICAL, disable, basicConfig
try:
    from bs4 import BeautifulSoup
except ImportError:
    exit('This program requires the bs4 module to run.')
try:
    from pyperclip import paste
except ImportError:
    exit('This program requires the pyperclip module to run.')
try:
    from requests import get
except ImportError:
    exit('This program requires the requests module to run.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-u', '--url', required=False)
    url = parser.parse_args().url
    if url == None:
        if paste() == '':
            exit('Url required, either as argument or saved to clipboard')
        url = paste()
    return {'url': url}

def download_page(download_path, link):
    url_obj = urlparse(link)
    if url_obj.params != '' and url_obj.query != '':
        params = '&'.join([url_obj.params, url_obj.query])
    elif url_obj.params != '':
        params = url_obj.params
    elif url_obj.query != '':
        params = url_obj.query
    else:
        params = ''

    link = 'https://{}{}?{}'.format(
        url_obj.netloc, url_obj.path,
        params
    )
    debug(link)
    page_name = url_obj.path[1:]

    try:
        res = get(link)
        res.raise_for_status()
    except:
        return False

    page_name = sub(r'/', r'_', page_name)
    if page_name.endswith('_'):
        page_name = page_name[:-1]
    debug(page_name)
    if page_name == '':
        page_name = 'index'
    with (download_path / page_name).open('wb') as file:
        for chunk in res.iter_content(100_000):
            file.write(chunk)
    return True




if __name__ == '__main__':
    main()