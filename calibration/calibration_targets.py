#!/usr/bin/env python

# could add code here to load up calibration_targets variable from the
# contents of an excel file...? or just plain csv?

calibration_targets = {
  # Added this data structure to support comments, units, references etc that
  # can be handled in the fixed width text parameter files as well as the csv
  # parameter files.
  "meta": {
    'GPPAllIgnoringNitrogen': {'units': 'g/m2/year', 'desc': 'GPP without N limitation', 'comment': 'ingpp', 'ref': ''},
    'NPPAllIgnoringNitrogen': {'units': 'g/m2/year', 'desc': 'NPP without N limitation', 'comment': 'innpp', 'ref': ''},
    'NPPAll': {'units': 'g/m2/year', 'desc': 'NPP with N limitation', 'comment': 'npp', 'ref': ''},
    'Nuptake': {'units': 'g/m2/year', 'desc': '', 'comment': 'nuptake', 'ref': ''},
    'VegCarbon': {
      'Leaf': {'units': 'g/m2', 'desc': '', 'comment': 'vegcl', 'ref': ''},
      'Stem': {'units': 'g/m2', 'desc': '', 'comment': 'vegcw', 'ref': ''},
      'Root': {'units': 'g/m2', 'desc': '', 'comment': 'vegcr', 'ref': ''},
    },
    'VegStructuralNitrogen': {
      'Leaf': {'units': 'g/m2', 'desc': '', 'comment': 'vegnl', 'ref': ''},
      'Stem': {'units': 'g/m2', 'desc': '', 'comment': 'vegnw', 'ref': ''},
      'Root': {'units': 'g/m2', 'desc': '', 'comment': 'vegnr', 'ref': ''},
    },
    'MossDeathC': {'units': '', 'desc': '', 'comment': 'dmossc', 'ref': ''},
    'CarbonShallow': {'units': '', 'desc': '', 'comment': 'shlwc', 'ref': ''},
    'CarbonDeep': {'units': '', 'desc': '', 'comment': 'deep', 'ref': ''},
    'CarbonMineralSum': {'units': '', 'desc': '', 'comment': 'minec', 'ref': ''},
    'OrganicNitrogenSum': {'units': '', 'desc': '', 'comment': 'soln', 'ref': ''},
    'AvailableNitrogenSum': {'units': '', 'desc': '', 'comment': 'avln', 'ref': ''},
  },

  ## WARNING: JUNK, PLACEHOLDER VALUES! USE AT YOUR OWN RISK!
  "BLANK": {
    'cmtnumber': 0,
    'PFTNames':                  [  'PFT0',  'PFT1',   'PFT2',   'PFT3',  'PFT4',  'PFT5',  'PFT6',  'PFT7',  'PFT0', 'PFT9'],
    'GPPAllIgnoringNitrogen':    [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # innpp     (gC/m2/year)   NPP without N limitation 
    'NPPAll':                    [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # vegcl     (gC/m2)
      'Stem':                    [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # vegcw     (gC/m2)
      'Root':                    [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # vegnl     (gN/m2)
      'Stem':                    [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # vegnw     (gN/m2)
      'Root':                    [     0.0,     0.0,      0.0,      0.0,     0.0,     0.0,     0.0,     0.0,     0.0,    0.0 ], # vegnr     (gN/m2)
    },
    'MossDeathC':                0.00,    #  dmossc
    'CarbonShallow':             0.00,    #  shlwc
    'CarbonDeep':                0.00,    #  deepc
    'CarbonMineralSum':          0.00,    #  minec
    'OrganicNitrogenSum':        0.00,    #  soln
    'AvailableNitrogenSum':      0.00,    #  avln
  },
  ## CMT01 - Black Spruce Forest, calibration for Murphy Dome climate.
  "black spruce forest": {
    'cmtnumber': 1,
                                 #    pft0     pft1      pft2      pft3     pft4     pft5     pft6     pft7     pft8    pft9   
    'PFTNames':                  ['BlackSpr', 'DecidShrub', 'Decid', 'Moss', '', '', '', '', '', ''],
    'GPPAllIgnoringNitrogen':    [  306.07,   24.53,    46.53,    54.23,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [  229.56,   18.40,    34.90,    40.65,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # innpp     (gC/m2/year)   NPP without N limitation
    'NPPAll':                    [  153.04,   12.27,    17.36,    27.10,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [    1.26,    0.07,     0.23,     0.03,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [  293.76,   15.13,     9.06,   180.85,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegcl     (gC/m2)
      'Stem':                    [ 1796.32,  100.16,   333.75,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegcw     (gC/m2)
      'Root':                    [  404.48,   15.07,    44.80,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [    6.35,    0.72,     0.70,     1.61,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegnl     (gN/m2)
      'Stem':                    [   24.34,    2.48,     9.45,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegnw     (gN/m2)
      'Root':                    [    0.17,    0.01,     0.03,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':              178.00,    #  dmossc
    'CarbonShallow':           888.91,    #  shlwc
    'CarbonDeep':             3174.53,    #  deepc
    'CarbonMineralSum':      19821.50,    #  minec
    'OrganicNitrogenSum':     1086.31,    #  soln
    'AvailableNitrogenSum':      0.76,    #  avln
  },
  ## CMT02 - White Spruce Forest, calibration for Murphy Dome climate.
  "white spruce forest": {
    'cmtnumber': 2,
                                 #    pft0     pft1      pft2      pft3     pft4     pft5     pft6     pft7     pft8    pft9   
    'PFTNames':                  ['WhiteSpr', 'DecidShrub', 'Decid', 'Moss', '', '', '', '', '', ''],
    'GPPAllIgnoringNitrogen':    [  491.81,   10.73,   189.32,    54.20,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [  368.96,    8.04,   141.99,    40.65,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # innpp     (gC/m2/year)   NPP without N limitation
    'NPPAll':                    [  245.90,    5.36,    94.66,    27.10,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [    1.36,    0.05,     0.92,     0.03,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [  417.34,    2.26,    26.99,   180.85,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegcl     (gC/m2)
      'Stem':                    [ 5359.60,   76.76,  1367.66,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegcw     (gC/m2)
      'Root':                    [  401.63,   10.33,   182.27,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [    9.03,    0.11,     2.10,     1.61,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegnl     (gN/m2)
      'Stem':                    [   72.61,    1.90,    38.72,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegnw     (gN/m2)
      'Root':                    [    9.20,    0.20,     3.57,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':              178.00,    #  dmossc
    'CarbonShallow':          1156.00,    #  shlwc
    'CarbonDeep':             4254.00,    #  deepc
    'CarbonMineralSum':      11005.00,    #  minec
    'OrganicNitrogenSum':      699.81,    #  soln
    'AvailableNitrogenSum':      1.69,    #  avln
  },
  ## CMT03 - Deciduous Forest, calibration for Murphy Dome climate.
  "deciduous forest": {
    'cmtnumber': 3,
                                 #    pft0     pft1      pft2      pft3     pft4     pft5     pft6     pft7     pft8    pft9   
    'PFTNames':                  ['SprTree', 'DecidShrub', 'DecidTree', 'Moss', '', '', '', '', '', ''],
    'GPPAllIgnoringNitrogen':    [    1.81,   61.75,   997.38,     0.82,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [    1.36,   46.31,   748.03,     0.62,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # innpp     (gC/m2/year)   NPP without N limitation
    'NPPAll':                    [    0.91,   30.87,   498.69,     0.41,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [    1.69,    0.07,     3.68,     0.01,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [    2.47,    8.33,   131.74,     5.60,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegcl     (gC/m2)
      'Stem':                    [   11.82,   93.25,  5469.13,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegcw     (gC/m2)
      'Root':                    [    0.99,   13.28,   731.99,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [    0.05,    0.41,     7.04,     0.10,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegnl     (gN/m2)
      'Stem':                    [    0.16,    2.37,   107.98,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegnw     (gN/m2)
      'Root':                    [    0.01,    0.11,     1.08,     0.00,    0.00,    0.00,    0.00,    0.00,    0.00,   0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':              178.19,    #  dmossc
    'CarbonShallow':           534.19,    #  shlwc
    'CarbonDeep':             2017.94,    #  deepc
    'CarbonMineralSum':      11004.89,    #  minec
    'OrganicNitrogenSum':      699.89,    #  soln
    'AvailableNitrogenSum':       3.5,    #  avln
  },
  ## CMT04 - Shrub Tundra, calibration for Toolik climate.
  "shrub tundra": {
    'cmtnumber': 4,
                                 #    pft0     pft1      pft2     pft3     pft4     pft5      pft6      pft7      pft8     pft9   
                  'PFTNames':    ['Salix', 'Betula', 'Decid', 'EGreen', 'Sedges', 'Forbs', 'Grasses', 'Lichens', 'Feather', 'PFT9'],
    'GPPAllIgnoringNitrogen':    [  143.89,  288.65,   42.33,    9.03,    19.39,   28.44,    11.29,    16.45,     37.38,    0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [  107.92,  216.49,   39.57,    8.44,    18.13,   26.59,    10.56,     8.23,     18.69,    0.00 ], # innpp     (gC/m2/year)   NPP without N limitation 
    'NPPAll':                    [   71.95,  144.33,   21.16,    4.51,     9.69,   14.22,     5.65,     8.23,     18.69,    0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [    0.81,    1.55,    0.29,    0.06,     0.14,    0.21,     0.08,     0.01,      0.54,    0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [   23.85,   38.01,   14.85,    1.30,     3.64,    5.33,     2.12,     18.7,     89.00,    0.00 ], # vegcl     (gC/m2)
      'Stem':                    [  194.07,  502.07,   30.67,    9.47,     0.00,    0.00,     0.00,      0.0,      0.00,    0.00 ], # vegcw     (gC/m2)
      'Root':                    [    6.10,   38.35,    2.25,    0.66,     6.06,    8.89,     3.53,      0.0,      0.00,    0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [    1.16,    1.84,    0.73,    0.03,     0.17,    0.25,     0.09,     0.67,      2.59,    0.00 ], # vegnl     (gN/m2)
      'Stem':                    [    1.94,    5.73,    0.66,    0.18,     0.00,    0.00,     0.00,     0.00,      0.00,    0.00 ], # vegnw     (gN/m2)
      'Root':                    [    0.08,    0.56,    0.04,    0.01,     0.12,    0.17,     0.07,     0.00,      0.00,    0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':              178.00,    #  dmossc
    'CarbonShallow':          2240.00,    #  shlwc
    'CarbonDeep':             5853.00,    #  deepc
    'CarbonMineralSum':      37022.00,    #  minec
    'OrganicNitrogenSum':     1843.00,    #  soln
    'AvailableNitrogenSum':      3.93,    #  avln
  },
  ## CMT05 Tussock Tundra (updated 2/23/2016, JDC: GPPain, NPPain, NPPall, Nuptake, Veg from Shaver & Chapin 1991; 
  ## Assume Toolik C:N same as Council; then Veg N = Shaver & Chapin Veg C * (Council N / Council C); MossDeathC from CTucker data;
  ## Soils data from H. Genet Tussock.xls and Nat. Soil Carbon Database (averages for Tussock from few profiles around and at Toolik)
  "tussock tundra": {
    'cmtnumber': 5,
                                 #    pft0     pft1      pft2      pft3     pft4     pft5     pft6     pft7     pft8    pft9   
                  'PFTNames':    ['Betula', 'Decid', 'EGreen', 'Sedges', 'Forbs', 'Lichens', 'Feather', 'Sphag', 'PFT8', 'PFT9'],
    'GPPAllIgnoringNitrogen':    [  106.20,   54.13,   208.50,   390.40,   7.016,  286.80,  191.80,   172.60,   0.00,   0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [   59.00,   27.06,   104.20,   195.20,   3.508,  136.60,   94.97,    85.42,   0.00,   0.00 ], # innpp     (gC/m2/year)   NPP without N limitation 
    'NPPAll':                    [   34.71,   14.47,    55.74,   104.40,   1.876,   68.29,   48.70,    43.81,   0.00,   0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [   0.197,   0.082,    0.418,    0.731,   0.009,   0.074,   0.487,    0.376,   0.00,   0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [    4.14,   15.01,    74.61,   105.25,    0.85,    42.70,   37.22,   86.84,   0.00,   0.00 ], # vegcl     (gC/m2)
      'Stem':                    [   69.78,   30.42,   127.74,     0.00,    0.00,     0.00,    0.00,    0.00,   0.00,   0.00 ], # vegcw     (gC/m2)
      'Root':                    [    4.54,    5.41,    11.84,   166.51,   11.71,     0.00,    0.00,    0.00,   0.00,   0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [    0.13,    0.47,     1.58,     4.72,    0.03,     0.69,    0.56,    1.49,   0.00,   0.00 ], # vegnl     (gN/m2)
      'Stem':                    [    1.13,    0.49,     2.06,     0.00,    0.00,     0.00,    0.00,    0.00,   0.00,   0.00 ], # vegnw     (gN/m2)
      'Root':                    [    1.02,    1.21,     1.77,     7.48,    1.81,     0.00,    0.00,    0.00,   0.00,   0.00 ], # vegnr     (gN/m2)
    },
    'RE':                       25.00,    #  Respiration_ecosystem  ** JUNK VALUE FOR TESTING! **
    'NEE':                      10.00,     #  Net Ecosystem Exchange ** JUNK VALUE FOR TESTING! **
    'MossDeathC':              178.00,    #  dmossc
    'CarbonShallow':          3079.00,    #  shlwc
    'CarbonDeep':             7703.00,    #  deepc
    'CarbonMineralSum':      43404.00,    #  minec
    'OrganicNitrogenSum':     2206.00,    #  soln
    'AvailableNitrogenSum':      8.958,   #  avln
  },
  ## CMT06 - WETSEDGE TUNDRA - CALIBRATION WITH toolik climate (also barrow climate)  Lichen gpp was 0.375, npp 0.187, feather 8.4 sphg 2.9, 1.45
  "wet sedge tundra": {
    'cmtnumber': 6,
                                 #    pft0     pft1      pft2      pft3     pft4     pft5     pft6     pft7     pft8    pft9   
                  'PFTNames':    ['Decid', 'Sedges', 'Grasses', 'Forbs', 'Lichens', 'Feather', 'Sphag', 'PFT7', 'PFT8', 'PFT9'],
    'GPPAllIgnoringNitrogen':    [  11.833,  197.867,   42.987,   10.667,   3.375,  16.000,   6.000,    0.00,   0.00,   0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [  11.064,  187.005,   40.193,    9.973,   2.187,   8.000,   3.000,    0.00,   0.00,   0.00 ], # innpp     (gC/m2/year)   NPP without N limitation 
    'NPPAll':                    [   5.916,   98.933,   21.493,    5.333,   2.187,   8.000,   3.000,    0.00,   0.00,   0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [   0.041,    1.758,    0.382,    0.089,    0.01,   0.033,   0.012,    0.00,   0.00,   0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [   2.000,   37.100,     8.06,    2.000,    2.00,   22.00,   23.00,    0.00,   0.00,   0.00 ], # vegcl     (gC/m2)
      'Stem':                    [   4.000,    0.000,     0.00,    0.000,    0.00,    0.00,    0.00,    0.00,   0.00,   0.00 ], # vegcw     (gC/m2)
      'Root':                    [   0.297,  161.280,    11.04,    3.200,    0.00,    0.00,    0.00,    0.00,   0.00,   0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [   0.006,    0.740,    0.161,    0.048,    0.12,    0.66,   0.012,    0.00,   0.00,   0.00 ], # vegnl     (gN/m2)
      'Stem':                    [   0.207,    0.000,    0.000,    0.000,    0.00,    0.00,   0.000,    0.00,   0.00,   0.00 ], # vegnw     (gN/m2)
      'Root':                    [   0.069,    2.776,    0.603,    0.130,    0.00,    0.00,   0.000,    0.00,   0.00,   0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':              178.00,    #  dmossc
    'CarbonShallow':          3358.00,    #  shlwc
    'CarbonDeep':             8401.00,    #  deepc
    'CarbonMineralSum':      44252.00,    #  minec
    'OrganicNitrogenSum':     2698.00,    #  soln
    'AvailableNitrogenSum':      0.48,    #  avln
  },
  ## CMT07 - HEATH TUNDRA - CALIBRATION TOOLIK CLIMATE   New Values from Helene, input by Joy 8 16 2019, except Nuptake and soilC numbers and forb
  "heath tundra": {
    'cmtnumber': 7,
                                 #    pft0     pft1      pft2      pft3       pft4    pft5      pft6    pft7     pft8    pft9   
                  'PFTNames':    ['Decid',  'EGreen',  'Forbs',  'Lichens','Grasses','Moss',   'PFT6', 'PFT7',  'PFT8',  'PFT9'],
    'GPPAllIgnoringNitrogen':    [  37.204,   69.055,    2.667,    72.760,   0.100,   0.744,    0.00,    0.00,    0.00,   0.00 ], # ingpp (gC/m2/year) GPP Wout N limitation
    'NPPAllIgnoringNitrogen':    [  18.602,   34.528,    2.493,    36.380,   0.050,   0.372,    0.00,    0.00,    0.00,   0.00 ], # innpp (gC/m2/year) NPP Wout N limitation 
    'NPPAll':                    [  12.401,   23.018,    1.333,    24.253,   0.033,   0.248,    0.00,    0.00,    0.00,   0.00 ], # npp   (gC/m2/year) NPP with N limitation
    'Nuptake':                   [    0.09,    0.215,    0.165,     0.010,   0.080,   0.051,    0.00,    0.00,    0.00,   0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [   6.908,   28.501,    1.100,    80.844,   1.029,   0.827,    0.00,    0.00,    0.00,   0.00 ], # vegcl     (gC/m2)
      'Stem':                    [  30.483,   67.635,    0.000,     0.000,   0.000,   0.000,    0.00,    0.00,    0.00,   0.00 ], # vegcw     (gC/m2)
      'Root':                    [  21.405,   43.189,    0.833,     0.000,   0.921,   0.000,    0.00,    0.00,    0.00,   0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [   0.274,    0.736,    0.300,     1.708,   0.018,   0.028,    0.00,    0.00,    0.00,   0.00 ], # vegnl     (gN/m2)
      'Stem':                    [   0.807,    1.414,    0.000,     0.000,   0.000,   0.000,    0.00,    0.00,    0.00,   0.00 ], # vegnw     (gN/m2)
      'Root':                    [   0.362,    0.446,    0.030,     0.000,   0.011,   0.000,    0.00,    0.00,    0.00,   0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':              178.00,    #  dmossc
    'CarbonShallow':          1065.00,    #  shlwc
    'CarbonDeep':             1071.00,    #  deepc
    'CarbonMineralSum':      32640.00,    #  minec
    'OrganicNitrogenSum':     1405.00,    #  soln
    'AvailableNitrogenSum':      0.17,    #  avln
  },
  ## Prepared from Vijay Patil work in the Yukon Flats with the mentoring of Eugenie Euskirchen- soil data comes from unknown
  "Shrubland": {
    'cmtnumber': 8,
                                 #      pft0      pft1      pft2      pft3     pft4     pft5     pft6     pft7      pft8    pft9   
                 # 'PFTNames':    ['D.Shrub', 'E.Shrub', 'D.Tree', 'E.Tree', 'Forbs', 'Gram', 'Feather', 'Lichen', 'Equisetum', 'Misc.'],
    'GPPAllIgnoringNitrogen':    [    166.12,     50.78,   319.62,   634.91,  120.25, 1086.39,   44.93,    8.40,    38.93,   0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [     83.06,     25.39,   159.81,   317.45,   60.12,  543.19,   22.46,    4.20,    19.47,   0.00 ], # innpp     (gC/m2/year)   NPP without N limitation 
    'NPPAll':                    [     55.37,     16.93,    85.46,   169.76,   32.15,  290.48,   22.46,    4.20,    10.41,   0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [      0.92,      0.26,     0.96,     2.08,    0.43,    3.85,    0.41,    0.06,     0.12,   0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [     50.91,     23.05,    35.94,    27.16,    6.83,  259.09,   67.39,    4.44,     2.38,   0.00 ], # vegcl     (gC/m2)
      'Stem':                    [     87.33,     26.03,  1000.19,   919.68,    0.00,    0.00,    0.00,    0.00,     0.00,   0.00 ], # vegcw     (gC/m2)
      'Root':                    [     40.09,     12.27,   207.23,    85.22,   44.01,  452.05,    0.00,    0.00,     9.50,   0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [      2.12,      0.76,     1.11,     0.75,    0.49,   10.24,    2.48,    0.12,     0.09,   0.00 ], # vegnl     (gN/m2)
      'Stem':                    [      1.38,      0.49,    15.78,    11.83,    0.00,    0.00,    0.00,    0.00,     0.00,   0.00 ], # vegnw     (gN/m2)
      'Root':                    [      0.84,      0.25,     4.19,     1.69,    0.85,    8.61,    0.00,    0.00,     0.17,   0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':              178.00,    #  dmossc
    'CarbonShallow':          3745.51,    #  shlwc
    'CarbonDeep':             7672.62,    #  deepc
    'CarbonMineralSum':      24235.14,    #  minec
    'OrganicNitrogenSum':     2177.91,    #  soln
    'AvailableNitrogenSum':       0.8,    #  avln
  },
 ## Prepared from EML??
  "Shrub tundra EML": {
    'cmtnumber': 9,
                                 #      pft0       pft1      pft2      pft3     pft4     pft5     pft6     pft7      pft8    pft9   
                  #'PFTNames':    ['Betnan', 'Carex', 'Ericoid', 'Feather', 'Lichen', 'Othmoss', 'Rubcha', 'Misc.', 'Misc.', 'Misc.'],
    'GPPAllIgnoringNitrogen':    [   1112.72,    200.06,   725.94,   364.58,   52.96,   55.43,  129.52,    0.00,    0.00,   0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [    834.54,    150.04,   544.46,   273.44,   39.72,   41.57,   97.14,    0.00,    0.00,   0.00 ], # innpp     (gC/m2/year)   NPP without N limitation 
    'NPPAll':                    [    556.36,    100.03,   362.97,   182.29,   26.48,   27.71,   64.76,    0.00,    0.00,   0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [      6.68,      1.20,     4.36,     2.19,    0.32,    0.33,    0.78,    0.00,    0.00,   0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [    397.15,     19.63,   269.81,   588.10,  139.99,   89.41,    1.33,    0.00,    0.00,   0.00 ], # vegcl     (gC/m2)
      'Stem':                    [   1767.96,    171.73,  1362.49,     0.00,    0.00,    0.00,   82.22,    0.00,    0.00,   0.00 ], # vegcw     (gC/m2)
      'Root':                    [    203.43,     80.40,   245.86,     0.00,    0.00,    0.00,   63.43,    0.00,    0.00,   0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [      6.95,      0.57,     5.52,     8.75,    2.30,    0.50,   0.044,    0.00,    0.00,   0.00 ], # vegnl     (gN/m2)
      'Stem':                    [     26.05,      2.30,    13.91,     0.00,    0.00,    0.00,    1.30,    0.00,    0.00,   0.00 ], # vegnw     (gN/m2)
      'Root':                    [      3.33,      0.92,     2.47,     0.00,    0.00,    0.00,    1.27,    0.00,    0.00,   0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':                0.00,    #  dmossc928.0
    'CarbonShallow':          4365.66,    #  shlwc
    'CarbonDeep':            12814.11,    #  deepc
    'CarbonMineralSum':      36329.49,    #  minec
    'OrganicNitrogenSum':     1904.10,    #  soln
    'AvailableNitrogenSum':      4.00,    #  avln
  },
 ## Prepared from EML??
  "Tussock tundra EML": {
    'cmtnumber': 10,
                                 #      pft0       pft1      pft2      pft3     pft4     pft5     pft6     pft7      pft8    pft9   
                  #'PFTNames':    ['Betnan', 'Carex', 'Ericoid', 'Erivag', 'Feather', 'Lichen', 'Othmoss', 'Rubcha', 'Sphag.', 'Misc.'],
    'GPPAllIgnoringNitrogen':    [     80.64,    300.26,   572.29,   657.57,   0.133,   46.58,  415.07,  154.58,    9.03,   0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [     60.48,    225.19,   429.22,   493.18,   0.100,   34.94,  311.31,  115.93,    6.77,   0.00 ], # innpp     (gC/m2/year)   NPP without N limitation 
    'NPPAll':                    [     40.32,    150.13,   286.14,   328.79,   0.066,   23.29,  207.54,   77.29,    4.51,   0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [      0.48,      1.80,     3.43,     3.95,  0.0008,    0.28,    2.49,    0.93,    0.05,   0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [      8.71,     18.65,   228.12,   269.81,   0.214,  123.12,  669.55,    0.71,   35.44,   0.00 ], # vegcl     (gC/m2)
      'Stem':                    [     11.64,    243.40,  1089.93,   226.60,   0.000,    0.00,    0.00,   22.40,    0.00,   0.00 ], # vegcw     (gC/m2)
      'Root':                    [     31.60,    140.91,   187.16,    58.98,   0.000,    0.00,    0.00,   76.58,    0.00,   0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [      0.15,      0.52,     4.46,     6.98,  0.0043,    0.95,   10.34,   0.027,    0.70,   0.00 ], # vegnl     (gN/m2)
      'Stem':                    [      0.11,      3.01,     9.77,     6.67,   0.000,    0.00,    0.00,    0.42,    0.00,   0.00 ], # vegnw     (gN/m2)
      'Root':                    [      0.34,      1.52,     1.77,     0.65,   0.000,    0.00,    0.00,    1.08,    0.00,   0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':                0.00,    #  dmossc
    'CarbonShallow':          4365.66,    #  shlwc
    'CarbonDeep':            12814.11,    #  deepc
    'CarbonMineralSum':      43416.95,    #  minec
    'OrganicNitrogenSum':     1998.37,    #  soln
    'AvailableNitrogenSum':      1.70,    #  avln
  },
  ## Updated by Heather Greaves 2017
  "Boreal Bog": {
    'cmtnumber': 31,
                                 #    pft0      pft1      pft2       pft3      pft4     pft5      pft6    pft7     pft8    pft9   
                                 #    Sphag     Sedge    Dshrub     Eshrub     Forb     Moss      Misc.   Misc.    Misc.   Misc.
    'GPPAllIgnoringNitrogen':    [   504.11,   133.91,    12.82,    207.88,    65.46,   27.25,    0.0,    0.0,     0.0,    0.0 ], # ingpp     (gC/m2/year)   GPP without N limitation 
    'NPPAllIgnoringNitrogen':    [   252.05,    66.95,     6.41,    103.94,    32.73,   13.62,    0.0,    0.0,     0.0,    0.0 ], # innpp     (gC/m2/year)   NPP without N limitation
    'NPPAll':                    [   190.95,    35.81,     3.43,     40.84,    17.51,    8.51,    0.0,    0.0,     0.0,    0.0 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [     3.23,     0.7,      0.02,     0.23,      0.04,    0.33,    0.0,    0.0,     0.0,    0.0 ], # nuptake   (gN/m2/year)
    'VegCarbon': {                                                                                            
      'Leaf':                    [   141.12,    22.74,     0.57,     16.10,     7.13,   24.04,    0.0,    0.0,     0.0,    0.0 ], # vegcl     (gC/m2) 
      'Stem':                    [     0.00,    45.80,    13.24,     74.89,     0.0,     0.0,     0.0,    0.0,     0.0,    0.0 ], # vegcw     (gC/m2)
      'Root':                    [     0.00,    59.83,     6.75,     70.59,    52.89,    0.0,     0.0,    0.0,     0.0,    0.0 ], # vegcr     (gC/m2)
    },                                                                                                        
    'VegStructuralNitrogen': {                                                                                
      'Leaf':                    [     1.771,    0.948,    0.021,     0.543,    0.317,   0.285,   0.0,    0.0,     0.0,    0.0 ], # vegnl     (gN/m2)
      'Stem':                    [     0.0,      0.728,    0.230,     1.274,    0.0,     0.0,     0.0,    0.0,     0.0,    0.0 ], # vegnw     (gN/m2)
      'Root':                    [     0.0,      1.618,    0.160,     1.754,    1.485,   0.0,     0.0,    0.0,     0.0,    0.0 ], # vegnr     (gN/m2)
    },
    'MossDeathC':                0.00,    #  dmossc ## IGNORE
    'CarbonShallow':          6028.95,    #  shlwc# From Mi et al, based on Manies
    'CarbonDeep':            40300.79,    #  deepc# From Mi et al, based on Manies
    'CarbonMineralSum':      60975.00,    #  minec# From Manies %C, %N, and BD
    'OrganicNitrogenSum':     5548.86,    #  soln # From Manies %C, %N, and BD
    'AvailableNitrogenSum':      9.41     #  avln # Using Bayley et al 2005 extractable n
  },
  ## CMT44 - SHRUB TUNDRA - CALIBRATION SEWARD PENINSULA CLIMATE (COUNCIL)   JOY Aug 17 2019 changed BETULA for Kougarok
  "shrub tundra kougarok": {
    'cmtnumber': 44,
                                 #    pft0     pft1      pft2     pft3     pft4     pft5      pft6      pft7      pft8     pft9   
                  'PFTNames':    [ 'Salix', 'Betula', 'Decid.', 'E.green','Sedges','Forbs','Grasses','Lichens','Feather.', 'Misc.'],
    'GPPAllIgnoringNitrogen':    [  143.89,  167.82,   42.33,    9.03,    19.39,   28.44,    11.29,    16.45,     37.38,    0.00 ], # ingpp     (gC/m2/year)   GPP without N limitation
    'NPPAllIgnoringNitrogen':    [  107.92,  125.87,   39.57,    8.44,    18.13,   26.59,    10.56,     8.23,     18.69,    0.00 ], # innpp     (gC/m2/year)   NPP without N limitation 
    'NPPAll':                    [   71.95,   83.91,   21.16,    4.51,     9.69,   14.22,     5.65,     8.23,     18.69,    0.00 ], # npp       (gC/m2/year)   NPP with N limitation
    'Nuptake':                   [    0.81,    0.90,    0.29,    0.06,     0.14,    0.21,     0.08,     0.01,      0.54,    0.00 ], # nuptake   (gN/m2/year)
    'VegCarbon': {
      'Leaf':                    [   23.85,   22.10,   14.85,    1.30,     3.64,    5.33,     2.12,     18.7,     89.00,    0.00 ], # vegcl     (gC/m2)
      'Stem':                    [  194.07,  291.90,   30.67,    9.47,     0.00,    0.00,     0.00,      0.0,      0.00,    0.00 ], # vegcw     (gC/m2)
      'Root':                    [    6.10,   22.30,    2.25,    0.66,     6.06,    8.89,     3.53,      0.0,      0.00,    0.00 ], # vegcr     (gC/m2)
    },
    'VegStructuralNitrogen': {
      'Leaf':                    [    1.16,    1.07,    0.73,    0.03,     0.17,    0.25,     0.09,     0.67,      2.59,    0.00 ], # vegnl     (gN/m2)
      'Stem':                    [    1.94,    3.33,    0.66,    0.18,     0.00,    0.00,     0.00,     0.00,      0.00,    0.00 ], # vegnw     (gN/m2)
      'Root':                    [    0.08,    0.33,    0.04,    0.01,     0.12,    0.17,     0.07,     0.00,      0.00,    0.00 ], # vegnr     (gN/m2)
    },
    'MossDeathC':              178.00,    #  dmossc
    'CarbonShallow':          2240.00,    #  shlwc
    'CarbonDeep':             5853.00,    #  deepc
    'CarbonMineralSum':      37022.00,    #  minec
    'OrganicNitrogenSum':     1843.00,    #  soln
    'AvailableNitrogenSum':      3.93,    #  avln
  }

}

def cmtbynumber(cmtnum):
  '''
  Find target values for a single CMT based on the number only.

  Parameters
  ----------
  cmtnumber : int
    The integer value for the CMT to return data for.

  Returns
  -------
  data : dict
    A multi-level dict structure with calibration target data for a single CMT.

  Raises
  ------
  RuntimeError if the cmtnum is not found anywhere in the calibration_targets
  data structure.
  '''
  for k, v in calibration_targets.items():
    if 'cmtnumber' in v.keys():
      if v['cmtnumber'] == cmtnum:
        return {k:v}
  raise RuntimeError("Can't find cmtnumber: {}".format(cmtnum))


def cmtnames():
  '''returns a list of community names'''
  return [key for key in list(calibration_targets.keys())]

def cmtnumbers():
  '''returns the cmt number for each known commnunity'''
  return [data['cmtnumber'] for k, data in calibration_targets.items()]

def caltargets2prettystring():
  '''returns a formatted string with one cmt name/number pair per line'''
  s = ''
  for key, value in calibration_targets.items():
    s += "{1:02d} {0:}\n".format(key, value['cmtnumber'])
  s = s[0:-1] # trim the last new line
  return s

def caltargets2prettystring2():
  '''returns sorted (by number) formatted string with '# - name' per line'''
  l = [
      '%s - %s' % (data['cmtnumber'], k)
      for k, data in
        calibration_targets.items()
  ]

  sl = sorted(l)
  return '\n'.join(sl)

def caltargets2prettystring3():
  '''returns a space separated list of (#)name pairs, sorted by number'''
  l = [
      '(%s)%s' % (data['cmtnumber'], k)
      for k, data in
        calibration_targets.items()
  ]

  sl = sorted(l)
  return ' '.join(sl)


def toxl():
  ''' A total hack attempt at writing out an excel workbook from the values
  that are hardcoded above in the calibraiton_targets dict. Actually kinda 
  works though...'''

  import xlwt

  font0 = xlwt.Font()
  font0.name = 'Times New Roman'
  font0.colour_index = 2
  font0.bold = True

  style0 = xlwt.XFStyle()
  style0.font = font0

  wb = xlwt.Workbook()

  nzr = 5
  nzc = 5


  for community, cmtdata in calibration_targets.items():
    ws = wb.add_sheet(community)

    #        r  c
    ws.write(0, 0, 'community number:', style0)
    ws.write(0, 1, cmtdata['cmtnumber'])

    r = nzr
    for key, data in cmtdata.items():
      print("OPERATING ON: %s" % key)
      if key == 'cmtnumber':
        pass
      else:
        ws.write(r, 1, key) # col 1, the main key
        print("row: %s col: %s key: %s" % (r, 1, key))
        if type(data) == list:
          for col, pftvalue in enumerate(data):
            ws.write(r, col + nzc, pftvalue)
            print("row: %s col: %s pftvalue: %s" % (r, col + nzc, pftvalue))

          r = r + 1
            
        elif type(data) == dict:
          for compartment, pftvals in data.items():
            ws.write(r, 2, compartment)
            print("row: %s col: %s compartment: %s" % (r, 2, compartment))

            for col, pftvalue in enumerate(pftvals):
              ws.write(r, col + nzc, pftvalue)
              print("row: %s col: %s pftvalue: %s" % (r, col + nzc, pftvalue))

            r = r + 1
        elif type(data) == int or type(data) == float:
          print("WTF")
          ws.write(r, nzc, data)
          print("row: %s col: %s data: %s" % (r, nzc, data))
          r = r + 1



  wb.save('example.xls')




def frmxl():
  print("NOT IMPLEMENTED")

if __name__ == '__main__':
  print("Nothing happening here yet...")

  # for testing:
  toxl()






