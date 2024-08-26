from case_enum import case_enum
from model import model
import os
import json

#############################################
# Benchmark:  LEU-MET-THERM-006 
# Cases:      1-30 
# Model by:   Nour Ali  
# Date:       26/08/2024
#############################################


def verify(cross_section:str, path='../verify/'):
    """
    This function is used to run the 30 cases and save the k-effective in a txt and json files.\n
    This function will first check if a case has been run before,
    if the case has been run, it will not run it again\n
    path: relative path to save case directory. """


    case={}

    case_path=path+'case'

    #check if k_eff.json exists
    if os.path.exists(path+'k_eff.json'):
        with open(path+'k_eff.json') as k:
            k_eff=json.load(k)
    else:
        k_eff={}


    for i in range(0,30):

        #check if k_eff['case'+str(i+1)] exists and has a vlue
        if 'case'+str(i+1) in k_eff.keys():
            if k_eff['case'+str(i+1)] != None:
                continue

        #run cases
        case[i+1]=model(case_enum(i+1), relative_path=case_path, cross_section=cross_section)

        #save k_eff
        sp=case[i+1].statepoint()
        k_eff['case'+str(i+1)]=str(sp.k_combined)

        with open(path+'k_eff.txt','w') as f:
            for key, value in k_eff.items():
                f.write(f'{key}: {value}\n')

        #save k_eff to json file
        with open(path+"k_eff.json", "w") as outfile: 
            json.dump(k_eff, outfile)





