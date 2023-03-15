from pathlib import Path
from requests import get
from bs4 import BeautifulSoup
from threading import Thread
from logging import debug, basicConfig, disable, CRITICAL, DEBUG
from os.path import basename

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def download(download_path, start_num, end_num):
    
    for i in range(start_num, end_num + 1):
        print('Downloading https://xkcd.com/%s...' % i)
        res = get('https://xkcd.com/%s' % i)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')
        debug(soup.select('#comic img')[0].get('src'))

        img_url = 'https:' + soup.select('#comic img')[0].get('src')
        debug(basename(img_url))
        
        img_res = get(img_url)
        img_res.raise_for_status()

        with (download_path / basename(img_url)).open('wb') as img_file:
            for chunk in img_res.iter_content(100_000):
                img_file.write(chunk)


def main():
    downloads_path = Path('downloads')
    downloads_path.mkdir(exist_ok=True, parents=True)
    
    res = get('https://xkcd.com/')
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    debug(soup.select('.comicNav a[rel=prev]')[0].get('href'))
    number_of_comics = int(soup.select('.comicNav a[rel=prev]')[0].get('href')[1:-1])
    debug(number_of_comics)

    download_threads = []
    for i in range(1, number_of_comics + 1, 10):
        download_thread = Thread(target=download, args=[downloads_path, i, i + 9])
        download_threads.append(download_thread)
        download_thread.start()
       


if __name__ == '__main__':
    main()    