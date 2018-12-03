from PIL import Image
from glob import glob
import PIL
import sys
import os


def image_save(path,image,type='jpg'):

    name = path.split('.')
    result_name = name[0] + '.' + type
    print(result_name)

    if os.path.exists(path):
        os.remove(path)
    else:
        print('File not found..')

    image.save(result_name)

    return result_name 


def compress_image(path_originals,path,image, infile):
    size = 1920, 1080
    width = 1920
    height = 1080
    listing = os.listdir(path_originals)

    name = infile.split('.')
    first_name = path+'/'+name[0] + '.jpg'
    if image.size[0] > width and image.size[1] > height:
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(first_name, quality=85)
    elif image.size[0] > width:
        wpercent = (width/float(image.size[0]))
        height = int((float(image.size[1])*float(wpercent)))
        image = image.resize((width,height), PIL.Image.ANTIALIAS)
        image.save(first_name,quality=85)
    elif image.size[1] > height:
        wpercent = (height/float(image.size[1]))
        width = int((float(image.size[0])*float(wpercent)))
        image = image.resize((width,height), PIL.Image.ANTIALIAS)
        image.save(first_name, quality=85)
    else:
        image.save(first_name, quality=85)


def processImage(img_path,convert_type='jpg'):
   
    img = Image.open(img_path)
    print(img)

    if img.format == "JPEG":
        image = img.convert('RGB')
        result_name = image_save(img_path,image,convert_type.lower())
        img.close()
        
    elif img.format == "GIF":
        #image = img.convert("RGB")
        # bg = Image.new("RGB", i.size)
        img.close()
        os.remove(img_path)
        result_name = None
        # image = Image.composite(i, bg, i)
        # result_name = image_save(img_path,image,convert_type.lower())
        
    elif img.format == "PNG":
        try:
            image = Image.new("RGB", img.size, (255,255,255))
            image.paste(img,img)
            result_name = image_save(img_path,image,convert_type.lower())
        except ValueError:
            image = img.convert('RGB')
            result_name = image_save(img_path,image,convert_type.lower())
        img.close()
        
    elif img.format == "BMP":
        image = img.convert('RGB')
        result_name = image_save(img_path,image,convert_type.lower())
        img.close()
        
    else:
        result_name = img_path
        img.close()

    
    return result_name


def processImage_folder(dir_path):
    listing = os.listdir(dir_path)

    for infile in listing:
        file_path = os.path.join(dir_path,infile)
        result_path = processImage(file_path)
        
    return True