import os
import csv

def save_files_to_csv(directory="australia_articles", output_csv="australian_articles.csv"):
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Paragraph'])  # CSV header

        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    paragraphs = content.split('\n\n')
                    title = os.path.splitext(filename)[0]  # Use filename as the title
                    for paragraph in paragraphs:
                        if paragraph.strip():  # Only save non-empty paragraphs
                            writer.writerow([title, paragraph])
                print(f"Processed {filename}")
    
    print(f"Data saved to {output_csv}")

def main():
    save_files_to_csv()

if __name__ == "__main__":
    main()
