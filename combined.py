import fastbook
fastbook.setup_book()
# Part 1: Importing fastbook module
from fastbook import *
# Part 2: Importing os and ImageFile modules and setting the LOAD_TRUNCATED_IMAGES option
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# main code
def custom_download_images(category, num_images, folder): 
  # this function receives image category name, 
  # number of images you want to download and 
  # name of the folder to download pictures into
  #Write code!
  pathname = (folder)
  #print (pathname)
  path = Path(pathname)
  #print(path) #added for debugging
  newdest = path
  #print(newdest) #added for debugging
  newdest.mkdir(parents=True, exist_ok=True) 
  newurls = search_images_ddg(category, max_images=num_images)
  #print(newurls)
  download_images(newdest, None, newurls, num_images)
  return

# the function below check file types and removes those that are not JPEGs
def checkTypes (dir, files_array):
  for filename in files_array:
    file_path = dir + '/' + filename
    image = Image.open(file_path)
    if ((image.format != 'JPEG') and (image.format != 'PNG') and (image.format != 'GIF')):
      print("Filename: ", image.filename, " Format: ", image.format)
      image.close()
      os.remove(file_path)
    else:
      image.close()   # close image file
  return 

#this is input data
rootdrive = 'gdrive/My Drive/images/' #define the root directory where folders will be created
terms = ['eagles','black','brown','bald'] #first item is main category, then all the variations you want to search for
num_images = 10
# black eagles, brown eagles, bald eagles
# black bear, brown bear, or teddy bear.

#from assignment 2 creating lists of terms labels for the directories based on the terms
#Fill in the lists!
termslen=len(terms)
#print("terms")
print("terms input array=",terms)
print("array size",termslen)
print("num_images",num_images)
labels=[""] * termslen
print("labels array=",labels)
i=0
labels[i]=rootdrive + terms[i]
print("i=",i)
print("label[i]=",labels[i])
i+=1

while i < termslen:
  print("i=",i)
  category=terms[i] + " " + terms[0]
  labels[i] = labels[0] + "/"+ category
  #print(labels[i])
  folder=labels[i]

  print("category=",category)

  print ("folderpath",folder)

  custom_download_images(category,num_images,folder)

  # I will add clean up code to this session
  print('total training images in folder',folder, len(os.listdir(folder)))
  filestoclean = os.listdir(folder)
  checkTypes(folder, filestoclean)
  print('new total training images in folder',folder, len(os.listdir(folder)))
  #

  i+= 1