import re
import string
import fitz  
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def text_extractor(file_path):
    try:
        # Open the PDF file
        doc = fitz.open(file_path)
        complete_text = ""

        # Loop through all pages of the document
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)

            # Extract text in 'dict' format which gives us more control
            blocks = page.get_text("dict")["blocks"]

            # Initialize strings for left and right column text
            left_column_text = ""
            right_column_text = ""

            # Split text based on its x-coordinate (position)
            for block in blocks:
                if block['type'] == 0:  # Type 0 means it's a text block
                    for line in block["lines"]:
                        for span in line["spans"]:
                            # Get the x-coordinate of the text (left side of the block)
                            x0 = span['bbox'][0]  # The x-coordinate of the text

                            # If the x-coordinate is on the left side of the page (left column)
                            if x0 < page.rect.width / 2:
                                left_column_text += span['text'] + " "
                            else:
                                right_column_text += span['text'] + " "

            # Add newline breaks between the left and right column text for each page
            complete_text += left_column_text.strip() + "\n" + right_column_text.strip() + "\n\n"
            
            # Reset the left and right column text for the next page
            left_column_text = ""
            right_column_text = ""

        doc.close()

        # Return the complete extracted text
        return complete_text.strip()

    except Exception as e:
        return f"Error extracting text: {e}"

def text_preprocessing(text, remove_numbers_flag=True):
    text = convert_to_lowercase(text)
    text = remove_punctuation(text)
    text = remove_special_symbols(text)  # Fix here: Use '=' instead of '-'
    text = remove_urls(text)
    text = remove_extra_spaces(text)
   # text = remove_stopwords(text)
    text = remove_foreign_languages(text)

    if remove_numbers_flag:
        text = remove_numbers(text)

    text = remove_extra_spaces(text)
    return text

def remove_special_symbols(text):
    """
    Removes punctuation and special symbols from the given text.
    """
    return re.sub(r'[^A-Za-z.0-9\s]', '', text) 

def remove_stopwords(text):
    """
    Removes stopwords from the given text.
    """
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Function to convert text to lowercase
def convert_to_lowercase(text):
    return text.lower()

# Function to remove punctuations
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Function to remove URLs
def remove_urls(text):
    return re.sub(r'http\S+|www\S+|https\S+', '', text)

# Function to remove extra spaces
def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

# Function to remove foreign languages (non-ASCII characters)
def remove_foreign_languages(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

def remove_numbers(text):
    """
    Removes all digits from the given text.
    """
    return re.sub(r'\d+', '', text)  # Remove all digits
