#-------------------------------------------------------------------------------------
import glob
import os
from pathlib import Path

def ClearDir(path='./', safe_del=True):
    '''brief:
            Removes all files from a directory.
        params (see default values for examples):
            path - The source directory of the images to turn into a gif. 
                   Must include preceding ./, should not include ending /
        example call:
            ClearDir('./kmeans/images')'''
    choice=''
    if(safe_del):
        print("Delete files from " + path + " y/n?")
        choice = input()
    if(safe_del == False or str(choice) == 'y'):
        files = glob.glob(path + '/*')
        for f in files:
            os.remove(f)

#-------------------------------------------------------------------------------------
import time
from IPython.display import Audio, display
def play_sound(self, etype, value, tb, tb_offset=None):
    display(Audio(url='https://www.redringtones.com/wp-content/uploads/2016/09/R2D2-scream.mp3', autoplay=True))
    time.sleep(0.25)
    self.showtraceback((etype, value, tb), tb_offset=tb_offset)
def ActivateCellFailSound():
    '''brief:
            Plays a ding if the cell execution fails. Only works for Jupyter Notebook.
        example call:
            CellFailChime()'''
    get_ipython().set_custom_exc((Exception,), play_sound)

#-------------------------------------------------------------------------------------
from IPython.display import Audio, display
class VarPrinter:
     def __init__(self, ip, url):
         self.ip = ip
         self.url_ = url
     def post_run_cell(self, result):
        if result.error_in_exec != None:
            print('womp womp')
        else:
            display(Audio(url=self.url_, autoplay=True))
            time.sleep(0.5)
def load_ipython_extension(ip, url):
    vp = VarPrinter(ip, url)
    ip.events.register("post_run_cell", vp.post_run_cell)

def ActivateCellDoneSound(url='http://soundfxcenter.com/movies/star-wars/8d82b5_Star_Wars_R2-D2_Excited_Sound_Effect.mp3'):
    '''brief:
          Plays a ding when a cell is complete. Kind of buggy with a failed cell.
        example call:
            CellDoneChime()'''
    load_ipython_extension(get_ipython(),url)

#-------------------------------------------------------------------------------------
from IPython.core.display import display, HTML
def FitCellsToWindow():
  '''
  Fits Jupyter cells to window size.

  Example Call:
      FitCellsToWindow()'''
  display(HTML("<style>.container { width:100% !important; }</style>"))

#-------------------------------------------------------------------------------------
def ColoredText(r, g, b, text):
    """
    Displays colored text in the console.
    
    Parameters:
        r    - Value from 0-255 for Red
        g    - Value from 0-255 for Green
        b    - Value from 0-255 for Blue
        text - Text to display with color
    
    Returns:
      Modified text string, now with the given color.

    Example Call:
      print(ColoredText(255, 0, 0, 'Hello World'))
    """
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)