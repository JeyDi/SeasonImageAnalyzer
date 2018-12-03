import os
import random
import shutil
import numpy as np
import cv2
from pathlib import Path
from tqdm import tqdm
from random import shuffle
from keras.preprocessing import image
from image_processing import processImage


main_keywords = ['summer','winter','autumn','spring']
main_dir_path = Path(__file__).resolve().parent.parent
split = 0.7

## 1 funzione:
#vai nella cartella corrispondente
#aggiungi il nome della label prima del numero: summer_id.jpg

#prendi la prima metà delle immagini (percentuale di split selezionabile)
#sposta la prima parte in: trainingset e ricalcola indici dopo la label: summer_newid.jpg
#sposta la seconda parte in: testset e ricalcola indici dopo la label: summer_newid.jpg

def clean_images(main_keywords,main_dir_path,split=0.7):
        
    training_path = os.path.join(main_dir_path, "trainingset")
    test_path = os.path.join(main_dir_path, "testset")
    print("\ntraining_path: " + str(training_path))
    print("\ntest_path: " + str(test_path))

    for i, item in enumerate(main_keywords):

        dir_path = os.path.join(main_dir_path,"download",item)
        filenames = os.listdir(dir_path)
        print("\ndir_path: " + str(dir_path))
        print("Number of files in the folder: ",len(filenames))
        if filenames : 

            for i, picture in enumerate(filenames):
                
                #Check if the files already updated
                if "_" not in picture: 
                    filename_without_ext = os.path.splitext(picture)[0]
                    extension = os.path.splitext(picture)[1]

                    new_file_name = str(item) + "_" + filename_without_ext
                    new_file_name_with_ext = new_file_name + extension

                    #print(new_file_name_with_ext)
                    os.rename(os.path.join(dir_path,picture), os.path.join(dir_path,new_file_name_with_ext))
                else:
                    continue
            
            #Re-get the new list of filenames
            filenames = os.listdir(dir_path)

            #Split the file to create the trainingset and the test set
            number_to_split = round(len(filenames) * (split*100) / 100)
            print("Number to split in ", item, " : ", number_to_split)
            #trainingset = range(0, len(main_keywords)-1, number_to_split)

            #Per ogni elemento di number_to_split
            #Genero un numero random da 0 a len(main_keywords)
            #Prendo l'elemento con quell'indice e lo sposto nella cartella di training
            
            #List of all files in the directory
            for i in range(0, number_to_split-1):

                filenames = os.listdir(dir_path)
                element = random.randint(0, len(filenames)-1)
                element_to_move = filenames[element]

                training_item_folder = os.path.join(training_path,item)
                training_file = os.path.join(training_path,item,element_to_move)

                #If the subfolder doesn't exist, create
                if not os.path.exists(training_item_folder):
                    os.makedirs(training_item_folder)
                
                if os.path.isfile(training_file):
                    print("File: " + str(training_file) + " already exist in the training set..")
                    continue
                else:
                    #Preprocess image and move
                    element_to_move_processed = processImage(os.path.join(dir_path,element_to_move))
                    if element_to_move_processed is not None:
                        shutil.move(element_to_move_processed, training_file)

            #Reload list of files remaining in the dataset subfolder
            remaining_filenames = os.listdir(dir_path)
            print("remaining files for testset: ", len(remaining_filenames))

            #Move this remaining file to the test set
            for f in remaining_filenames:
                
                test_item_folder = os.path.join(test_path,item)
                test_file = os.path.join(test_path,item,f)

                #If the subfolder doesn't exist, create
                if not os.path.exists(test_item_folder):
                    os.makedirs(test_item_folder)

                if os.path.isfile(test_file):
                    print("File: " + str(test_file) + " already exist in the test set..")
                    continue
                else:
                    #Preprocess image and move
                    element_to_move_processed = processImage(os.path.join(dir_path,f))
                    if element_to_move_processed is not None:
                        shutil.move(element_to_move_processed, test_file)

            print("Folder: ", item, " splitted")
        else:
            print("Folder is empty..")

    return(True)

#Alexa Davalos

## 2 funzione:
###RICALCOLO GLI INDICI PER TRAININGSET E TESTSET
def calculate_indexes(start_path,datasetname = "trainingset"):
    
    dir_path = os.path.join(start_path,datasetname)
    print("Calculate new indexes in: ", dir_path)
    filenames = os.listdir(dir_path)

    for i, item in enumerate(filenames):
        
        class_name = item.split('_')[0]
        extension = item.split('.')[1]
        new_name =  class_name + "_" + str(i) + "." + extension

        old_image = os.path.join(dir_path,item)
        new_image = os.path.join(dir_path,new_name)
        os.rename(old_image, new_image)
    
    print("Completed...")
    return True
        

## 3 funzione:
#genera un numpy array caricando le immagini in rgb
#salva il numpy array per gli esperimenti

#Create a label for an image
def create_label(keywords,image):

    for i, key in enumerate(keywords):
        
        label = image.split('_')[0]
        
        if key.lower() == label.lower():
            ohl = np.array([i])
    
    return(ohl)

#Create the dataset
def create_dataset(keywords,start_path,dataset_type="trainingset"):

    dataset = []

    dir_path = os.path.join(start_path, dataset_type)

    for i in tqdm(os.listdir(dir_path)):
        
        image_path = os.path.join(dir_path,i)
        
        #print("ImagePath: ",image_path)

        # Load image in color
        img = image.load_img(image_path)
        
        #Append the new image and label
        dataset.append([np.array(img),create_label(keywords,i)])

    dataset = np.array(dataset)
    #Save the numpy array to disk
    outfile = str(os.path.join(start_path,dataset_type)) + ".npy"
    np.save(outfile, dataset)
    print("Numpy array saved")
    return dataset


        



