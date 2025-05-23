# Analytical Image Differencing (AID)


## Introduction
- This code is used for the analysis of quantitative phase images (QPI) by the Analytical Image Differencing (AID)
  method, which is described in a [paper]([https://doi.org/10.1016/j.cmpb.2025.108829). It is important to analyze cell by cell. Therefore, it is necessary 
  to have a series of images containing only one cell.

## run.py
1. Select path to data. Only *.tiff file are accepted. 
```
path = r"C:......"
```
2. Set threshold for selection of cell from the background.
```
trashold = 0
```
3. Choose whether the exported AID images should be quantitative. Only for images! Not for generated raw data.
```
quantitative = False # False or True 
```
4. Set step between source images for AID.
```
step = 1 
``` 
5. Time step between source images in original data series (in seconds).
```
time_step = 30 
```
6. Select type of AID. If 'two' - AID images consist from two colors (in shades of red and green coded areas for decrement and increment of the cell mass). 
If 'four' - AID images are extended with shades of blue color. After mixing of colors: Newly occupied areas are marked in shades of turquoise, just abandoned areas are marked in shades of purple.
In shades of red and green coded areas for decrement and increment of the cell mass. Similarly to this [paper](https://doi.org/10.1117/1.jbo.20.11.111214).
```
n_of_collors = 'two' # 'two' or 'four' 
```
7. Select magnification of used objective lens for define of pixel area size. The pixel areas and magnifications are defined in 
the head of AID_core.py. The calculation of cell mass from phase values is defined in AID_core.py -> class Core -> rad_to_pg 
method and is described in this [paper](https://doi.org/10.1242/jcs.s3-95.31.271). Modify values of this method by your type of quantitative 
phase microscope.
```
mag = '40x' # '4x' or '10x' or '20x' or '40x' or '60x'
```
8. Select wavelength of used light (in nm).
```
wavelength = 650
```
9. Choose whether the phase values should be converted to cell  mass.
```
rad_to_pg = True # False or True
```
10. Select type of AID calculation between incremental and "to first" method.
```
AID_type = "to_first" # "increment" or "to_first"
```
11. Select procedures, which will be run:
    - 'AID' calculates data, creates images, data table and all data saves;
    - 'plot' generates output plots;
    - 'all' creates all procedures.
```
what_to_run = 'all' # 'AID' or 'plot' or 'all'
```

## Export
After running all the procedures this directory structure is obtained:
- **images_COG**    
    This directory contains the overlay source images:    
    - red color is image with index _n_
    - blue color is image with index _n+1_
    
    The white line connects points of centre of gravity of both images.
- **AID**    
    This directory contains images with AID. 
    
    For two color AID:     
    - shades of red color is decrement,
    - shades of green color is increment,

    or for four color AID:
    - shades of red color is decrement,
    - shades of green color is increment,
    - shades of turquoise color is newly occupied area,
    - shades of purple just abandoned area.
 
- **AID_raw** 
    
    This directory contains numpy files with AID. 

- **AID_COG**

   This directory contains images with AID. The same as AID. The white line connects points of centre of gravity 
   of increment and decrement.

- **zero_line_AID**    
    This directory contains images with AID: 
    
    - shades of red color is decrement,
    - shades of green color is increment,
    - white color represents zero-line.

- **zero_line_AID_raw**    
    This directory contains numpy files with zero line AID.

- **area_masks** 

    This directory contains images with areas:
    - blue color is anchor area,
    - red color is decrement area,
    - green color is increment area.

- **area_masks_raw**

    This directory contains numpy files with areas. 

- **area_masks_extended** 

    This directory contains images with extended areas. 
    - Turquoise color is anchor area with increased mass values,
    - purple color is anchor area with decreased mass values,
    - red color is decrement area,
    - green color is increment area,
    - white color represents zero-line.

- **area_masks_extended_raw**

    This directory contains numpy files with extended areas. 

- **data**

    This directory contains subdirectories with all calculated data:
    - ***image_1*** & ***image_2*** - source image files from witch  is AID calculated; numpy files; and JSON structures with  
      cell mass and centres of gravities,
    - ***increment*** - image file; numpy file; and JSON structure with  cell mass and centres of gravities, 
    - ***increment_area*** - image file; numpy file; and JSON structure with  cell mass and centres of gravities, 
    - ***decrement*** - image file; numpy file; and JSON structure with  cell mass and centres of gravities, 
    - ***decrement_area*** - image file; numpy file; and JSON structure with  cell mass and centres of gravities, 
    - ***anchor_area*** - image file; numpy file; and JSON structure with  cell mass and centres of gravities, 
    - ***anchor_increment_area*** - image file; numpy file; and JSON structure with  cell mass and centres of gravities, 
    - ***anchor_decrement_area*** - image file; numpy file; and JSON structure with  cell mass and centres of gravities, 
    - ***zeroline*** - JSON structure with length of zero-line.
    
    
- **export**
    This directory contains the all exported plots, numpy files and exported excel tables.

## Description of the graphs
**mass**

- "image x mass": 
  - *x* - image;  *y* - cell mass 
- "increment x mass": 
  - *x* - AID;  *y* - sum of  mass increment 
- "decrement x mass": 
  - *x* - AID;  *y* - sum of  mass decrement 
        
**increment-decrement_weighted**    

- "increment-decrement_COG_displacement": 
  - *x* - AID;  *y* - the distance between the weighted COGs of increment and decrement
- "increment-decrement_COG_angle": 
  - *x* - AID;  *y* - the angle between the weighted COGs of increment and decrement 
  (measured from the positive direction of the axis *x*)

**image_1_COG** and **image_1_COG_weighted**    

- vector charts:
  - axes *x* - coordinate *x*; axes  *y* - coordinate *y*; vectors - between the coordinates of the centroids 
  of the areas  (..._COG)/the weighted centroids (..._COG_weighted)
- column charts:
  - axes *x* - AID indicating the vector destination point; axes  *y* - distance or angle of the vector 
         
**image_2_COG** and **image_2_COG_weighted**    
- vector charts:
  - axes *x* - coordinate *x*; axes  *y* - coordinate *y*; vectors - between the coordinates of the centroids 
  of the areas  (..._COG)/the weighted centroids (..._COG_weighted)
- column charts:
  - axes *x* - AID indicating the vector destination point; axes  *y* - distance or angle of the vector 
      
**decrement_area_COG** and **decrement_area_COG_weighted** 
- vector charts:
  - axes *x* - coordinate *x*; axes  *y* - coordinate *y*; vectors - between the coordinates of the centroids 
  of the areas (..._COG)/the weighted centroids (..._COG_weighted)
- column charts:
  - axes *x* - AID indicating the vector destination point; axes  *y* - distance or angle of the vector 
    
**decrement_COG** and **decrement_COG_weighted**
- vector charts:
  - axes *x* - coordinate *x*; axes  *y* - coordinate *y*; vectors - between the coordinates of the centroids 
  of the areas (..._COG)/the weighted centroids (..._COG_weighted)
- column charts:
  - axes *x* - AID indicating the vector destination point; axes  *y* - distance or angle of the vector 

**increment_COG** and **increment_COG_weighted**
- vector charts:
  - axes *x* - coordinate *x*; axes  *y* - coordinate *y*; vectors - between the coordinates of the centroids 
  of the areas (..._COG)/the weighted centroids (..._COG_weighted)
- column charts:
  - axes *x* - AID indicating the vector destination point; axes  *y* - distance or angle of the vector 
        
**increment_area_COG** and **increment_area_COG_weighted** 
- vector charts:
  - axes *x* - coordinate *x*; axes  *y* - coordinate *y*; vectors - between the coordinates of the centroids 
  of the areas (..._COG)/the weighted centroids (..._COG_weighted)
- column charts:
  - axes *x* - AID indicating the vector destination point; axes  *y* - distance or angle of the vector 
                         
**anchor_area_COG** and **anchor_area_COG_weighted**    
- vector charts:
  - axes *x* - coordinate *x*; axes  *y* - coordinate *y*; vectors - between the coordinates of the centroids 
  of the areas (..._COG)/the weighted centroids (..._COG_weighted)
- column charts:
  - axes *x* - AID indicating the vector destination point; axes  *y* - distance or angle of the vector 
         
**anchor_decrement_area_COG** and **anchor_decrement_area_COG_weighted**    
- vector charts:
  - axes *x* - coordinate *x*; axes  *y* - coordinate *y*; vectors - between the coordinates of the centroids 
  of the areas (..._COG)/the weighted centroids (..._COG_weighted)
- column charts:
  - axes *x* - AID indicating the vector destination point; axes  *y* - distance or angle of the vector 
                 
**anchor_increment_area_COG** and **anchor_increment_area_COG_weighted**    
- vector charts:
  - axes *x* - coordinate *x*; axes  *y* - coordinate *y*; vectors - between the coordinates of the centroids 
  of the areas (..._COG)/the weighted centroids (..._COG_weighted)
- column charts:
  - axes *x* - AID indicating the vector destination point; axes  *y* - distance or angle of the vector 
