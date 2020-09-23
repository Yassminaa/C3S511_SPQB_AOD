#!/usr/bin/env python

import cdsapi
import numpy as np 
import os

c = cdsapi.Client()

# Here you define all the scripts parameters
stream =  'satellite-aerosol-properties'
file_fmt = 'zip'
yyyys = 2002
yyyye = 2012

yyyy = yyyys

while yyyy <= yyyye:

 for mm in ['01','02','03','04','05','06','07','08','09','10','11','12']:

    fout = 'AATSR_monthly_'+str(yyyy)+str(mm)
    y=str(yyyy)
    c.retrieve(stream,{
    'variable'      : 'aerosol_optical_depth',
    'sensor_on_satellite': 'aatsr_on_envisat',
    'algorithm': 'swansea',
    'year'          : y,
    'month'         : mm,
    'time_aggregation': 'monthly_average',
    'version': 'v4.32',
    'format'        : file_fmt
    }, fout+'.zip')

    os.system('unzip '+fout+'.zip')
 
 yyyy += 1

