####################################################################################################
# ToSingleChannelData_torcheeg.py

# input: mat file_name, electrode_name chosen for single channel model
# output: new dictionary that has single focused channel as a first row

####################################################################################################

from mappingElectrodes import mapElectrodes
import scipy
import numpy as np

def convertToSingleChannel(file_name, electrode):    # file_name: name(str) of file from Preprocessed_EEG like 1_20131107.mat 
    mat_dict = scipy.io.loadmat(file_name)           # electrode(str): chosen for single channel model
    electrodes = mapElectrodes()
    
    for i in range(3, len(list(mat_dict.keys()))):
        temp = mat_dict[list(mat_dict.keys())[i]][0]
        mat_dict[list(mat_dict.keys())[i]][0] = np.array(mat_dict[list(mat_dict.keys())[i]][electrodes[electrode]].tolist())
        mat_dict[list(mat_dict.keys())[i]][electrodes[electrode]] = temp

    return mat_dict

while (True):    
    file_names = input()
    if (file_names == "end"):
        break
    
    scipy.io.savemat("Preprocessed_EEG/" + file_names, convertToSingleChannel("Preprocessed_EEG/" + file_names, "C4"))




