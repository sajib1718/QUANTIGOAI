import json
import os

# Define the input and output file names
input_file_name = "pos_0.png.json"
output_file_name = "formatted_pos_0.png.json"

# Define the folder path where the JSON files are located
folder_path = "sampleJson"

# Read the JSON file
input_file_path = os.path.join(folder_path, input_file_name)
with open(input_file_path, "r") as file:
    data = json.load(file)

# Perform the necessary formatting
formatted_data = {
    "filename": input_file_name,
    "data": data
}

# Write the formatted data to a new JSON file
output_file_path = os.path.join(folder_path, output_file_name)
with open(output_file_path, "w") as file:
    json.dump(formatted_data, file, indent=4)

print(f"Formatted JSON saved as {output_file_name}.")
