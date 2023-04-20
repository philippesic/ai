
import fastbook
fastbook.setup_book()

from fastbook import *

from fastai.vision.all import *
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def download_img(path, term, count):
    dpath = Path(path)
    dest = dpath
    dest.mkdir(parents=True, exist_ok=True)
    urls = search_images_ddg(term, max_images=count)
    download_images(dest, None, urls, 200)


def clean (dir, files_array):
  for filename in files_array:
    file_path = dir + '/' + filename
    image = Image.open(file_path)
    if ((image.format != 'JPEG') and (image.format != 'PNG') and (image.format != 'GIF')):
      print("Filename: ", image.filename, " Format: ", image.format)
      image.close()
      os.remove(file_path)
    else:
      image.close()








