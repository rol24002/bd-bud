"""Assigning numerical values to petal descriptors in order to determine which flower it is"""

#importing spreadsheet
import pandas as pd

# URL of the Google Sheets CSV export
url = "https://docs.google.com/spreadsheets/d/1M4GVrWIwBFvq14DaJubvQ5bRJ-9mTB1Mp2Hh9spKd08/export?format=csv"

# Reading the spreadsheet
df = pd.read_csv(url)


# Flower types
flowers = ["daisy", "orchid", "violet"]

# Function to lookup descriptors and create a dataset
def create_descriptor_dataset(descriptors):
    """
    Looks up each descriptor in the DataFrame and creates a new DataFrame (dataset) 
    containing the matching rows.

    Args:
        descriptors (list): A list of petal descriptors to look up.

    Returns:
        pandas.DataFrame: A DataFrame containing the rows matching the descriptors, or None if no matches.
    """
    
    rows = []
    for descriptor in descriptors:
        row = df[df["Descriptor:"].str.lower() == descriptor.lower()]
        if not row.empty:
            rows.append(row)

    if rows:
        # Concatenate the found rows into a single DataFrame
        dataset = pd.concat(rows, ignore_index=True)
        return dataset
    else:
        return None

# Calling the function with example descriptors
descriptors_to_lookup = ['green', 'white', 'small', 'pointed', 'green', 'red', 'smooth']
descriptor_dataset = create_descriptor_dataset(descriptors_to_lookup)

# Print the resulting dataset
if descriptor_dataset is not None:
    print("Dataset created from descriptors:")
    print(descriptor_dataset)
else:
    print("No matching descriptors found.")

#Example of how to access specific columns.
if descriptor_dataset is not None:
    print("\nExample: Accessing the 'Value:' column:")
    print(descriptor_dataset['Value:'])

#multiply the values in the Value: column
valueProduct = descriptor_dataset['Value:'].product()
print(valueProduct)