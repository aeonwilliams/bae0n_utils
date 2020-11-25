# bae0n_utils

Collection of utility functions to be used in Python. 

### FitCellsToWindow
#### ex: FitCellsToWindow()
Fits Jupyter cells to window size.

### ActivateCellDoneSound
#### ex: ActivateCellDoneSound(url='https://bigsoundbank.com/UPLOAD/mp3/0116.mp3')
Plays a sound effect when a cell is complete. Currently kind of buggy with a failed cell.

params:
- url (optional) - url of the sound you want to play. Accepts .wav and .mp3

### ActivateCellFailSound
#### ex: ActivateCellFailSound()
Plays a sound effect if the cell execution fails.

### ClearDir
#### ex: ClearDir('./images')
Removes all files from a directory.
    
params:
- path - The source directory of the images to turn into a gif. Must include preceding ./, should not include ending /

### MakeGif
#### ex: MakeGif('./data', './', 'test', 100, 'jpg')
Turns a directory of images into a gif.
    
params:
- source_dir - The source directory of the images to turn into a gif. Must include preceding ./
- out_dir    - The directory to save the gif to. Must include preceding ./
- gif_name   - The name of the gif. Do not include filetype.
- duration   - Number of frames in the gif...I think.
- file_type  - File extension for the images. Do not include preceding .

### CorrMatrixAnalysis
Displays in depth analysis of the correlation between features. Currently only addresses correlation of dependent feature to independent features, but will be updated soon.

params:
- df          - The dataframe to analyze.
- dep_feature - The dependent feature.

#### example call:
df = pd.read_csv('Iris.csv')

CorrMatrixAnalysis(df, 'species')
<details>
  <summary>Example output</summary>
  
  Features With High Correlation to diagnosis:
    -0.79  - concave points_worst
    -0.78  - perimeter_worst
    -0.78  - concave points_mean
    -0.78  - radius_worst
    -0.74  - perimeter_mean
    -0.73  - area_worst
    -0.73  - radius_mean
    -0.71  - area_mean
    
    Features With Moderate Correlation to diagnosis:
    -0.70  - concavity_mean
    -0.66  - concavity_worst
    -0.60  - compactness_mean
    -0.59  - compactness_worst
    -0.57  - radius_se
    -0.56  - perimeter_se
    -0.55  - area_se

    Features With No Correlation to diagnosis:
    -0.29  - compactness_se
    -0.25  - concavity_se
    -0.08  - fractal_dimension_se
     0.07  - smoothness_se
    -0.04  - id
     0.01  - fractal_dimension_mean
     0.01  - texture_se
     0.01  - symmetry_se
</details>

Many thanks to my muse for the constant inspiration, great ideas, and support <3