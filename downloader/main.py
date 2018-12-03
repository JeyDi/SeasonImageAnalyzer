import os
from pathlib import Path
from google_downloader import image_downloader
from dataset_organizer import clean_images, create_label, create_dataset, calculate_indexes
from image_processing import processImage, processImage_folder

#Global variable for a specific task
KEYWORDS = ['summer','winter','autumn','spring']
MAXIMAGES = 200

DIR_PATH = Path(__file__).resolve().parent.parent
DOWNLOAD_PATH = os.path.join(DIR_PATH,"dataset","download")
DATASET_PATH = os.path.join(DIR_PATH,"dataset")

#Call Image Downloader
print("\n\t--- DOWNLOAD IMAGES ---")
#image_downloader(KEYWORDS,DOWNLOAD_PATH,MAXIMAGES)

#Clean Images
print("\n\t--- CLEAN IMAGES ---\n")
clean_images(KEYWORDS,DATASET_PATH,0.7)

print('\nProcess image folder')
#path_to_remove = os.path.join(DATASET_PATH,'trainingset','summer')
#processImage_folder(path_to_remove)

#Calculate New Index
print("\n\t--- CALCULATE NEW INDEX ---\n")
# calculate_indexes(DATASET_PATH,"trainingset")
# calculate_indexes(DATASET_PATH,"testset")

#Create the new dataset
print("\n\t--- CREATE NEW NUMPY DATASETS ---\n")
#trainingset = create_dataset(KEYWORDS,DATASET_PATH, "trainingset")
# testset = create_dataset(KEYWORDS,DATASET_PATH, "testset")

#train_datagen = ImageDataGenerator(rescale=1./255)
