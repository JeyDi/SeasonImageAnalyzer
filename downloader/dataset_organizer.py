import os
import random
import shutil
from pathlib import Path


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

        dir_path = os.path.join(main_dir_path,item)
        filenames = os.listdir(dir_path)
        print("\ndir_path: " + str(dir_path))

        if filenames : 

            for i, picture in enumerate(filenames):
                
                #Check if the files already updated
                if "_" not in picture: 
                    filename_without_ext = os.path.splitext(picture)[0]
                    extension = os.path.splitext(picture)[1]

                    new_file_name = str(item) + "_" + filename_without_ext
                    new_file_name_with_ext = new_file_name + extension

                    print(new_file_name_with_ext)
                    os.rename(os.path.join(dir_path,picture), os.path.join(dir_path,new_file_name_with_ext))
                else:
                    continue
            
            #Re-get the new list of filenames
            filenames = os.listdir(dir_path)

            #Split the file to create the trainingset and the test set
            number_to_split = round(len(filenames) * (split*100) / 100)
            print(number_to_split)
            trainingset = range(0, len(main_keywords), number_to_split)

            #Per ogni elemento di number_to_split
            #Genero un numero random da 0 a len(main_keywords)
            #Prendo l'elemento con quell'indice e lo sposto nella cartella di training
            
            #List of all files in the directory
            for i in range(0, number_to_split):

                filenames = os.listdir(dir_path)
                element = random.randint(0, len(filenames))
                element_to_move = filenames[element]
                training_file = os.path.join(training_path,element_to_move)

                if os.path.isfile(training_file):
                    print("File: " + str(training_file) + " already exist in the training set..")
                    continue
                else:
                    shutil.move(os.path.join(dir_path,element_to_move), training_file)

            #Reload list of files remaining in the dataset subfolder
            remaining_filenames = os.listdir(dir_path)

            #Move this remaining file to the test set
            for f in remaining_filenames:

                test_file = os.path.join(test_path,f)

                if os.path.isfile(test_file):
                    print("File: " + str(test_file) + " already exist in the test set..")
                    continue
                else:
                    shutil.move(os.path.join(dir_path,f), test_file)

        else:
            print("Folder is empty..")

    return(True)


## 2 funzione:
###RICALCOLO GLI INDICI PER TRAININGSET E TESTSET
    

## 3 funzione:
#genera un numpy array caricando le immagini in rgb
#salva il numpy array per gli esperimenti





