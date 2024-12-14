import csv
import json

def parse_csv(file_path):
    """Reads a CSV file and returns the data as a list of dictionaries."""
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))

def read_json(file_path):
    """Reads a JSON file and returns the data."""
    with open(file_path, 'r', encoding="utf-8") as f:
        return json.load(f)

def write_json(file_path, data):
    """Writes data to a JSON file."""
    with open(file_path, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)
