"""Assigning numerical values to petal descriptors in order to determine which flower it is"""

#importing data
from flask import Flask, request, jsonify
from PIL import Image
import io

#not sure what this does but it is needed for the code to run
app = Flask(__name__)

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

def identify_plant(image_data):
    """
    Simulates plant identification based on image data. 
    Replace with your actual image processing logic.
    """
    # For now, let's just use placeholder descriptors.
    descriptors_to_lookup = ['green', 'white', 'small', 'pointed', 'green', 'red', 'smooth']
    descriptor_dataset = create_descriptor_dataset(descriptors_to_lookup)

    if descriptor_dataset is not None:
        valueProduct = descriptor_dataset['Value:'].product()
        #Replace this logic with your plant identification logic
        if valueProduct > 100:
            return "Daisy"
        elif valueProduct > 50:
            return "Orchid"
        else:
            return "Violet"
    else:
        return "Unknown Plant"
    
#The image handling maggigers
@app.route('/identify', methods=['POST'])
def identify():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    try:
        image = Image.open(io.BytesIO(image_file.read()))
        # You'll need to convert this image to a format your image processing model expects.
        # For simplicity, we'll pass the raw bytes for now.
        plant_name = identify_plant(image_file.read())  # Replace with actual image processing
        return jsonify({'plant': plant_name})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)