import json
import re

# Function to convert the timestamp format
def convert_timestamp(match):
    date = match.group(1)
    time = match.group(2)
    return f"{date} {time}"

# Read the JSON file
with open("all.json", "r") as file:
    data = json.load(file)

# Define a regular expression pattern to match the original timestamp format
original_regex_pattern = r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2}).(\d{3})Z"

# Convert dates within the JSON structure
def convert_dates(obj):
    if isinstance(obj, str):
        # Check if the string matches the timestamp format
        match = re.match(original_regex_pattern, obj)
        if match:
            return convert_timestamp(match)
        else:
            return obj
    elif isinstance(obj, list):
        return [convert_dates(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_dates(value) for key, value in obj.items()}
    else:
        return obj

# Convert dates within the loaded JSON data
converted_data = convert_dates(data)

# Write the modified JSON to an output file
with open("output.json", "w") as outfile:
    json.dump(converted_data, outfile, indent=4)

print("Conversion complete. Result saved in 'output.json'.")