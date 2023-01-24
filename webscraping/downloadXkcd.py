'''
1) get xkcd homepage
2) download comic
3) go to previous page
4) repeat 2 and 3 till it gets to first page
5) optionally take a number of pages to download
'''
from sys import exit
from pathlib import Path
from argparse import ArgumentParser
from logging import debug, DEBUG, CRITICAL, basicConfig, disable
try:
    from bs4 import BeautifulSoup
except ImportError:
    exit('This program requires the bs4 module to run.')
try:
    from requests import get
except ImportError:
    exit('This program requires the requests module to run.')
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def main():
    print('Download xkcd')
    download_dir = Path('.').absolute() / 'xkcd'
    download_dir.mkdir(parents=True, exist_ok=True)

    # args = parse_args()
    args = {'num': 1}
    num_of_pages = args['num']
    link = ''
    while True:
        res = get('https://xkcd.com/{}'.format(link))
        soup_object = BeautifulSoup(res.text, 'html.parser')
        img_link = soup_object.select('#comic > img')[0].get('src')
        debug(img_link)
        img = get('https:{}'.format(img_link))
        save_img(img, download_dir)

        link = soup_object.select('ul.comicNav a[rel="prev"]')[0].get('href')
        debug(link)

        num_of_pages -= 1
        if num_of_pages == 0 or link == '#':
            break



if __name__ == '__main__':
    main()
