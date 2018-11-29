import os
from pathlib import Path
import google_downloader
import dataset_organizer

KEYWORDS = ['summer','winter','autumn','spring']
MAXIMAGES = 200
DIR_PATH = Path(__file__).resolve().parent.parent
ROOTDIR = "dataset"

directory = os.path.join(DIR_PATH,ROOTDIR)

