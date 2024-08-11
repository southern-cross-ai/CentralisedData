import os
import pandas as pd

# Directory containing the processed text files
processed_txt_dir = 'processed_text_files'

# DataFrame to store the results
df = pd.DataFrame(columns=['Filename', 'Paragraph'])

# Function to count the number of tokens in a paragraph
def count_tokens(paragraph):
    return len(paragraph.split())

# Iterate through all processed text files in the directory
for filename in os.listdir(processed_txt_dir):
    if filename.startswith('Processed_') and filename.endswith('.txt'):
        txt_path = os.path.join(processed_txt_dir, filename)

        # Read the processed text
        with open(txt_path, 'r', encoding='utf-8') as file:
            paragraphs = file.read().split('\n')

        # Filter paragraphs that have 15 or more tokens
        filtered_paragraphs = [para.strip() for para in paragraphs if count_tokens(para.strip()) >= 15]

        # Create a temporary DataFrame for the current file
        temp_df = pd.DataFrame({
            'Filename': [filename] * len(filtered_paragraphs),
            'Paragraph': filtered_paragraphs
        })

        # Concatenate the temporary DataFrame to the main DataFrame
        df = pd.concat([df, temp_df], ignore_index=True)

# Save the DataFrame to a CSV file
csv_output_path = os.path.join(processed_txt_dir, '../axiv.csv')
df.to_csv(csv_output_path, index=False, encoding='utf-8')

print(f"Processed paragraphs saved to {csv_output_path}")
