
import os
from icrawler.builtin import GoogleImageCrawler


def image_downloader(keyworkds=[],dir_path="dataset",maximages=100):
    
    for i, item in enumerate(keyworkds):

        dir_path_keyword = os.path.join(dir_path,item)

        #If the directory not exist, create
        if not os.path.exists(dir_path_keyword):
            os.makedirs(dir_path_keyword)
        
        print('\n\tWriting on directory: ' + str(dir_path_keyword))
        print('\tThe images for keyword: ' + str(item) + '\n')

        google_crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': dir_path_keyword})
        filters = dict(
            type='photo'
            # size='large',
            # color='orange',
            # license='commercial,modify',
            # date=((2017, 1, 1), (2017, 11, 30))
            )
        google_crawler.crawl(keyword=item, filters=filters, max_num=maximages, file_idx_offset=0)

    return(True)