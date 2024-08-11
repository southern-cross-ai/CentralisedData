import os
import re

# Directory containing the text files
txt_dir = 'text_files'
# Directory to save processed text files
processed_txt_dir = 'processed_text_files'
os.makedirs(processed_txt_dir, exist_ok=True)


# Function to concatenate split paragraphs
def concatenate_paragraphs(text):
    lines = text.splitlines()
    paragraphs = []
    current_paragraph = []

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            if current_paragraph:
                paragraphs.append(' '.join(current_paragraph))
                current_paragraph = []
        else:
            current_paragraph.append(stripped_line)

    if current_paragraph:
        paragraphs.append(' '.join(current_paragraph))

    return '\n\n'.join(paragraphs)


# Function to remove math formulas and special symbols
def remove_math_and_symbols(text):
    math_patterns = [
        r'\$.*?\$',  # Inline math (e.g., $x+y$)
        r'\[.*?\]',  # Math in brackets
        r'\(.*?\)',  # Math in parentheses
        r'\\[a-zA-Z]+\b',  # LaTeX commands
        r'=\s*\d+',  # Equations like x = 5
    ]
    for pattern in math_patterns:
        text = re.sub(pattern, '', text)
    return text


# Function to remove non-textual elements
def remove_non_textual_elements(text):
    # Remove lines with keywords like 'Figure', 'Table', 'References', etc.
    text = re.sub(r'Figure \d+|Table \d+|References|Acknowledgments', '', text)
    # Remove headers/footers or page numbers (common in academic papers)
    text = re.sub(r'\d+\s*$', '', text, flags=re.MULTILINE)
    return text


# Function to remove short paragraphs
def remove_short_paragraphs(text, min_word_count=20):
    paragraphs = text.split('\n\n')
    filtered_paragraphs = [para for para in paragraphs if len(para.split()) >= min_word_count]
    return '\n\n'.join(filtered_paragraphs)


# Function to link paragraphs that are not terminated with a full stop
def link_unfinished_paragraphs(text):
    paragraphs = text.split('\n\n')
    linked_paragraphs = []

    i = 0
    while i < len(paragraphs):
        current_paragraph = paragraphs[i].strip()
        if i + 1 < len(paragraphs):
            next_paragraph = paragraphs[i + 1].strip()
            if not current_paragraph.endswith('。'):  # If not terminated with a full stop (句号)
                current_paragraph = f"{current_paragraph} {next_paragraph}"
                i += 1  # Skip the next paragraph since it's now merged with the current one
        linked_paragraphs.append(current_paragraph)
        i += 1

    return '\n\n'.join(linked_paragraphs)


# Function to process the text from each file
def process_academic_text(raw_text):
    text = remove_math_and_symbols(raw_text)
    text = remove_non_textual_elements(text)
    text = concatenate_paragraphs(text)
    text = remove_short_paragraphs(text)  # Remove paragraphs with fewer than 20 words
    text = link_unfinished_paragraphs(text)  # Link paragraphs not terminated with a full stop
    return text


def is_valid_paragraph(line):
    return re.match(r'^[A-Za-z].*\.$', line) is not None


def process_text_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = []
    stop_processing = False

    for line in lines:
        line = line.strip()

        # 如果遇到 "reference" 关键词，就停止处理剩余内容
        if re.search(r'\breference\b', line, re.IGNORECASE):
            stop_processing = True
            break

        # 检查段落是否符合条件
        if is_valid_paragraph(line):
            processed_lines.append(line)

    return '\n'.join(processed_lines)

# Iterate through all text files in the directory
for filename in os.listdir(txt_dir):
    if filename.endswith('.txt'):
        txt_path = os.path.join(txt_dir, filename)
        processed_txt_path = os.path.join(processed_txt_dir, f"Processed_{filename}")

        # Read the raw text
        with open(txt_path, 'r', encoding='utf-8') as file:
            raw_text = file.read()

        # Process the text
        #processed_text = process_academic_text(raw_text)
        processed_text = process_text_file(txt_path, processed_txt_path)

        # Save the processed text to a new file
        with open(processed_txt_path, 'w', encoding='utf-8') as file:
            file.write(processed_text)

        print(f"Processed {filename} and saved to {processed_txt_path}")
