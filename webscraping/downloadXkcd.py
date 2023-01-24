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

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--num-of-pages', required=False)

    args = parser.parse_args()
    num_of_pages = args.num_of_pages
    if num_of_pages == None:
        num_of_pages = -1
    return {'num': num_of_pages}

def download_save_img(download_dir, img_link):
    img = get('https:{}'.format(img_link), stream=True)
    img_name = img_link.split('/')[-1]
    print('Downloading {}'.format(img_name))
    with (download_dir / img_name).open('wb') as file:
        for chunk in img.iter_content(100_000):
            file.write(chunk)

def main():
    print('Download xkcd')
    download_dir = Path('.').absolute() / 'xkcd'
    download_dir.mkdir(parents=True, exist_ok=True)

    args = parse_args()
    num_of_pages = args['num']
    link = ''
    while True:
        res = get('https://xkcd.com/{}'.format(link))
        soup_object = BeautifulSoup(res.text, 'html.parser')
        img_link = soup_object.select('#comic > img')[0].get('src')

        debug(img_link)
        download_save_img(download_dir, img_link)

        link = soup_object.select('ul.comicNav a[rel="prev"]')[0].get('href')
        debug(link)

        num_of_pages -= 1
        if num_of_pages == 0 or link == '#':
            break



if __name__ == '__main__':
    main()
