import os
from pathlib import Path
from google_downloader import image_downloader
from dataset_organizer import clean_images

#Global variable for a specific task
KEYWORDS = ['summer','winter','autumn','spring']
MAXIMAGES = 200
DIR_PATH = Path(__file__).resolve().parent.parent
ROOTDIR = "dataset"
DATASET_PATH = os.path.join(DIR_PATH,ROOTDIR)


#Call Image Downloader
image_downloader(KEYWORDS,DATASET_PATH,MAXIMAGES)

#Clean Images
clean_images(KEYWORDS,DATASET_PATH,0.7)



