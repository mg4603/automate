'''
1) take category as cmdline arg or from clipboard
2) take destination folder
3) search for images
4) download images that match category
'''
from argparse import ArgumentParser
from pathlib import Path
from logging import debug, DEBUG, CRITICAL, disable, basicConfig
try:
    from bs4 import BeautifulSoup
except ImportError:
    exit('This program requires the bs4 module.')
try:
    from requests import get
except ImportError:
    exit('This program requires the requests module.')
try:
    from pyperclip import paste
except ImportError:
    exit('This program requires the pyperclip module.')

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
disable(CRITICAL)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--category', required=False)
    category = parser.parse_args().category
    if category == None:
        if paste() == '':
            exit('No search category given.')
        category = paste()
    return {'category': category}

def get_save_img(destination_path, img_link):
    img_name = img_link.split('/')[-1]
    print('Downloading{}...'.format(img_name))
    img = get('https:{}'.format(img_link), stream=True)
    with (destination_path / img_name).open('wb') as file:
        for chunk in img.iter_content(100_000):
            file.write(chunk)

def main():
    print('Flickr Images Downloader')
    args = parse_args()

    print('Enter destination file path:')
    destination_name = input('> ')

    destination_path = Path(destination_name).absolute() / '{}_imgs'.format(
        args['category']
    )
    destination_path.mkdir(exist_ok=True, parents=True)

    print('Starting downloads')
    res = get('https://www.flickr.com/search/?text={}'.format(
        args['category']
    ))

    soup_object = BeautifulSoup(res.text)
    links = soup_object.select('.search-photos-results img')
    debug('\n'.join(map(str, links)))

    for link in links:
        debug(link.get('src'))
        get_save_img(destination_path, link.get('src'))

    print('Done')

if __name__ == '__main__':
    main()