# Importing necessary functions
from text_extract import text_extractor, text_preprocessing
from topicextractor import topic_modeling
from llama2 import generate_summary
# Example usage
file_path = "/home/sg/Downloads/PHYSICSCH4CLASS12.pdf"

complete_text = text_extractor(file_path)
processed_text = text_preprocessing(complete_text)
text = generate_summary(processed_text)
print(text)

