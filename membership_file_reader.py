import os
import re
import h5py
import numpy as np

membership_directory = "/cosma8/data/dp004/flamingo/Runs/L1000N1800/HYDRO_FIDUCIAL/SOAP/membership_0077/" # Location of membership files
pattern = "membership_0077\.\d+\.hdf5" # Membership file format

# Find all membership_files matching the pattern
membership_files = [f for f in os.listdir(membership_directory) if re.match(pattern, f)]

# Define a function to extract the numeric part of the filename
def extract_number(filename):
    return int(re.search(r'\d+', filename.split('.')[1]).group())

# Sort membership_files numerically based on the number in the filename
membership_files.sort(key=extract_number)

print(membership_files)

# Initialize an empty list to store data arrays
Property_arrays = []

# Loop through each file and read its data into the list
for file_name in membership_files:
    with h5py.File(os.path.join(membership_directory, file_name), 'r') as f:
        Property = f['name_of_property'][:]  # Change to required quantity name 
        Property_arrays.append(Property)

print('Combining data...')
# Concatenate all arrays into one
Property_combined = np.concatenate(Property_arrays, axis=0)
print(len(Property_combined))
# Now combined_data contains all data from the membership_files in a single array
