import os
from icrawler.builtin import GoogleImageCrawler



def google_downloader(keywords,dir_path,maximages=100):
        
    for i, item in enumerate(keywords):

        dir_path = os.path.join(dir_path,item)
        print('\n\tWriting on directory: ' + str(dir_path))
        print('\tThe images for keyword: ' + str(item) + '\n')

        google_crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': dir_path})
        filters = dict(
            type='photo'
            # size='large',
            # color='orange',
            # license='commercial,modify',
            # date=((2017, 1, 1), (2017, 11, 30))
            )
        google_crawler.crawl(keyword=item, filters=filters, max_num=maximages, file_idx_offset=0)
