# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:10:48 2019

@author: Borg
"""
import os
import AID_core
import plot

path = os.path.join(os.path.dirname(__file__), "B02-02r")
trashold = 0
quantitative = False #only for images! not for raw data.
step = 1 # step od AID
time_step = 30 # time step between images in original data series (seconds)
n_of_colors = 'two' # 'two' or 'four' colors of AID
mag = '40x'
wavelength = 650 #nm
rad_to_pg = True
AID_type = "increment" # "increment" or "to_first"


what_to_run = 'all' # 'AID' or 'plot' or 'all'


if __name__ == "__main__":
    if what_to_run == 'AID': # provides AID analysis
        core = AID_core.Core(path, trashold, quantitative, step, n_of_colors, mag, wavelength, rad_to_pg, AID_type)
        core.generate_AIDs()
        AID = core.AID
        AID_names = core.AID_names
        zero_line_AID = core.zero_line_AID
        zero_lines = core.zero_lines
    
        sorted_area_masks = core.sorted_area_masks
        sorted_extended_anchor_areas = core.sorted_extended_anchor_areas
        sorted_COG = core.sorted_COG
        sorted_AID_COG = core.sorted_AID_COG
        sorted_images_COG = core.sorted_images_COG
        
        core.generate_sorted_images()
        sorted_images = core.sorted_images
        sorted_names_of_images = core.sorted_names_of_images
    
        core.save_data()
    
    if what_to_run == 'plot': # generates plots
        grafs = plot.Grafs(path, rad_to_pg)
        grafs.generate_export()
    
    if what_to_run == 'all': # provides AID analysis and generates plots
        core = AID_core.Core(path, trashold, quantitative, step, n_of_colors, mag, wavelength, rad_to_pg, AID_type)
        core.generate_AIDs()
        AID = core.AID
        AID_names = core.AID_names
        zero_line_AID = core.zero_line_AID
        zero_lines = core.zero_lines
    
        sorted_area_masks = core.sorted_area_masks
        sorted_extended_anchor_areas = core.sorted_extended_anchor_areas
        sorted_COG = core.sorted_COG
        sorted_AID_COG = core.sorted_AID_COG
        sorted_images_COG = core.sorted_images_COG
        
        core.generate_sorted_images()
        sorted_images = core.sorted_images
        sorted_names_of_images = core.sorted_names_of_images
    
        core.save_data()

        grafs = plot.Grafs(path, rad_to_pg)
        grafs.generate_export()
        
