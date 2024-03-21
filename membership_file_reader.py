import os
import re
import h5py
import numpy as np

membership_directory = "/cosma8/data/dp004/flamingo/Runs/L1000N1800/HYDRO_FIDUCIAL/SOAP/membership_0077/"
pattern = "membership_0077\.\d+\.hdf5"

# Find all membership_files matching the pattern
membership_files = [f for f in os.listdir(membership_directory) if re.match(pattern, f)]

# Define a function to extract the numeric part of the filename
def extract_number(filename):
    return int(re.search(r'\d+', filename.split('.')[1]).group())

# Sort membership_files numerically based on the number in the filename
membership_files.sort(key=extract_number)

print(membership_files)
# Initialize an empty list to store data arrays
BH_GroupNumber_arrays = []

# Loop through each file and read its data into the list
for file_name in membership_files:
    with h5py.File(os.path.join(membership_directory, file_name), 'r') as f:
        BH_GroupNumber = f['PartType5/GroupNr_all'][:]  
        BH_GroupNumber_arrays.append(BH_GroupNumber)

print('Combining data...')
# Concatenate all arrays into one
BH_GroupNumber_all = np.concatenate(BH_GroupNumber_arrays, axis=0)
print(len(BH_GroupNumber_all))
# Now combined_data contains all data from the membership_files in a single array
