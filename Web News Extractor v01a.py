# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:05:01 2023

@author: paulf
"""

import json
from datetime import datetime
import newspaper

# Function to extract main text from a website
def extract_main_text(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    return article.text.strip()

# User inputs website URL and filename
website_url = input("Enter the website URL: ")
filename = input("Enter the filename: ")

# Extract main text from the website
extracted_text = extract_main_text(website_url)

# Create a dictionary with the extracted data
data = {
    "website": website_url,
    "timestamp": str(datetime.now()),
    "text": extracted_text
}

# Save the data as a JSON file with timestamp-appended filename
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
output_filename = f"{filename}_{timestamp}.json"

with open(output_filename, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Main text extracted from {website_url} has been saved as {output_filename}.")
