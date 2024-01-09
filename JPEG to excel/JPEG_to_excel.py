import pytesseract
from PIL import Image
import pandas as pd

def image_to_text(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Use pytesseract to convert the image into text
    text = pytesseract.image_to_string(img)
    return text

def text_to_excel(text, excel_path):
    # Split the text into lines and then split each line into columns based on spaces
    lines = text.split('\n')
    data = [line.split() for line in lines]
    # Convert the data into a pandas DataFrame and then save it as an Excel file
    df = pd.DataFrame(data)
    df.to_excel(excel_path)

# Ask for the image file path
image_path = input("Please enter the path to your image file: ").strip('\"')

# Ask for the desired Excel file path
excel_path = input("Please enter the path where you want to save the Excel file: ").strip('\"')

# Check if the Excel file path ends with .xlsx or .xls
if not (excel_path.endswith('.xlsx') or excel_path.endswith('.xls')):
    print("Error: The Excel file path should end with .xlsx or .xls")
else:
    text = image_to_text(image_path)
    text_to_excel(text, excel_path)

