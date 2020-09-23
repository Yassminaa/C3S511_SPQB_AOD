#!/usr/bin/env python
import os
yyyys = 2002
yyyye = 2012
yyyy = yyyys
while yyyy <= yyyye:
    for mm in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        fin = str(yyyy)+str(mm)+'-C3S-L3_AEROSOL-AER_PRODUCTS-AATSR-ENVISAT-SWANSEA-MONTHLY-v4.32'
        fout= 'add_time/C3S-L3_AEROSOL-AER_PRODUCTS-AATSR-ENVISAT-SWANSEA-MONTHLY-v4.32_'+str(yyyy)+str(mm)+'.nc'
        os.system('cdo settunits,days -settaxis,'+str(yyyy)+'-'+str(mm)+'-15,00:00,1month '+fin+'.nc '+fout)
    yyyy += 1

