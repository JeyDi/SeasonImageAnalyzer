import os
from pathlib import Path


KEYWORDS = ['summer','winter','autumn','spring']
DIR_PATH = Path(__file__).resolve().parent.parent
SPLIT = 0.5

## 1 funzione:
#vai nella cartella corrispondente
#aggiungi il nome della label prima del numero: summer_id.jpg

#prendi la prima metà delle immagini (percentuale di split selezionabile)
#sposta la prima parte in: trainingset e ricalcola indici dopo la label: summer_newid.jpg
#sposta la seconda parte in: testset e ricalcola indici dopo la label: summer_newid.jpg

for i, item in enumerate(KEYWORDS):

    dir_path = os.path.join(DIR_PATH,"dataset",item)
    filenames = os.listdir(dir_path)

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
    
    #Split the file to create the trainingset and the test set
    number_to_split = round(len(KEYWORDS) * (SPLIT*100) / 100)
    trainingset = range(0, len(KEYWORDS), number_to_split)
    print(trainingset)

    #Per ogni elemento in 


## 2 funzione:
#genera un numpy array caricando le immagini in rgb
#salva il numpy array per gli esperimenti





