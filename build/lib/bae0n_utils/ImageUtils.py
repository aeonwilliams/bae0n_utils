from pathlib import Path
import os
import glob
from PIL import Image, ImageDraw

def MakeGif(source_dir='./', out_dir='./', gif_name='test', duration=100, file_type='jpg'):
    '''brief:
            Turns a directory of images into a gif.
        params (see default values for examples):
            source_dir - The source directory of the images to turn into a gif. Must include preceding ./
            out_dir    - The directory to save the gif to. Must include preceding ./
            gif_name   - The name of the gif. Do not include filetype.
            duration   - Number of frames in the gif...I think.
            file_type  - File extension for the images. Do not include preceding .
        example call:
            MakeGif('./data', './', 'test', 100, 'jpg')'''
    images = []
    
    paths = sorted(Path(source_dir).iterdir(), key=os.path.getmtime)
    
    for file in paths:
        if str(file).endswith('.' + file_type):
            images.append(Image.open(file))

    if(len(images) > 0):
        images[0].save(out_dir + '/' + gif_name + '.gif', save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)