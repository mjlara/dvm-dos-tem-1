# Sensitivity adapted for the calibration type output
# uses calibration configuration file as an input
# Example: python3 run_mads_sensitivity.py /work/mads_calibration/config-step1-md1.yaml
# Author: Elchin Jafarov 
# Date: 03/27/2023

import os,sys
import json
import numpy as np
import pandas as pd
import mads_sensitivity as Sensitivity

#read the config yaml file and 
if len(sys.argv) != 2:
    print("Usage: python run_mads_sensitivity.py <path/configfilename>")
    sys.exit(1)

config_file_name = sys.argv[1]
print(f"The filename you provided is: {config_file_name}")

#define the SA setup
driver = Sensitivity.SensitivityDriver(config_file=config_file_name)
driver.clean()
sample_size=500
driver.design_experiment(sample_size, driver.cmtnum,
  params=driver.paramnames,
  pftnums=driver.pftnums,
  percent_diffs=list(0.1*np.ones(len(driver.pftnums))),
  sampling_method='loguniform')

#customize bounds
#STEP 1
#new_bounds=[[350, 500], [250, 430], [300, 450], [100, 200], [20, 100]]

#STEP 2

#new_bounds=[[1, 10],[1, 10],[1, 10],[1, 10],[1, 10], \
#        [-20, -0.1],[-20, -0.1],[-20, -0.1],[-20, -0.1],[-20, -0.1], \
#        [-20, -0.1],[-20, -0.1], \
#        [-20, -0.1],[-20, -0.1],[-20, -0.1] 
#        ]


#STEP 3 Vegc Vegn
#new_bounds=[
#        [0.000001, 0.2], [0.00001, 0.2], [0.00001, 0.2], [0.00001, 0.2], [0.00001, 0.2], \
#        [0.00001, 0.2], [0.00001, 0.2], \
#        [0.00001, 0.2], [0.00001, 0.2], [0.00001, 0.2], \
#        [1e-7, 0.2], [1e-7, 0.2], [1e-7, 0.2], [1e-7, 0.2], [1e-7, 0.2], \
#        [1e-7, 0.2], [1e-7, 0.2], \
#        [1e-7, 0.2], [1e-7, 0.2], [1e-7, 0.2],
#        ]


#STEP 3
#new_bounds=[[1, 10],[1, 10],[1, 10],[1, 10],[1, 10], \
#        [-20, -0.1],[-20, -0.1],[-20, -0.1],[-20, -0.1],[-20, -0.1], \
#        [-20, -0.1],[-20, -0.1], \
#        [-20, -0.1],[-20, -0.1],[-20, -0.1], \
#        [0.00001, 0.2], [0.00001, 0.2], [0.00001, 0.2], [0.00001, 0.2], [0.00001, 0.2], \
#        [0.00001, 0.2], [0.00001, 0.2], \
#        [0.00001, 0.2], [0.00001, 0.2], [0.00001, 0.2], \
#        [1e-7, 0.2], [1e-7, 0.2], [1e-7, 0.2], [1e-7, 0.2], [1e-7, 0.2], \
#        [1e-7, 0.2], [1e-7, 0.2], \
#        [1e-7, 0.2], [1e-7, 0.2], [1e-7, 0.2] \
#        ]


#STEP 4
new_bounds=[[1e-2, 3],[1e-2, 1.5],[5e-3, 0.8],[1e-3, 0.25],[1e-12, 1e-4]]

for i in range(len(driver.params)):
    driver.params[i]['bounds']=new_bounds[i]

driver.generate_loguniform(sample_size)
#print(driver.info())

#setup folders based on a sample size  
try:
    driver.setup_multi(calib=True)
except ValueError:
    print("Oops!  setup_multi failed.  Check the setup...")

#run themads_sensitivity in parallel
try:
    driver.run_all_samples()
except ValueError:
    print("Oops!  run_all_samples failed.  Check the sample folders...")

#save results in the work_dir results.txt
#NOTE, that the last row in the results.txt is targets/observations
driver.save_results()

