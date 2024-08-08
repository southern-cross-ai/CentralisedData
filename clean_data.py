import re
import json
import os


def srt_to_json(srt_file, output_folder):
    pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)\n\n', re.DOTALL)

    with open(srt_file, 'r', encoding='utf-8') as file:
        srt_content = file.read()

    matches = pattern.findall(srt_content)
    subtitles = []

    for match in matches:
        subtitle = {
            'text': match[3].replace('\n', ' '),
            'extra_info': ''
        }
        subtitles.append(subtitle)

    json_content = json.dumps(subtitles, indent=4, ensure_ascii=False)
    json_filename = os.path.splitext(os.path.basename(srt_file))[0] + '.json'
    json_file = os.path.join(output_folder, json_filename)

    with open(json_file, 'w', encoding='utf-8') as file:
        file.write(json_content)

    print(f"Converted {srt_file} to {json_file}")


def convert_all_srt_in_folder(folder_path):
    output_folder = os.path.join(folder_path, 'cleaned_data')
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith('.srt'):
            srt_file = os.path.join(folder_path, filename)
            srt_to_json(srt_file, output_folder)


if __name__ == "__main__":
    folder_path = input("Please enter the folder path containing SRT files: ")
    if os.path.isdir(folder_path):
        convert_all_srt_in_folder(folder_path)
    else:
        print("The provided path is invalid. Please enter a valid folder path.")