import fastbook
fastbook.setup_book()

from fastbook import *

from fastai.vision.all import *
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

root_path = './img'

def download_img(term, count, dpath):
    urls = search_images_ddg(term, max_images=count)
    download_images(dpath, None, urls, max_pics=count)

def clean (dir):
    cleaned_files = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with Image.open(file_path) as image:
                    if ((image.format != 'JPEG') and (image.format != 'PNG') and (image.format != 'GIF')):
                        print("Filename: ", file_path, " Format: ", image.format)
                        os.remove(file_path)
                    else:
                        cleaned_files.append(file_path)
            except Exception as e:
                print(f"Error while processing {file_path}: {str(e)}")
                os.remove(file_path)
    return cleaned_files

search = input("Enter search term: ")
amount = int(input("Enter number of images to download: "))
tot_path = os.path.join(root_path, search.replace(" ", "_"))
os.makedirs(tot_path, exist_ok=True)

download_img(search, amount, tot_path)
cleaned_files = clean(tot_path)
print(f"Downloaded {len(cleaned_files)} files.")



#fish = DataBlock(blocks = (ImageBlock, CategoryBlock),
           #      get_items=get_image_files, 
           #      get_y=parent_label,
           #      splitter=RandomSplitter(valid_pct=0.2, seed=42),
           #      item_tfms=Resize(224))

#dataload = fish.dataloaders(root_path + cur_path)
