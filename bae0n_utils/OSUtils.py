import glob
import os
from pathlib import Path

###################################################################################################
# brief:
    # Removes all files from a directory.
# params (see default values for examples):
    # path - The source directory of the images to turn into a gif. 
    #        Must include preceding ./, should not include ending /
# example call:
    # ClearDir('./kmeans/images')
###################################################################################################
def ClearDir(path='./'):
    '''brief:
            Removes all files from a directory.
        params (see default values for examples):
            path - The source directory of the images to turn into a gif. 
                   Must include preceding ./, should not include ending /
        example call:
            ClearDir('./kmeans/images')'''
    print("Delete files from " + path + " y/n?")
    if(input() == 'y'):
        files = glob.glob(path + '/*')
        for f in files:
            os.remove(f)